import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id} starting to fetch data.')
    await asyncio.sleep(sleep_time)
    return {'id': task_id, 'data': f'Sample data from coroutine {task_id}'}


async def main():
    # Run two tasks concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))

    result1 = await task1
    result2 = await task2

    # Followed by the third task (taking about 4 seconds to complete)
    task3 = asyncio.create_task(fetch_data(3, 1))
    result3 = await task3

    print(result1, result2, result3)


asyncio.run(main())
