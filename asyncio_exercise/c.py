import asyncio

async def worker(tool_name:str, timeout: int):
    try: 
        print(f"{tool_name} started")
        await asyncio.sleep(timeout)
        print(f"{tool_name} finished")
    finally:
        print(f"{tool_name}cleaned")


async def run_agent():
    taska = asyncio.create_task(worker("weather", 1), name = "weather")
    taskb = asyncio.create_task(worker("search",10), name = "search")

    await asyncio.gather(taska, taskb)
    

  
    

async def main():
    try:
        await asyncio.wait_for(run_agent(), timeout=3)
    except asyncio.TimeoutError:
        print("agent timeout")
    
asyncio.run(main())