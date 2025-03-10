import asyncio


async def main():
    """
    Returns a coroutine that simply prints out a message.
    :return: None
    """
    print('Start of main coroutine')


asyncio.run(main())
