import asyncio


async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id} starting to fetch data...')

    # Simulate a network request or an I/O operation.
    await asyncio.sleep(sleep_time)

    return {'task_id': task_id, 'data': f'Sample data from coroutine {task_id}'}


async def main():
    tasks = []
    async with asyncio.TaskGroup() as tg:
        for i, sleep_time in enumerate([2, 1, 3], start=1):
            task = tg.create_task(fetch_data(i, sleep_time))
            tasks.append(task)

    # After all items in `TaskGroup` have completed, collect the results
    results = [task.result() for task in tasks]

    for result in results:
        print(f'Received {result=}')


if __name__ == '__main__':
    asyncio.run(main())
