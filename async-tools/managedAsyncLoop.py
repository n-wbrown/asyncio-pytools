"""
managedAsyncLoop.py

Objective: create two coroutines, one of which can create/start and kill the
other

"""

import datetime
import zmq.asyncio
import asyncio


async def worker(loop,future):
    for i in range(20):
        await asyncio.sleep(.4)
        print("worker alive",i)
    future.set_result("worker done")


async def mgr(loop,future):
    for i in range(10):
        await asyncio.sleep(.5)
        print("mgr alive", i )

        if i == 2:
            #create new task
            f = asyncio.Future()
            f = asyncio.ensure_future(worker(loop,f))

        if i == 7:
            f.cancel()
    
    future.set_result("mgr done")




loop = asyncio.get_event_loop()

future = asyncio.Future()
asyncio.ensure_future(mgr(loop,future))
# future = asyncio.ensure_future(mgr(loop,future)) # seems to do the same thing
loop.run_until_complete(future)
print("ending")
print("future result:",future.result())
loop.close()








