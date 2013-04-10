import zmq
import time
import sys

port = "5556"
if len(sys.argv) > 1:
    port = int(sys.argv[1])

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:%s" % port)

while True:
    #  Wait for next request from client
    message = socket.recv()
    print "Received request: ", message
    time.sleep (1)  
    socket.send("World from %s" % port)
