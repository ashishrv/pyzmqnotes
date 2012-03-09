Polling and Sockets
================================

Using multiprocessing module helped us to launch the server, clients as processes from the same program.
How ever, you would have noticed that this still suffered from one limitation. These processes would serve only one 
socket connection. How ever, in real world a process might be connected to multiple sockets and work on data received on both.

In such situation, it is better to poll for data on the sockets. 
ZMQ provides facility for polling sockets as you can not block on recv().


.. toctree::
   :maxdepth: 2
   
   ZMQ Poller    <zmqpoller.rst>
   PyZmq Tornado Event Loop <tornadoeventloop.rst>
   

   

