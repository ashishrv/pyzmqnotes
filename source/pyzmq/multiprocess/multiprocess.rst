Multiprocess & pyzmq
================================

You will have noticed in the previous examples for the REQUEST-REPLY pattern that we executed the server and client separately.
This was due to the fact that each program had a while loop that would run for ever.
Only way is to invoke these little programs separately. 

This served well to understand the various ØMQ patterns and devices.
How ever, it is far better to use multiprocessing module.

This part of tutorial has nothing to do with ØMQ but how we use it with python programs.

**request_reply_processes.py**

.. literalinclude:: code/request_reply_processes.py
    :emphasize-lines: 4,6,18,34-40

Now it easy to run the server and clients in one go.

The output shows how the requests are load balanced across available servers::

    Running server on port:  5550
    Running server on port:  5552
    Running server on port:  5554
    Running server on port:  5556
    Connecting to server with ports [5550, 5552, 5554, 5556]
    Sending request  0 ...
    Received request #0: Hello
    Received reply  0 [ World from 5550 ]
    Sending request  1 ...
    Received request #0: Hello
    Received reply  1 [ World from 5552 ]
    Sending request  2 ...
    Received request #0: Hello
    Received reply  2 [ World from 5554 ]
    Sending request  3 ...
    Received request #0: Hello
    Received reply  3 [ World from 5556 ]
    Sending request  4 ...
    Received request #1: Hello
    Received reply  4 [ World from 5550 ]






