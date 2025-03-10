import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(delay):
    print('Fetching data...')

    # Simulate an I/O operation with a call to `sleep()`
    await asyncio.sleep(delay)

    print('Data fetched')

    return {'data': 'Some data'}


# Define a coroutine that calls the first coroutine.
async def main():
    """
    Returns a coroutine that awaits data from another coroutine.
    :return: None
    """
    print('Start of main coroutine')
    task = fetch_data(2)
    print('End of main coroutine')

    # Await completion of the `fetch_data()` coroutine.
    # This action pauses the `main()` coroutine until
    # the `fetch_data()` call completes.
    result = await task
    print(f'Received result: {result}')


asyncio.run(main())
