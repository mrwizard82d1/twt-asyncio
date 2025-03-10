import asyncio


# Define a coroutine that simulates a time-consuming task
async def fetch_data(task_id, sleep_time):
    print(f'Coroutine {task_id} starting to fetch data.')
    await asyncio.sleep(sleep_time)
    if task_id == 2:
        raise RuntimeError('Oops! Something went wrong.')
    return {'id': task_id, 'data': f'Sample data from coroutine {task_id}'}



# Illustrate the `asyncio.gather()` function
async def main():
    # Run coroutines in parallel gathering the returned values from
    # multiple coroutines into `results`.
    #
    # BEWARE: `asyncio.gather()` is not the best at handling failures.
    # When a failure occurs in one coroutine, it **does not** cancel
    # the execution of other still running tasks. (In Python 3.11,
    # raising an exception **will** terminate the process. This
    # behavior may have changed since the video.) The video recommends
    # using a `TaskGroup` to handle this situation.
    results = await asyncio.gather(
        fetch_data(1, 2), fetch_data(2, 1), fetch_data(3, 3)
    )

    # Process the gathered results
    for result in results:
        print(result)


asyncio.run(main())
