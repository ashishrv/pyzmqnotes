ZeroMQ Design Principles
==================================

Topologies
-----------------

Topology is the primary concept in ØMQ. Some of it's key properties are:

* Topology is a graph 

 * where nodes are applications
 * lattices are data channels between applications.
 
* All the applications agree on the same wire protocol for their business logic.
* The graph is compact

 * any two nodes are connected either directly or 
 * via one or more intermediaries.
 

On comparing with Class as design tool::

    Just like "Classes" can be used to design a modular program, you could
    also create a mess. There are no single right way to split business logic into topologies.
    
    The only rule of the thumb is that topology is an atomic unit of scaling. 
    You can scale topology as a whole, but you cannot scale just one aspect of it.
    
Transports
----------------

Underlying transports retain their native characteristics without providing a common, all encompassing interface on top::


             +------------------+
             |Messaging Patterns| Message routing layer
             +------------------+
              +---+ +----+ +---+
              |   | |    | |   |  Lightweight wrapper
              +---+ +----+ +---+
              +---+ +----+ +---+
              |TCP| |SCTP| |PGM|  Underlying transport layer
              +---+ +----+ +---+



* IP layer abstracts away the need to find the route to destination host.
* TCP abstracts away the fact that network is inherently lossy and provides reliability guarantees.
* ØMQ abstracts away the need to specify a particular network location to send the data to. 

 * Messages are sent to a topology, not to a specific endpoint.
 * Topology is tied to particular business logic
 * When you are sending a message to a topology, you are basically asking for a specific service to be provided
 
Messaging Patterns
----------------------

Routing algorithms differ in various topologies. 
For some, you just need to inform (Pub/Sub), while other requires a response (req/reply).
ØMQ reflects this fact by defining several so called "messaging patterns".
Messaging pattern defines both the protocol used for communication between the nodes and functionality of an individual node.
In 0MQ, different patterns behave like different protocols. 
You cannot connect publish/subscribe node to request/reply node the same way as you cannot connect TCP endpoint to SCTP endpoint.
This strict separation is necessary to provide guarantees about the behavior of the topology as a whole. 

Other messaging systems choose to offer generic routing infrastructure that allows user to build & mix routing algorithm on top of it.
For example: AMQP model of exchanges, bindings and consumers
ZeroMQ like JMS (Topics & Queues) delivers pre-packaged messaging patterns.


Hop-by-Hop vs. End-to-End
--------------------------------

A good feature of Internet stack is the clean separation of hop-by-hop functionality (IP) and end-to-end functionality (TCP, UDP, SCTP et al.) 
The idea is that every node in the network has to implement IP, however, only the endpoints using a specific end-to-end protocol, 
such as TCP, have to be aware of it::

                    Endpoint             Endpoint
                    +---+                +---+
                    |TCP|   Routers      |TCP|
                    +---+                +---+
                    +---+   +---+  +---+ +---+
                    |IP |   |IP |  |IP | |IP |
                    +---+   +---+  +---+ +---+
                    
                    
ØMQ adheres to this design principle. It provides separate hop-by-hop layer (denoted by socket types beginning with "X") and end-to-end layer::

          Endpoint                                Endpoint

          +----+    0MQ               0MQ         +----+
          |REQ |    Device            Device      |REP |
          +----+                                  +----+
          +----+   +----++----+   +----++----+    +----+
          |XREQ|---|XREP||XREQ|---|XREP||XREQ|----|XREP|
          +----+   +----++----+   +----++----+    +----+
          

Hop-to-hop layer is responsible for routing and end-to-end layer can provide additional services, such as reliability, encryption etc.

Actual ØMQ architecture::

          +---------+   +---------+  +----+
          |PUB/SUB  |   |REQ/REP  |  |....| End to End
          +---------+   +---------+  +----+
          +---------+   +---------+  +----+
          |XPUB/XSUB|   |XREQ/XREP|  |....| Hop to Hop
          +---------+   +---------+  +----+
          +-------------------------------+
          |Underlaying    Transport       | Transport
          +-------------------------------+
          

Key Design Principles
----------------------------


Uniformity Principle
~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 

    Uniformity principle states that it should not matter to which node in the topology you connect your application to. 
    The service provided should be the same.

Let's consider an anti-pattern that breaks this principle in a pub/sub topology::

          +-+      +-+
          |A|      |B|
          +-+      +-+
           |        |
           |  |--------|
           | +-+      +-+
           |-|1|      |2|
             +-+      +-+
              .        .
            ? .  +-+   . ?
              ...|C|....
                 +-+
                 
* If "C" gets connected to "1", then it receives messages from both "A" & "B".
* While if "C" gets connected to "2", then it receives messages from "B" only.
* This topology violates "uniformity principle".


Scalability Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 

    Scalability principle states that when topology cannot handle the load, (overloaded or congested),
    it should be possible to solve the problem by adding new nodes to the topology.

An anti-pattern violating the scalability principle: breaking an application into fixed number of functional blocks.

Splitting a monolithic application combining both accounting and human resource functionality::

         +----------+         +---------+
         |Accounting|---------|Human    |
         +----------+         |Resources|
                              +---------+
                              
When the two-node systems fails to cope with the load, you can not scale without re-writing the functional pieces again.

A more complex case of non-scalable anti-pattern is distributed logging::

                  +---+    +---+    +---+
                  |App|    |App|    |App|
                  +---+    +---+    +---+
                    |        |        |
                    |------- |   -----|
                          +------+
                          |Logger|
                          +------+
                          

As number of applications to log grows, the load on the logger increases, until it is not capable to handle the load. 
Adding intermediary nodes doesn't solve the problem. All the messages have to get to the logger no matter whether there are.

* To make this kind of "data collection" pattern scalable, intermediary nodes have to aggregate the messages.
* Send fixed amount of messages downstream not depending on number of upstream applications. 
* For ex: "Pub/Sub" pattern uses this kind of aggregation pattern for forwarding subscriptions.


Internet conforms to scalability principle. 
New nodes can be added at any time, whether end-user boxes or intermediary infrastructure, 
without compromising the functionality or the performance of the Internet as a whole
    

Interjection Principle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 

    Interjection principle states that inserting an intermediary node into the topology should not change the behavior at the endpoints. 
    Interjection of intermediary node can be used to scale up a topology.
    
Example::

       Original               Topology
         Topology        with interjected node
        +-+                    +-+
        |A|                    |A|
        +-+                    +-+
         |       ----->         |
         |                      |
     ---------              --------
     |   |   |              |      |
    +-+ +-+ +-+            +-+    +-+
    |B| |C| |D|            |B|    |I|
    +-+ +-+ +-+            +-+    +-+
                                   |
                                   |
                                 ------
                                  |   |
                                 +-+ +-+
                                 |C| |D|
                                 +-+ +-+

The behavior at endpoint A changes when intermediary is inserted into the topology. 
Instead of reporting 3 peers it now reports 2 peers. 
Thus, exposing the number of connected peers breaks the interjection principle.

Interjection principle is crucial for the way Internet works. 
If changing the topology in the middle — say when backbone operator adds new routers — would break the applications at the endpoints, 
the Internet would very quickly get into the state of disrepair.


 

















