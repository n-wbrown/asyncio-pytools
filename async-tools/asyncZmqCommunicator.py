"""
asyncZmqCommunicator.py

objective:  get two async coros to communicate via zmq
maybe this will help:
https://github.com/zeromq/pyzmq/blob/master/examples/asyncio/coroutines.py
"""

import asyncio
import datetime
import zmq
import zmq.asyncio

async def server(loop,index,sock):
    print("server:",index)
    message = await sock.recv()
    print("server received:",message)#this line isn't being reached 
    #sock.send(b"response")

async def client(loop,index,sock):
    print("client:",index)
    await asyncio.sleep(1)
    print("client sending")
    sock.send(b"initiating")
    #message = await sock.recv()
    #print("client received:",message)

async def ticker(loop):
    for i in range(5):
        print(".")
        await asyncio.sleep(1)

use_async = True
if not use_async:
    ctx = zmq.Context()
    s_sock = ctx.socket(zmq.REP)
    c_sock = ctx.socket(zmq.REQ)
    # bind for incoming 
    s_sock.bind("tcp://*:5559")
    # connect for outgoing
    c_sock.connect("tcp://localhost:5559")
    c_sock.send(b"hi")
    message=s_sock.recv()
    print(message)


if use_async:
    loop = asyncio.get_event_loop()
    ctx = zmq.asyncio.Context()
    s_sock = ctx.socket(zmq.REP)
    c_sock = ctx.socket(zmq.REQ)
    # bind for incoming 
    s_sock.bind("tcp://*:5555")
    # connect for outgoing
    c_sock.connect("tcp://localhost:5555")






    tasks = [
        loop.create_task(ticker(loop)),
        loop.create_task(client(loop,0,c_sock)),
        loop.create_task(server(loop,0,s_sock)),
    ]
    
    task_collection = asyncio.wait(tasks)
    loop.run_until_complete(task_collection)
    print("tasks_complete")
    loop.close()
