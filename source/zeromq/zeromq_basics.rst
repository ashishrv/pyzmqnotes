ZeroMQ Basics
=======================

ZeroMQ does not provide out of box messaging system experience like ActiveMQ or RabbitMQ.
It is more of a messaging library that allows you to build your own library. It is higher 
level concept than sockets and provides as lower level conceptual framework as possible to
build messaging systems.

Key features of 0MQ are performance, simplicity and scalability.


Stack::

                           +------+
                           |ZeroMQ|
                           +------+
                            +----+
                            |TCP/|
                            |IP  |
                            +----+




.. toctree::
   :maxdepth: 1
   
   Concepts             <zeromq_concept.rst> 
   Design principles    <zeromq_design.rst>
   Scaling Up           <zeromq_scaling.rst>
   Pattern Summary      <zeromq_patternsummary.rst>



