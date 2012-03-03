import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5559")

for request in range(1,10):
    socket.send("Hello")
    message = socket.recv()
    print "Received reply ", request, "[", message, "]"
    
