==============================
Message Queue Basics
==============================

Message queues provide an asynchronous communications protocol, meaning that the sender and receiver of the message do not need to interact with the message queue at the same time. Messages placed onto the queue are stored until the recipient retrieves them.

Some message queues work within a system or application while others allow passing of messages between remote system. These kinds are also called message-oriented middleware.


Deployment
-----------------

Typical deployment::

                          Adiminstrator
                          configures
                                |
                            +----------+
                            |Messaging |
                            |Middleware|
                            +----------+
        upstream                | midstream           downstreams
                           +-------------+          +------------+
    +------------+         |Named        |<---------|Applications|
    |Applications|-------> |Message Queue|   |      +------------+
    +------------+   |     +-------------+   |
                     |                       connect
                     |                       to get messages
                 connect to
                 publish messages
                 


Message Queue Properties
-------------------------------

Various flavors and additional properties / services are provides along with basic operations.

* *Durability*: If the messages remain in memory or are persisted via storage so that they are not lost
* *Security policies*: Who should be able to access these messages or queues
* *Message purging policies*: Do these messages live for ever or do they expire?
* *Filtering of messages*: Upstream / Midstream or Downstream ?
* *Routing policies*: In a system with many queue servers, what servers should receive a message or a queue's messages?

 * *Direct vs Store&Forward routing*: Direct messages are sent directly to the computer where the destination queue resides and do not access the directory service.

* *Batching policies*: Should messages be delivered immediately or wait a bit and try to deliver many messages at once?
* *Delivery*: When should a message be considered delivered? When one queue has it? Or when it has been forwarded to at least one remote queue? Or to all queues?

 * *Delivery policies*: Are there guarantees that messages are delivered at least once?

* *Transactional vs Non-transactional messages*: Sending a transactional message can be included with other operations—such as updating a database in an atomic process that can be aborted if any part of the transaction fails. Transactional messages guarantee exactly-once and in-order delivery.
* *Ordered Messages*: Some queues provide guarantees of ordered delivery, while others do not. If your messages consist of updates to state, then two messages updating the same entity, may result in inconsistency if their order is switched. 


End Notes
----------------

One interesting aspect, I have learnt is that all the various characteristics may not be required by all messages. 
If messages are about *changes of states* then it is important that they arrive in order, otherwise not. 
Similarly certain messages do not required durability, while for some that might be of utmost importance. 
In certain cases, guaranteed delivery to endpoint is very important but for some we could relax that rule.

 




