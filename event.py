"""Demonstrate the `asyncio.Event` 'primitive.'"""

# Remember, an asynchronous event is **not** an event defined,
# for example, by C#.
#
# This example is like setting a boolean flag; however, we are
# setting the flag in an asynchronous context. For example,
# one thread simply waits on an event. A second thread sets
# the event perhaps after performing some set up work or
# writing data somewhere.

import asyncio


async def waiter(event):
    print('Waiting for event to be set')
    await event.wait()
    print('Event has been set. Continuing execution.')


async def setter(event):
    await asyncio.sleep(2)  # Simulate doing some work
    event.set()
    print('Event has been set!')


async def main():
    event = asyncio.Event()
    await asyncio.gather(waiter(event), setter(event))


if __name__ == '__main__':
    asyncio.run(main())
