import asyncio
import zmq
import zmq.asyncio

ctx = zmq.asyncio.Context()

async def recv_and_process():
    sock = ctx.socket(zmq.PULL)
    sock.bind("tcp://*:%s" % 5000)
    msg = await sock.recv_multipart() # waits for msg to be ready
    reply =await async_process(msg)
    await sock.send_multipart(reply)

asyncio.get_event_loop().run_until_complete(recv_and_process())