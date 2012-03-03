Competing or related products
================================



`RestMQ <http://www.restmq.com/>`_ ::

    Redis based message queue, uses HTTP as transport, JSON to format a 
    minimalist protocol and is organized as REST resources.
    It is built using Python, Twisted, Cyclone (a Tornado implementation over twisted) 
    and Redis.
    
.. sidebar:: These are not the same

    Some of these are much more and different from what ZeroMQ is.
    Some of these are message/queue/broker based design that offer
    many features like persistence, reliability etc

    
`HornetMQ <http://www.jboss.org/hornetq>`_ ( `HornetMQ architecture <http://docs.jboss.org/hornetq/2.2.5.Final/user-manual/en/html/architecture.html>`_ )::

    HornetQ is an open source project to build a multi-protocol, embeddable, 
    very high performance, clustered, asynchronous messaging system.
    HornetQ is an example of Message Oriented Middleware (MoM) .
    http://en.wikipedia.org/wiki/Message_oriented_middleware
    It is written in Java
    

`Apache Kafka <http://incubator.apache.org/kafka/index.html>`_ ( `Kafka Design <http://incubator.apache.org/kafka/design.html>`_ )::

    Kafka is a distributed publish-subscribe messaging system. It is designed to support persistent messaging, high-throughput, 
    explicit support for partitioning messages over Kafka servers & support for parallel data load into Hadoop.
    

`MSMQ <http://msdn.microsoft.com/en-us/library/windows/desktop/ms711472%28v=VS.85%29.aspx>`_ ( `MSMQ architecture <http://msdn.microsoft.com/en-us/library/windows/desktop/aa374359%28v=vs.85%29.aspx>`_ ) ::

    Microsoft Message Queuing, or MSMQ, is technology for asynchronous messaging. Whenever there's need for two or more applications 
    (processes) to send messages to each other without having to immediately know results, MSMQ can be used.
    
`ActiveMQ <http://activemq.apache.org/>`_ ( `activemq architecture <https://cwiki.apache.org/ACTIVEMQ/code-overview.html>`_ ) ::

    It is open source messaging and Integration Patterns server. It is JMS compliant. It supports many cross-platform clients &
    protocols. It supports OpenWire & Stomp.
    
`RabbitMQ <http://www.rabbitmq.com/>`_ ( `RabbitMQ details <http://www.rabbitmq.com/delicious.html>`_ ):: 

    RabbitMQ provides robust messaging for applications. It is the leading implementation of AMQP, 
    the open standard for business messaging, and, through plug-ins, supports STOMP, HTTP for lightweight web messaging, 
    and other protocols. See the usage of rabbitmq in openstack: http://nova.openstack.org/devref/rabbit.html
    
`httpsqs <http://code.google.com/p/httpsqs/>`_ ::

    HTTPSQS is a Simple Queue Service based on HTTP GET/POST protocol. 

`Amazon SQS <http://aws.amazon.com/sqs/>`_ ::

    Amazon Simple Queue Service (Amazon SQS) offers a reliable, highly scalable, hosted queue for storing messages 
    as they travel between computers. By using Amazon SQS, developers can simply move data between distributed components 
    of their applications that perform different tasks, without losing messages or requiring each component to be always available.
    
    An interesting characteristics:
    When a message is received, it becomes “locked” while being processed. This keeps other computers from processing the message 
    simultaneously. If the message processing fails, the lock will expire and the message will be available again. In the case 
    where the application needs more time for processing, the “lock” timeout can be changed dynamically via the 
    ChangeMessageVisibility operation.
    

    