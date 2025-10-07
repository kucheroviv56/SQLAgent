from fastapi import FastAPI, HTTPException
from agent.agent import run_sql_agent
from api.schemas import QueryRequest, QueryResponse  

app = FastAPI(title="SQL Agent API", version="1.0")

@app.post("/ask", response_model=QueryResponse)
def ask_agent(request: QueryRequest):
    if not request.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")
    
    try:
        answer = run_sql_agent(request.query)
        return QueryResponse(answer=answer)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Agent error: {e}")
