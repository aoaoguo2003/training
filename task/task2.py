import asyncio
import time
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


async def execute_tool(tool_name: str, seconds:int, attempt: int) ->str:
    await asyncio.sleep(seconds)

    if tool_name == "search" and attempt == 1:
        raise asyncio.TimeoutError

    if tool_name == "weather":
        raise ValueError("weather tool failed")
    
    return f"{tool_name} result"

async def safe_call_tool(request_id:str, 
                        tool_name: str, 
                        seconds:int, 
                        timeout: int,
                        attempt: int
                        ) -> dict:
    
    try:
        start_time = time.perf_counter()
        result = await asyncio.wait_for(execute_tool(tool_name= tool_name, seconds= seconds, attempt=attempt), timeout = timeout)
        
        latency = time.perf_counter() - start_time

        return {

            "request_id": request_id,
            "tool_name": tool_name,
            "success": True,
            "result": result,
            "error": None,
            "error_type": None,
            "latency": round(latency, 2)
        }

    except asyncio.TimeoutError:
        latency = time.perf_counter() - start_time

        logger.warning(
            "tool call timeout: request_id=%s, tool=%s, latency=%.2f",
            request_id,
            tool_name,
            latency
        )

        return {
            "request_id": request_id,
            "tool_name": tool_name,
            "success": False,
            "result": None,
            "error_type": "TIMEOUT",
            "message": "tool call timed out",
            "latency": round(latency, 2)
        }

    except Exception as error:
        latency = time.perf_counter() - start_time

        logger.warning(
            "tool call failed: request_id=%s, tool=%s, latency=%.2f",
            request_id,
            tool_name,
            latency
        )

        return {
            "request_id": request_id,
            "tool_name": tool_name,
            "success": False,
            "error_type": "TOOL_ERROR",
            "result": None,
            "message": str(error),
            "latency": round(latency, 2)
        }    
    

async def call_tool_with_retry(
    request_id: str,
    tool_name: str,
    seconds: int,
    timeout: int,
    max_attempts: int
) -> dict:
    start_time = time.perf_counter()

    for attempt in range(1, max_attempts + 1):
        try:
            logger.info(
                "tool attempt started request_id=%s tool=%s attempt=%d",
                request_id,
                tool_name,
                attempt
            )

            result = await asyncio.wait_for(
                execute_tool(
                    tool_name=tool_name,
                    seconds=seconds,
                    attempt=attempt
                ),
                timeout=timeout
            )

            latency = time.perf_counter() - start_time

            return {
                "request_id": request_id,
                "tool_name": tool_name,
                "success": True,
                "result": result,
                "error": None,
                "error_type": None,
                "attempts": attempt,
                "latency": round(latency, 2)
            }

        except asyncio.TimeoutError:
            logger.warning(
                "tool timeout request_id=%s tool=%s attempt=%d",
                request_id,
                tool_name,
                attempt
            )

            if attempt == max_attempts:
                latency = time.perf_counter() - start_time

                return {
                    "request_id": request_id,
                    "tool_name": tool_name,
                    "success": False,
                    "result": None,
                    "error": "tool call timed out",
                    "error_type": "TIMEOUT",
                    "attempts": attempt,
                    "latency": round(latency, 2)
                }

            delay = 2 ** (attempt - 1)

            logger.info(
                "retry scheduled request_id=%s tool=%s delay=%d",
                request_id,
                tool_name,
                delay
            )

            await asyncio.sleep(delay)

        except ValueError as error:
            latency = time.perf_counter() - start_time

            logger.error(
                "tool error request_id=%s tool=%s attempt=%d error=%s",
                request_id,
                tool_name,
                attempt,
                error
            )

            return {
                "request_id": request_id,
                "tool_name": tool_name,
                "success": False,
                "result": None,
                "error": str(error),
                "error_type": "TOOL_ERROR",
                "attempts": attempt,
                "latency": round(latency, 2)
            }



async def main():
    result = await asyncio.gather(
        call_tool_with_retry(
        "req-001", "search", 1, timeout=2, max_attempts=3
    ),
    call_tool_with_retry(
        "req-001", "weather", 1, timeout=2, max_attempts=3
    ),
    call_tool_with_retry(
        "req-001", "calculator", 1, timeout=2, max_attempts=3
    )
    )

    return result

asyncio.run(main())



