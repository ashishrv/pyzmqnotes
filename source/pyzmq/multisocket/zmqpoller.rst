ZMQ Poller
=============================


In this program, we will create a command server that tells when the worker should exit.
Workers subscribes to a topic published by a publisher and prints it.
It exits when it receives "Exit" message from the command server.


**zmqpolling.py**

PUSH server that sends command to workers to continue working or exit.

.. literalinclude:: code/zmqpolling.py
    :lines: 1-20
    :emphasize-lines: 9,13-18
    
Publisher that publishes for topics "8","9","10" in random order.

.. literalinclude:: code/zmqpolling.py
    :lines: 21-36
    :emphasize-lines: 4,14
    
    
Worker that works on messages received for topic "9".
We setup zmq poller to poll for messages on the socket connection to both command server and publisher.

.. literalinclude:: code/zmqpolling.py
    :lines: 38-50
    :emphasize-lines: 11-13    
    
We poll the sockets to check if we have messages to recv and work on it.
Worker continues working until it receives exit condition. 

.. literalinclude:: code/zmqpolling.py
    :lines: 51-66
    :emphasize-lines: 4-6,9-13   
           
Finally, we fire up all the processes.

.. literalinclude:: code/zmqpolling.py
    :lines: 66-
    :emphasize-lines: 7-9    
    
Output of the program::

	Running server on port:  5556
	Running server on port:  5558
	8 server#2739
	Connected to server with port 5556
	Connected to publisher with port 5558
	Recieved control command: Continue
	9 server#2739
	Processing ...  9 server#2739
	Recieved control command: Continue
	9 server#2739
	Processing ...  9 server#2739
	Recieved control command: Continue
	9 server#2739
	Processing ...  9 server#2739
	Recieved control command: Continue
	8 server#2739
	Recieved control command: Continue
	8 server#2739
	Recieved control command: Continue
	8 server#2739
	Recieved control command: Exit
	Recieved exit command, client will stop recieving messages
	8 server#2739
	9 server#2739
	8 server#2739

           