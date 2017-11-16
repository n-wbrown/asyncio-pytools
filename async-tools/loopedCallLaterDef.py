i"""
loopedCallLaterDef.py 

Repeatedly execute a function (not async function) using the call_soon command.
"""
import asyncio
import datetime

def display_date(end_time, loop, delay):
    print(delay,":",datetime.datetime.now())
    if (loop.time() + 1.0) < end_time:
        loop.call_later(delay, display_date, end_time, loop, delay)
    else:
        loop.stop()

loop = asyncio.get_event_loop()

# Schedule the first call to display_date()
loop.call_soon(display_date, loop.time()+5.0, loop, 1)
loop.call_soon(display_date, loop.time()+3.0, loop, 1.2)

# Blocking call interrupted by loop.stop()
loop.run_forever()
print("run_forever has been passed")
loop.close()
