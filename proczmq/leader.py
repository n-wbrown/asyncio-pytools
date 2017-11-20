"""
leader.py

Paired with worker.py as the server in the clinet server model for a zmq server
"""



import zmq
import time

if __name__ == "__main__":
    print("leader starting")
    ctx = zmq.Context()
    s_sock = ctx.socket(zmq.REP)
    # bind for incoming 
    s_sock.bind("tcp://127.0.0.1:5555")

    message = s_sock.recv()
    print(message)

    print("leader ending")