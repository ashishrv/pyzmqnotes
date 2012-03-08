ØMQ Messaging Patterns
==============================

In distributed architecture, different parts of system interconnect and communicate with 
each other. These interconnecting systems viewed graphically represents a network topology.

Messaging patterns are network oriented architectural pattern that describes the flow of 
communication between interconnecting systems. ØMQ provides pre-optimized sockets which 
enables you to take advantage of these patterns.

Each pattern in ØMQ defines the constraints on the network topology. What systems can 
connect to each other and flow of communication between them. These patterns are designed to scale.

We will run through each of the pattern with an example. 

.. toctree::
   :maxdepth: 2
   
   PAIR      <pair.rst>
   Client/Server <client_server.rst>
   Publish/Subscribe <pubsub.rst>
   Push/Pull      <pushpull.rst>
   

   

   
   