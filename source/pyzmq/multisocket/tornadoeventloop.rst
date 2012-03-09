PyZmq Tornado Event Loop
===================================

ØMQ Poller can be used to serve and communicate with multiple sockets. 
How ever, with ØMQ Poller, you end up with explicit blocks (under if loop) for handling
the sockets. Each socket registered with ØMQ Poller has to have an explicit "if block" to handle it.

PyZmq includes the `tornado ioloop <http://zeromq.github.com/pyzmq/eventloop.html>`_ and 
adapts its IOStream class into ZMQStream for handling poll events on ØMQ sockets. 
You can register callbacks to receive and send data.

Before you do this, you must have tornado module installed::

    pip install tornado
    
We will be redoing the previous program to take advantage of the ZMQStream and Tornado ioloop.

**pyzmq_stream_poller.py**

You must first install PyZMQ’s IOLoop.

.. literalinclude:: code/pyzmq_stream_poller.py
    :lines: 1-9
    :emphasize-lines: 7-8

We have left the command server and the topic publisher same as before.

.. literalinclude:: code/pyzmq_stream_poller.py
    :lines: 10-38

Message handlers are separated from the worker logic. 
Also note, that we stop the event loop once the worker receives the "Exit" command. 
    
.. literalinclude:: code/pyzmq_stream_poller.py
    :lines: 40-51
    :emphasize-lines: 6
    
Here, you can see that we use ZMQStream class to register callbacks.
The callbacks are the handlers that we had written earlier.
The "If blocks" in previous program has been converted to callbacks registered with tornado event loop.
There are no explicit socket handling blocks here.
    
.. literalinclude:: code/pyzmq_stream_poller.py
    :lines: 52-77
    :emphasize-lines: 5-6,12-13,15


    
In the output, you should notice that client has exited prior to the publishers 
which keeps publishing without any subscribers to process these messages::          


    Running server on port:  5556
    Running server on port:  5558
    8 server#2028
    Connected to server with port 5556
    Connected to publisher with port 5558
    Received control command: ['Continue']
    9 server#2028
    Processing ... ['9 server#2028']
    Received control command: ['Continue']
    8 server#2028
    Received control command: ['Continue']
    8 server#2028
    Received control command: ['Continue']
    8 server#2028
    Received control command: ['Continue']
    9 server#2028
    Processing ... ['9 server#2028']
    Received control command: ['Continue']
    9 server#2028
    Processing ... ['9 server#2028']
    Received control command: ['Exit']
    Received exit command, client will stop receiving messages
    Worker has stopped processing messages.
    8 server#2028
    8 server#2028
    9 server#2028




