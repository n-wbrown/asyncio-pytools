import asyncio
import datetime
import zmq.asyncio





async def display_date(loop,port,socket):
    end_time = loop.time() + 5.0
    while True:
        # print(datetime.datetime.now())
        print("-")
        await socket.send_string("Server message to client")
        print("server waiting")
        msg = await s.recv_multipart()
        print('received', msg)

        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)




loop = asyncio.get_event_loop()

server_port = "5556"
server_context = zmq.asyncio.Context.instance()
server_socket = server_context.socket(zmq.PAIR)
server_socket.bind("tcp://*:%s" % server_port)

client_port = "5556"
client_context = zmq.asyncio.Context.instance()
client_socket = client_context.socket(zmq.PAIR)
client_socket.connect("tcp://localhost:%s" % client_port)




loop = asyncio.get_event_loop()
# Blocking call which returns when the display_date() coroutine is done
loop.run_until_complete(display_date(loop,server_port,server_socket))
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

