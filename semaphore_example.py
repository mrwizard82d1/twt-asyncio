import asyncio


async def access_resource(semaphore, resource_id):
    """Control access to `resource_id` using `semaphore."""
    async with semaphore:
        # Simulate accessing a limited resource
        print(f'Accessing resource {resource_id}')
        await asyncio.sleep(1)
        print(f'Releasing resource {resource_id}')


async def main():
    semaphore = asyncio.Semaphore(2)  # Allows 2 concurrent accesses
    await asyncio.gather(*(access_resource(semaphore, i) for i in range(5)))


if __name__ == '__main__':
    asyncio.run(main())
