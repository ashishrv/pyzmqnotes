import time
import zmq
from zmq.devices.basedevice import ProcessDevice
from multiprocessing import Process

frontend_port = 5559
backend_port = 5560
number_of_workers = 2

streamerdevice  = ProcessDevice(zmq.STREAMER, zmq.PULL, zmq.PUSH)
streamerdevice.bind_in("tcp://127.0.0.1:%d" % frontend_port )
streamerdevice.bind_out("tcp://127.0.0.1:%d" % backend_port)
streamerdevice.setsockopt_in(zmq.IDENTITY, 'PULL')
streamerdevice.setsockopt_out(zmq.IDENTITY, 'PUSH')
streamerdevice.start()

def server():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://127.0.0.1:%d" % frontend_port)

    for i in xrange(0,10):
        socket.send('#%s' % i)

def worker(work_num):
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://127.0.0.1:%d" % backend_port)
    
    while True:
        message = socket.recv()
        print "Worker #%s got message! %s" % (work_num, message)
        time.sleep(1)

for work_num in range(number_of_workers):
    Process(target=worker, args=(work_num,)).start()
time.sleep(1)

server()

