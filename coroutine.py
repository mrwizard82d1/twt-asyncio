import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id} starting to fetch data.')
    await asyncio.sleep(sleep_time)
    return {'id': task_id, 'data': f'Sample data from coroutine {task_id}'}



# Use `asyncio.TaskGroup` for running multiple, parallel tasks
async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # At this point in execution, all tasks have completed
    results = [task.result() for task in tasks]

    for result in results:
        print(f'Received {result=}')


asyncio.run(main())
