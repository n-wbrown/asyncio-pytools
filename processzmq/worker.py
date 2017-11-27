"""
worker.py

Paired with lleader.py as the client in the clinet server model for a zmq server


"""
import zmq
import time 
if __name__ == "__main__":
    print("worker starting")
    ctx = zmq.Context()
    c_sock = ctx.socket(zmq.REQ)
    # connect for outgoing
    c_sock.connect("tcp://localhost:5555")
    c_sock.send(b"hi")

    print("worker ending")
