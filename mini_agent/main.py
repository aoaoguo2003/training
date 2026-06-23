#user input -- 识别需求--调用对应的工具--并发执行--输出结果
from fastapi import FastAPI 
import logging
from agent import run_agent
import asyncio
from schemas import UserRequest
from response import analysis_tool_results


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


app = FastAPI()
@app.post("/agent/run")
async def agent_run(request: UserRequest):
    result = await run_agent(
        request_id = request.request_id,
        message = request.message
    )
    summary = analysis_tool_results(result["tool_results"])
    return {
        "result": result, 
        "summary": summary
    }

async def main():
    results = await run_agent("user001", "please check the weather and use the calculator")
    response = analysis_tool_results(results["tool_results"])
    print(results)
    print(response)


if  __name__ == "__main__":
    asyncio.run(main())