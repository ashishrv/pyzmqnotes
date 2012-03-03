import zmq
import sys
import random

port = "5559"
context = zmq.Context()
print "Connecting to server..."
socket = context.socket(zmq.REQ)
socket.connect ("tcp://localhost:%s" % port)
client_id = random.randrange(1,10005)
#  Do 10 requests, waiting each time for a response
for request in range (1,10):
    print "Sending request ", request,"..."    
    socket.send ("Hello from %s" % client_id)
    #  Get the reply.
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
