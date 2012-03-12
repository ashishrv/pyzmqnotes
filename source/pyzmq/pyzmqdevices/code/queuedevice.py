import time
import zmq
from zmq.devices.basedevice import ProcessDevice
from multiprocessing import Process
import random

frontend_port = 5559
backend_port = 5560
number_of_workers = 2

queuedevice = ProcessDevice(zmq.QUEUE, zmq.XREP, zmq.XREQ)
queuedevice.bind_in("tcp://127.0.0.1:%d" % frontend_port)
queuedevice.bind_out("tcp://127.0.0.1:%d" % backend_port)
queuedevice.setsockopt_in(zmq.HWM, 1)
queuedevice.setsockopt_out(zmq.HWM, 1)
queuedevice.start()
time.sleep (2)  


def server(backend_port):
    print "Connecting a server to queue device"
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.connect("tcp://127.0.0.1:%s" % backend_port)
    server_id = random.randrange(1,10005)
    while True:
        message = socket.recv()
        print "Received request: ", message  
        socket.send("Response from %s" % server_id)

def client(frontend_port, client_id):
    print "Connecting a worker #%s to queue device" % client_id
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://127.0.0.1:%s" % frontend_port)
    #  Do 10 requests, waiting each time for a response
    for request in range (1,5):
        print "Sending request #%s" % request
        socket.send ("Request fron client: %s" % client_id)
        #  Get the reply.
        message = socket.recv()
        print "Received reply ", request, "[", message, "]"

Process(target=server, args=(backend_port,)).start()  

time.sleep(2)
    
for client_id in range(number_of_workers):
    Process(target=client, args=(frontend_port, client_id,)).start()

