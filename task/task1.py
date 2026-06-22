import time
import asyncio

import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)

async def safe_call_tool(
        request_id: str,
        tool_name: str,
        seconds: int
) -> dict:
    logger.info("call_start request_id=%s, tool_name=%s",request_id, tool_name)
    try:
        await asyncio.sleep(seconds)
        if tool_name == "weather":
            raise ValueError("weather tool failed")
        logger.info("call completed request_id=%s, tool_name=%s", request_id, tool_name)

        return {
            "request_id": request_id,
            "tool_name": tool_name,
            "success": True,
            "result": f"{tool_name} result",
            "error": None

        }
    except Exception as error:
        logger.error("error request_id=%s, tool_name=%s, error=%s", request_id, tool_name, error)
        return {
            "request_id": request_id,
            "tool_name": tool_name,
            "success": False,
            "result": None,
            "error": str(error)
        }
    

async def main():
    start_time = time.perf_counter()
    results = await asyncio.gather(
        safe_call_tool("req-001", "search", 2),
        safe_call_tool("req-001", "weather", 1),
        safe_call_tool("req-001", "calculator", 3)
    )

    latency = time.perf_counter() - start_time
    print(f"total latency: {latency:.2f} seconds")
    return results

print(asyncio.run(main()))


def analyse_tool_results(results: list[dict]) ->dict:
    success_count = 0
    fail_count = 0
    fail_tools = []
    timeout_count = 0

    for result in results:
        if result["success"]:
            success_count += 1
        else:
            fail_count += 1
            fail_tools.append(result["tool_name"])

            if result["error_type"] == "TIMEOUT":
                timeout_count += 1
    


    return {
        "total_tools": len(results),
        "success_count": success_count,
        "failure_count": fail_count,
        "failed_tools": fail_tools,
        "timeout_count": timeout_count
    }


