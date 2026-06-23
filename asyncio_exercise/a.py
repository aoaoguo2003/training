import asyncio


async def worker(name:str, seconds:int):
    print(f"{name} start")
    try: 
        await asyncio.sleep(seconds)#await 就相当于厨师告诉经理：我现在要等东西，先去安排别人吧

        print(f"{name} finished")

    finally:
        print("cleanup")


async def main():
    try: 
        task = asyncio.create_task(worker("weather", 3))

        await asyncio.sleep(1)#停止执行main一秒，回去处理其他的异步任务

        task.cancel()

        await task

    except asyncio.CancelledError:
       print("worker cancelled")

    print("task.done", task.done())
    print("task.cancelled()", task.cancelled())

asyncio.run(main())