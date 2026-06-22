import asyncio
  
async def weather_tool(request_id: str, message: str):
    await asyncio.sleep(1)

    return {
        "request_id": request_id,
        "tool_name": ":weather",
        "result": f"the weather of {message} toady is sunny"#暂时这样
    }

async def calculator_tool(request_id: str, message:str):
    await asyncio.sleep(1)

    return {
        "request_id": request_id,
        "tool_name": "calculator",
        "result": f"the sum of {message} is 77"#暂时这样
    }

TOOL_REGISTRY = {
    "weather": weather_tool,
    "calculator": calculator_tool
}



