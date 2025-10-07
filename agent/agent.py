from agent.agent_setup import init_db, init_llm, init_toolkit, init_agent
from config import LOG_FILE

def run_sql_agent(query: str, log_file: str = LOG_FILE) -> str:
    db = init_db()
    llm = init_llm()
    tools = init_toolkit(db, llm)
    agent = init_agent(llm, tools)

    final_answer = ""
    with open(log_file, "a", encoding="utf-8") as log:
        for event in agent.stream({"messages": ("user", query)}, stream_mode="values"):
            for role, message in event["messages"]:
                log.write(f"{role}: {message}\n")
            final_answer = event["messages"][-1][1]
    return final_answer
