import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id} starting to fetch data.')
    await asyncio.sleep(sleep_time)
    return {'id': task_id, 'data': f'Sample data from coroutine {task_id}'}


async def main():
    # Create `asyncio` **tasks** for multiple coroutines that we may run concurrently
    task1 = asyncio.create_task(fetch_data(1, 2))
    task2 = asyncio.create_task(fetch_data(2, 3))
    task3 = asyncio.create_task(fetch_data(3, 1))

    # Because we invoked `asyncio.create_task()` for each chunk of
    # work, awaiting these three tasks runs these tasks **in parallel**.
    # As a consequence, instead of taking about 6 seconds to complete,
    # these three tasks complete in about 3 seconds (the time of the
    # longest task).
    result1 = await task1
    result2 = await task2
    result3 = await task3

    print(result1, result2, result3)


asyncio.run(main())
