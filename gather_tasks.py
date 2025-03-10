import asyncio


async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id=} starting to fetch data.')

    # Simulate a network request or I/O operation
    await asyncio.sleep(sleep_time)

    # Return some data as a result
    return {'task_id': task_id, 'data': f'Sample data from coroutine {task_id=}'}


async def main():
    # Run coroutines concurrently and gather their results
    results = await asyncio.gather(
        fetch_data(1, 2),
        fetch_data(2,1),
        fetch_data(3,3)
    )

    # Process the result
    for result in results:
        print(f'Received {result=}')


if __name__ == '__main__':
    asyncio.run(main())
