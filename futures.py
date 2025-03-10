import asyncio


# NOTE: One typically **does not** write code using a `future`; instead, being a lower-level feature, it
# may be used by library authors to handle asynchronous operations.
#
# BEWARE: this code simply waits for a call to `set_result()` on the `future` that we create; other things
# may occur after the `set_result()` call that this code is **ignoring**.


async def set_future_result(future, value):
    # Emulate a "long" operation by sleeping
    await asyncio.sleep(2)

    # Simulate finally getting a result
    future.set_result(value)

    print(f'Set the result of the future to "{value}"')


async def main():
    # Create a future object
    loop = asyncio.get_event_loop()
    future = loop.create_future()

    # Schedule setting the future's result
    asyncio.create_task(set_future_result(future, 'Future result is ready'))

    # Wait for the future result
    result = await future
    print(f'Received {result=} from future')


if __name__ == '__main__':
    asyncio.run(main())
