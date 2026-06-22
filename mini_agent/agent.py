import asyncio

from tools import TOOL_REGISTRY

from tool_runner import call_tool_with_retry

def select_tools(message: str):
    selected_tools = []
    if "weather" in message.lower():
        selected_tools.append("weather")
    
    if "calculator" in message.lower() or "*" in message:
        selected_tools.append("calculator")

    return selected_tools

async def run_agent(request_id: str, message: str):
    selected_tools = select_tools(message)
    if selected_tools == []:
        return{
            "request_id": request_id,
            "success": False,
            "message": "No tool matched",
            "selected_tools": [],
            "tool_results": []
        }

    tasks = []

    for tool_name in selected_tools:
        task = call_tool_with_retry(request_id, tool_name, message, 3, 2)
        tasks.append(task)

    results = await asyncio.gather(*tasks)
    
    return results