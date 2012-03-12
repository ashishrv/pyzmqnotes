Queue
==================

Here we will use the **ProcessDevice** to create a QUEUE device for connecting client and server.

**queuedevice.py** 

.. literalinclude:: code/queuedevice.py
    :lines: 1-10
    :emphasize-lines: 3
    
As noted earlier, we do not pass socket instance but socket type to ProcessDevice.
Also here, we observe the constraint on request/reply pattern by setting the high water mark to 1.

.. literalinclude:: code/queuedevice.py
    :lines: 11-18
    :emphasize-lines: 1,4-5
    
Server waits on a request to which it replies.
    
.. literalinclude:: code/queuedevice.py
    :lines: 19-30
    :emphasize-lines: 4
    
Client makes a request and waits for a reply.

.. literalinclude:: code/queuedevice.py
    :lines: 31-43
    :emphasize-lines: 4
    
We have already started our device. 
Now we will bring up the server, before bringing up the client.
Clients make a few request to server connected to our device.

.. literalinclude:: code/queuedevice.py
    :lines: 44-50
    

Output::

    Connecting a server to queue device
    Connecting a worker #0 to queue device
    Sending request #1
    Connecting a worker #1 to queue device
    Received request:  Request fron client: 0
    Received reply  1 [ Response from 6548 ]
    Sending request #2
    Received request:  Request fron client: 0
    Sending request #1
    Received reply  2 [ Response from 6548 ]
    Sending request #3
    Received request:  Request fron client: 0
    Received request:  Request fron client: 1
    Received reply  3 [ Response from 6548 ]
    Sending request #4
    Received request:  Request fron client: 0
    Received reply  1 [ Response from 6548 ]
    Sending request #2
    Received request:  Request fron client: 1
    Received reply  4 [ Response from 6548 ]
    Received reply  2 [ Response from 6548 ]
    Sending request #3
    Received request:  Request fron client: 1
    Received reply  3 [ Response from 6548 ]
    Sending request #4
    Received request:  Request fron client: 1
    Received reply  4 [ Response from 6548 ]
    
