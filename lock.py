"""Using (low-level) locks with `asyncio`."""

import asyncio


# A shared variable
shared_resource = 0


# An `asyncio` lock
lock = asyncio.Lock()


async def modify_shared_resource():
    global shared_resource
    # The `async with` expression acquires the lock (and releases it when the block exits
    async with lock:
        # Critical section starts
        print(f'Resource before modification: {shared_resource}')
        shared_resource += 1  # Modify the shared resource
        await asyncio.sleep(1)  # Simulate an I/O operation
        print(f'Resource after modification: {shared_resource}')
        # Critical section ends


async def main():
    # Runs `modify_shared_resources()` for 5 concurrent "consumers"
    await asyncio.gather(*(modify_shared_resource() for _ in range(5)))


if __name__ == '__main__':
    asyncio.run(main())
