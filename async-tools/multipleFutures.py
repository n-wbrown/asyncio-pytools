"""
zmqClientServer.py

Try to make zmq and asnycio play nice together in a client/server model.

Bonus objective: Also use the zmq asyncio tools
"""

import asyncio
import datetime
import zmq
import time





async def server(loop,port,socket):
    end_time = loop.time() + 2.0
    while True:
        print(datetime.datetime.now())
        #print("-")
        #await socket.send_string("Server message to client")
        #print("server waiting")
        #msg = await s.recv_multipart()
        #print('received', msg)
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(.2)




loop = asyncio.get_event_loop()

#server_port = "5556"
#server_context = zmq.asyncio.Context.instance()
#server_socket = server_context.socket(zmq.PAIR)
#server_socket.bind("tcp://*:%s" % server_port)
#
#client_port = "5556"
#client_context = zmq.asyncio.Context.instance()
#client_socket = client_context.socket(zmq.PAIR)
#client_socket.connect("tcp://localhost:%s" % client_port)




loop = asyncio.get_event_loop()

print("run_until_complete(coro)")
loop.run_until_complete(server(loop,None,None))

print("run_until_complete(future)")
z = asyncio.ensure_future(server(loop,None,None))
loop.run_until_complete(z)

print("run_until_complete(multiple)")

tasks = [
    loop.create_task(server(loop,None,None)),
    loop.create_task(server(loop,None,None))
]
task_collection = asyncio.wait(tasks)
loop.run_until_complete(task_collection)







loop.close()



# def server( end_time, loop, delay, port, socket):
#     print(delay,":",datetime.datetime.now())
#     if (loop.time() + 1.0) < end_time:
#         socket.send_string("Server message to client")
#         msg = await socket.recv()
#         print(msg)
#         loop.call_later(delay, server, end_time, loop, delay, port, socket)
#     else:
#         loop.stop()



# def client( end_time, loop, delay, port, socket):
#     print(delay,":",datetime.datetime.now())
#     if (loop.time() + 1.0) < end_time:
#         msg = await socket.recv()
#         print(msg)
#         socket.send_string("client message to server")
#         loop.call_later(delay, client, end_time, loop, delay, port, socket)
#     else:
#         loop.stop()




# loop = asyncio.get_event_loop()

# server_port = "5556"
# server_context = zmq.asyncio.Context.instance()
# server_socket = server_context.socket(zmq.PAIR)
# server_socket.bind("tcp://*:%s" % server_port)

# client_port = "5556"
# client_context = zmq.asyncio.Context.instance()
# client_socket = client_context.socket(zmq.PAIR)
# client_socket.connect("tcp://localhost:%s" % client_port)

# loop.call_soon(server, loop.time()+5.0, loop, 1, server_port, server_socket)
# loop.call_soon(server, loop.time()+3.0, loop, 1.2, client_port, client_socket)





# loop.run_forever()
# loop.close()

