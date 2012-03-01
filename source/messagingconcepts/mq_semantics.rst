Message Queue Semantics
====================================

A **queue** holds messages, it is a FIFO buffer. 

An **exchange** routes messages, it is an algorithm, with no storage. 

A **binding** is a relationship between an exchange and a queue, it tells the exchange what queues expect what messages. 
Bindings are independent and orthogonal except that a queue will not get the same message more than once. 

AMQP defines a set of exchange types each corresponding to a specific routing algorithm, and lets applications create and use exchange instances at runtime.
It lets applications create queues at runtime, and bind them dynamically to zero or more exchanges. 
It then lets applications consume messages off their queue or queues.

