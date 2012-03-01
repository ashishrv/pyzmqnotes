Rationale behind AMQ & AMQP
===============================

Middleware:

    middleware consists of software agents acting as an intermediary between different application components.
    
Centralized Messaging Servers
------------------------------------

The basic reason of being of a messaging server is to reduce the interconnection complexity of a network. 
In a network with no central messaging server, each application does its own message queueing and routing. 
We would use existing protocols such as SOAP to connect peers. 
If the whole network has to be reachable, each peer needs to connect to every other peer, which results in up to n(n−1)/2 connections::

               +---+         +---+
               |App|.........|App|
               +---+       .'+---+
                 |  `-. .-'    |
                 |    .'-.     |
               +---+.'    `-.+---+
               |App|---------|App|
               +---+         +---+
               
This is the traditional way of constructing ad-hoc application networks and it is a painfully unscalable model.

There are two alternatives: 

1. Peer-to-peer networks 
2. A central messaging server moves the messaging complexity to one point

Messaging server architecture::

            +---+               +---+
            |App|`.          .-'|App|
            +---+  `-.+--+.-'   +---+
                      |MS|
                    .'+--+`-.
            +---+.-'         `-.+---+
            |App|               |App|
            +---+               +---+
            
Messaging servers usually provides disk-based or memory-based FIFO data stores also called message queues 
that many applications can write to and read to simultaneously.

It is often significantly cheaper to develop independent applications and connect them using good middleware, than to develop a single all-encompassing application.

Existing Middleware Options
-------------------------------

1. Niche middleware: connecting components on a single platform, or for a single language environment
2. General-purpose middleware products (IBM MQ Series, BEA Tuxedo): Expensive & Complex
3. Java middleware servers: not focussed on standards
4. Limited scope middleware standards: JMS exclusively for Java applications, CORBA uses a complex object-centered model which is unsuitable for many kinds of application.



Functional requirements
----------------------------------

Messaging Models::

    1. Store-and-forward with many writers and one reader.
    2. Transaction distribution with many writers and many readers.
    3. Publish-subscribe with many writers and many readers.
    4. Content-based routing with many writers and many readers.
    5. Queued file transfer with many writers and many readers.
    6. Point-to-point connection between two peers.
    7. Market data distribution with many sources and many readers.
    
Store-and-Forward
~~~~~~~~~~~~~~~~~~~~~~~~~~

* Messages contain business data - database updates, client profiles, electronic documents.
* Messages are addressed to specific applications.
* Messages cannot be lost, once accepted by the middleware, and until delivered to the reader.
* Delivery synchronization is defined by the reader, signaling the middleware when it is ready to receive messages.
* The volumes involved can be up to 10-1,000 messages per second
* Each message being 1-100Kb large. 
* Emphasis is on reliability and security rather than on raw performance.

Transaction Distribution
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* A message is a unit of work rather than a unit of information
* Message delivery is enclosed in a transaction so that errors in processing can be communicated back to the queue.
* When a transaction is aborted, the message is re-queued and sent to a different reader. 

Publish-Subscribe
~~~~~~~~~~~~~~~~~~~~~~~~~~

* single message can be delivered to many readers
* pub-sub is much more scalable than messaging queuing
* Routing is done using a topic name 
* readers subscribe by asking for specific topics
* The response time for pub-sub systems used for event notification is often very important
* the emphasis is on performance and specific qualities-of-service rather than reliability.

Content-Based Routing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Recipient for a message is determined not by the sender but by the contents of the message. 
* CBR tends to be computationally expensive

Queued File Transfer
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* store-and-forward systems can be requested to transfer messages as large as or greater than several GB in size
* This can be thought of as unifying file transfer with enterprise messaging.
* Messages are provided to the network as files (rather than memory blocks)
* Files are delivered in the order received by the destination.
* Files can be resent partially to recover from network failures.


Point-to-Point Connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Follows the model of a remote procedure call (RPC)
* RPC usually has visibility to the end-user of an application, so must complete rapidly.
* Messages contain units of work 
* Messages are addressed to specific applications.
* RPC systems do not hide much complexity from the developer.


How does AMQ fit in?
-----------------------------

Interoperability
~~~~~~~~~~~~~~~~~~~~

AMQ tries to **improve interoperability** by standardizing certain distinct layers on top of transport for message queuing systems.

* Wire-level protocol : **AMQP**
* Semantics of the command set : A general-purpose modular framework for the server semantics (the **AMQ framework**)
* APIs

Wire-level protocol and command semantics, needs absolute conformity in order to create functional interoperability, even if the APIs differ.
The commands to send messages, read messages, start and commit transactions must look the same, and must work the same.

Performance
~~~~~~~~~~~~~~~~~~~~~

Middleware is always a bottleneck. The key to making a "fast" protocol is to make a protocol that can be 

* read and written in large chunks (not character by character)
* uses a minimum of network capacity (since every octet costs time)
* minimum of chatter (since every round trip costs a serious amount of time)


Models to follow
~~~~~~~~~~~~~~~~~~~~~~

**Email**: 

    Closest parallel to middleware is SMTP

The significant differences between email and the other protocols mentioned are 

* **Asynchrony** : messages are pushed towards their recipients
* **Persistence** : data is stored safely until everyone who needs it has finished using it.
* Allow messages to be routed by content as well as by address

**Lessons from Linux**:

    a good example of how a small but well-designed core can become the basis for large and 
    complex products through the gradual accretion of add-ons and extensions over time.
    
    
Characteristics of MQ that varies
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. The **size of the message**: very small to very large.
2. The **type of the message**: application data, files, and possibly other types such as streamed data.
3. The **reliability requirement**: low to very high.
4. The **latency requirement**: unimportant to critical.
5. The **routing model**: single named recipient, fanout, name-based routing, content-based routing, etc.
6. The **distribution model**: single reader, message fanout, and workload distribution.




