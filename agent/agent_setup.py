from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain import hub
from langchain.chat_models import init_chat_model
from langgraph.prebuilt import create_react_agent
from config import DB_URI, LLM_MODEL, LLM_PROVIDER

def init_db():
    return SQLDatabase.from_uri(DB_URI)

def init_llm():
    return init_chat_model(LLM_MODEL, model_provider=LLM_PROVIDER)

def init_toolkit(db, llm):
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    return toolkit.get_tools()

def init_agent(llm, tools):
    prompt_template = hub.pull("langchain-ai/sql-agent-system-prompt")
    system_message = prompt_template.format(dialect="postgresql", top_k=10)
    return create_react_agent(model=llm, tools=tools, prompt=system_message)
