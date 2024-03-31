import asyncio


async def main():

    # await number()

    # task1 = asyncio.create_task(letter())
    # task2 = asyncio.create_task(func2())

    # await task1
    # count = await task2
    # print(f"\nmain: received count {count} from task2")

    task1 = asyncio.create_task(letter())
    task2 = asyncio.create_task(func2())
    await number()
    await task1
    count = await task2
    print(f"\nmain: received count {count} from task2")


async def letter():
    print("A")
    await asyncio.sleep(1)
    print("B")


async def number():
    print("One")
    await asyncio.sleep(1)
    print("Two")


async def func2():
    print("func2: counting", flush=True)
    count = 0
    for _ in range(1000000):
        count += 1

    print(f"func2: done (counted to {count})", flush=True)
    return count


if __name__ == "__main__":
    asyncio.run(main())
