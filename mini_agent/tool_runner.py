from tools import TOOL_REGISTRY
import asyncio
import time

async def call_tool_with_retry(request_id, tool_name, query, timeout, max_attempts):
    if tool_name not in TOOL_REGISTRY:
        return {
            "request_id": request_id,
            "tool_name": tool_name,
            "success": False,
            "result": None,
            "error": f"unsupported tool: {tool_name}",
            "error_type": "UNSUPPORTED_TOOL",
            "attempts": 0 
        }
    
    tool_function = TOOL_REGISTRY[tool_name]
    start_time = time.perf_counter()

    for attempt in range(1, max_attempts +1):
        try:
            result = await asyncio.wait_for(
                tool_function(request_id, query),
                timeout = timeout
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
            
            else:
                delay = 2**(attempt - 1)
                await asyncio.sleep(delay)

        except Exception as error:
            latency = time.perf_counter() - start_time
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



