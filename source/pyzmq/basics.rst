ØMQ and pyzmq Basics
=======================

Installation
---------------------

It is better to install it using virtualenv/virtualenwrapper::

    pip install pyzmq-static
    
    
ØMQ Version
-------------------

2.1.7::

    import zmq
    print zmq.pyzmq_version()
    
    

ØMQ context
--------------------

Before using any ØMQ library functions, the caller must initialize a ØMQ context::

    import zmq
    import time
    context = zmq.Context()
    
Contexts are thread safe unlike sockets. An application can create and manage multiple contexts.

ØMQ sockets
----------------------

zmq sockets are created from the initialized context::

    socket = context.socket(zmq.REP)

* zmq sockets are of certain types which enable one of the various communication patterns. 
* zmq socket type must be passed during socket creation. 

    



