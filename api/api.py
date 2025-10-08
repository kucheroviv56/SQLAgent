from fastapi import FastAPI, HTTPException
from agent.agent import run_sql_agent
from api.schemas import QueryRequest, QueryResponse  
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="SQL Agent API", version="1.0")

@app.post("/ask", response_model=QueryResponse)
def ask_agent(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        message = run_sql_agent(request.query, log_file="agent.log")
        if hasattr(message, "content"):
            answer = message.content
        else:
            answer = str(message)

        return QueryResponse(answer=answer)
    except Exception as e:
        import traceback
        tb = traceback.format_exc()
        logger.error("Ошибка агента: %s\n%s", e, tb)
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")