The AMQ Framework
-----------------------------

Earlier the two main technologies: store-and-forward (S&F) and pub-sub (pub-sub) were implemented separately. 
Java Messaging (JMS) tried to combine the two types by masking their differences under a broader term destination.

* This usually makes thing brittle & difficult. 
* The "destination" concept is semantically too confused to act as a basis for a server design, and by extension, protocol design.

AMQ break S&F and pub-sub into a component grammar that lets you rebuild these two ways of working, but also construct new semantics.

* The AMQ component grammar is called the "AMQ framework".
* It is a language that lets architects create arbitrary middleware engines. It specifies: 

 * A component (the message queue) that holds messages in a FIFO queue
 * A component (the exchange) that routes messages into message queues.
 * A component (the binding) that defines the routing paths.
 
* S&F consists of a simple exchange and sophisticated message queues.
* pub-sub consists of a sophisticated exchange and simple message queues.

AMQP
----------------

Goal was a fast and compact syntax capable of handling a complex set of commands and data.

It consists of many pieces:

1. A general framing format.
2. A general way of carrying commands.
3. A general way of carrying data.
4. A general way of handling errors.



Designing AMQP framework
-------------------------------

* Under the hood, the two extreme cases -  pub-sub and S&F looks the same
* In pub-sub, the message queue is mostly hidden but there
* In case of routing of message, the difference is that in pub-sub model, there is no direct coupling

 * The publisher does not know who the recipient is for a specific message.

* All matching (routing decisions) can be done by specialized engines.

 * The algorithm for doing high-speed topic matching is quite specific and has no place in S&F messaging.
 
The design is encapsulated as `message semantics <../../messagingconcepts/mq_semantics.html>`_

AMQP framework design focused on:

1. "**Routing key**": This is like the "To" field of an email message. All messages have a routing key.
2. The matching and routing engine is called an "**exchange**". The exchange accepts messages, examines them, and routes them to a set of message queues as necessary.
3. The tie between message queue and exchange is called a "**binding**". A binding is a specification, telling the exchange what messages to route into the queue.


The Exchange Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~

An exchange is a logic engine that accepts messages, inspects them, and on the basis of pre-declared routing tables, 
routes the messages to a set of message queues.

This satisfies the functional requirement:

1. An exchange that routes on the routing key. This implements S&F transaction distribution, queued file-transfer, point-to-point.
2. An exchange that routes unconditionally. This implements fanout.
3. An exchange that routes on a routing key pattern. This implements pub-sub.
4. An exchange that routes on message header fields. This implements market data.
5. Arbitrary exchanges that route on the message contents. These implement content-based routing, message transformation, etc.


Exchange type is an algorithm while an instance of exchange type routing tables and binding information.

Default wiring
####################

The full logic of creating and using a queue involves, creation of queue, **binding of queue to 1 or more exchanges** and consuming from the queue. 
AMQ provides default binding techniques which allows for **binding of queue to 0 or more exchanges**.

Mandatory Routing
#######################

A message delivery can fail when a exchange does not have a message queue to route a message to it. 

1. Exchange could silently drop it
2. Exchange can signal the application that it failed to route the message

This option can set when publishing a message.

AMQP is asynchronous for all performance-critical commands and only way for an application to get success/failure status 
for an asynchronous command is to wrap it in a transaction, which creates a synchronous envelope. This makes it slow.
How ever other ways to signal the failure is to treat the condition as exceptional and signal by means of stopping the session or stopping the whole connection.

Message Queue Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The "message queue" is an AMQ concept that abstracts the FIFO message stores that form the heart of most messaging servers. 
AMQ allows you to create various types explicitly at run time.

Private vs. Shared
#########################

* When a message queue is shared by multiple consumers, its messages are distribute amongst these consumers. 
* When a message queue is private to one consumer, its messages are sent only to that consumer.

Durable vs. Temporary
#########################

A durable message queue is like a configured object: when the server (re)starts, the message queue is present and active. 
Temporary queues are destroyed when the server shuts down.

Automatic Deletion
########################

when the last service provider has stopped working with a message queue, the server deletes the queue.


Content Class Concept
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Content class is like an object-oriented class (without the inheritance), and consists of a set of property definitions plus a set of methods.

*Each message is an instance of a content class*.

There are three content classes as provided by AMQ framework:

1. Basic content, for the standard messaging domain.
2. File content, for queued file transfer.
3. Stream content, for streamed data (video, voice, or other data).

The exchanges and message queues are able to handle any content type. 
This means AMQ provides the same routing and queuing mechanisms for streamed data, and large files, as it does for typical messages. 


Reliability vs. Performance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In general the trade-off between message reliability and speed is that the more reliable the system, the slower it will run.

1. The type of memory used: system RAM or disk storage. If we want messages to survive a system reboot, they must be on disk.
2. The degree of redundancy: none, mirrored. This is called 1-safe, 2-safe, etc. If we want to survive a system failure (e.g. disk crash) we need redundancy.
3. The redundancy distance: if we want a redundant system to survive a physical event (fire, lightning, hurricane), it must be physically separated from its peer.
4. The degree of transactionality: none, partial, full. If we want to be sure that the data was safely written in a coherent manner we must use transactions (of varying complexity).

Designing the Wire-Level Protocol
----------------------------------------

The key elements are:

1. The protocol header: how connections are opened.
2. The framing layer: how data is delimited on the connection.
3. The data types: how data fields are formatted.
4. The method layer: how methods are carried between peers.
5. The content layer: how content is carried between peers.

Protocol header is an agreement between client & server about framing. Everything that follows the protocol header is built on frames.























