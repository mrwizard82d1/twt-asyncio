import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay, id):
    print(f'Fetching data... {id=}')

    # Simulate an I/O operation with a call to `sleep()`
    await asyncio.sleep(delay)

    print(f'Data fetched. {id=}')

    return {'data': 'Some data', 'id': id}


# Define a coroutine that calls the first coroutine.
async def main():
    """
    Returns a coroutine that awaits data from another coroutine.
    :return: None
    """
    task1 = fetch_data(2, 1)
    task2 = fetch_data(2, 2)

    # At first glance, we might think than `task1` and `task2` are
    # running in-parallel; however, because we are awaiting each task,
    # they **do not** run in parallel but **sequentially**. That is,
    # running this code takes **4** seconds instead of about 2 seconds.

    result1 = await task1
    print(f'Received result: {result1}')

    result2 = await task2
    print(f'Received result: {result2}')


asyncio.run(main())
