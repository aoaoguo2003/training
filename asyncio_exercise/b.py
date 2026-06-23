import asyncio


async def worker(name:str, seconds:int):
    print(f"{name} start")
    try: 
        await asyncio.sleep(seconds)

        print(f"{name} finished")

    finally:
        print("cleanup")


async def main():
    taska = asyncio.create_task(worker("A", 2))
    taskb = asyncio.create_task(worker("B", 5))
    taskc = asyncio.create_task(worker("C", 10))
    tasks = [taska, taskb, taskc]

    await asyncio.sleep(3)#停止执行main3秒，回去处理其他的异步任务
    for task in tasks:
        if not task.done():
            task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)


    for task in tasks:
        print(f"{task} is done: {task.done()}")
        print(f"{task} is cancelled: {task.cancelled()}")

asyncio.run(main())