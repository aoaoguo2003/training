from fastapi import FastAPI, HTTPException, status
from schemas import AgentRequest
import logging
import time
from responses import success_response, error_response
from services import run_agent_logic
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/health")
def health():
    return {
        "status": "ok",
        "service": "agent-api"
    }

@app.post("/agent/run")
def run_agent(request: AgentRequest):
    start_time = time.perf_counter()
    logger.info("request start, request_id=%s, user_id=%s, prompt_length=%d", request.request_id, request.user_id, len(request.prompt))
    
    
    result = run_agent_logic(request)
    latency = time.perf_counter() - start_time
    logger.info(
        "request completed request_id=%s success=%s latency=%.3f",
        request.request_id,
        result["success"],
        latency
    )

    return result

