"""
repeatedFuture.py

Use futures to manage a repeated async function.

Taken from stackexchange 

"""

import asyncio 

async def periodic():
    while True:
        print("step")
        await asyncio.sleep(1)

def end(task):
    task.cancel()

task = asyncio.ensure_future(periodic())
loop = asyncio.get_event_loop()
loop.call_later(5,end,task)

try:
    loop.run_until_complete(task)
except asyncio.CancelledError:
    pass
