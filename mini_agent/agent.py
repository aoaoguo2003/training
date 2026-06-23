import asyncio

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
            "error_type": "no_tool_matched",
            "tool_results": []
        }

    tasks = []

    try:
        for tool_name in selected_tools:
            task = asyncio.create_task(call_tool_with_retry(request_id, tool_name, message, 3, 2), name=f"{request_id}:{tool_name}")
            tasks.append(task)

        for task in tasks:
            print(task.get_name())

        results = await asyncio.gather(*tasks)
        
        success_count = 0
        
        for result in results:
            if result["success"]:
                success_count += 1

        return {
            "request_id": request_id,
            "success": success_count > 0,
            "message": "Agent execution completed",
            "selected_tools": selected_tools,
            "error_type": None,
            "tool_results": results
        }
    except asyncio.CancelledError:
        #未运行的task都取消运行，已完成的保留原任务结果
        for task in tasks:
            if not task.done():
                task.cancel()
        #等待所有 Task 结束并完成清理
        await asyncio.gather(
            *tasks,
            return_exceptions=True
        )

        raise

