Streamer
=============================

Here we will use the **ProcessDevice** to create a STREAMER device for pipelining server and workers.


**streamerdevice.py** 



.. literalinclude:: code/streamerdevice.py
    :lines: 1-9
    :emphasize-lines: 3
    
    
The key difference here is that while *zmq.device* take Socket objects as arguments, 
*zmq.devices.basedevice.ProcessDevice* takes socket types.

.. literalinclude:: code/streamerdevice.py
    :lines: 10
    :emphasize-lines: 1
    

For each configuration method (bind/connect/setsockopt), the proxy methods are prefixed with \"in\_\" or \"out\_\"
corresponding to the frontend and backend sockets.

.. literalinclude:: code/streamerdevice.py
    :lines: 11-14
    :emphasize-lines: 1-4
    
    
Finally, you can start the device in background.    

.. literalinclude:: code/streamerdevice.py
    :lines: 15-16
    :emphasize-lines: 1

Server and workers in the pipeline have been kept relatively simple for illustration purposes.

.. literalinclude:: code/streamerdevice.py
    :lines: 16-
    :emphasize-lines: 3-4, 10-11  

    
The requests are farmed out to workers in load balanced manner::

    Worker #1 got message! #0
    Worker #0 got message! #1
    Worker #1 got message! #2
    Worker #0 got message! #3
    Worker #1 got message! #4
    Worker #0 got message! #5
    Worker #1 got message! #6
    Worker #0 got message! #7
    Worker #1 got message! #8
    Worker #0 got message! #9



