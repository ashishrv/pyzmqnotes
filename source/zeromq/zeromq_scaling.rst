Scaling up with ZeroMQ
==================================

Scenario #1
~~~~~~~~~~~~~~~~~~~~


Consider data distribution using "Pub/Sub" model across WAN between offices.
For example: sending stock prices to all the broker's computing application on their desktop.

Initial approach with centralized server::

                             .
                             :
          HEADQUARTER        :          BRANCH OFFICE
                             :
                +------+     :   Over WAN
           -----|Server|-----:--------------------------
           |    +------+     :     |         |         |
           |       |         :     |         |         |
        +------+   |         :     |         |         |
        |Client|   |         :     |         |         |
        +------+   |         :     |         |         |
                +------+     :     |         |         |
                |Client|     :     |         |         |
                +------+     :     |         |         |
                             :     |         |         |
                             :  +------+  +------+ +------+
                             :  |Client|  |Client| |Client|
                             :  +------+  +------+ +------+
                             :
                             :

In the above model, the data is separately sent/copied to each client in the remote office.
This means we are wasting the bandwidth thrice!! More subscribers in remote office means, more 
wastage of bandwidth.

.. note:: 

    ØMQ's model of scaling is based on so called devices, intermediary nodes that sit on the network and route the messages. 
                            
                            
Scaled up solution::

                             .
                             :
          HEADQUARTER        :          BRANCH OFFICE
                             :
                +------+     :   Over WAN
           -----|Server|-----:---------------
           |    +------+     :              |
           |       |         :         +----------+
        +------+   |         :         |0MQ Device|
        |Client|   |         :         +----------+
        +------+   |         :     ----------|----------
                +------+     :     |         |         |
                |Client|     :     | Over    |   Over  |
                +------+     :     | Lan     |   Lan   |
                             :     |         |         |
                             :  +------+  +------+ +------+
                             :  |Client|  |Client| |Client|
                             :  +------+  +------+ +------+
                             :
                             :
                             :
                             :
                            


Scenario #2
~~~~~~~~~~~~~~~~~~~~~~~~~

Consider a Video broadcast service that is being used by users located across the continent, connected to different ISP.

In this scenario exactly the same data are transferred in thousands of copies over the inter-continental link.

Video broadcast service scenario::

                    +-------------------+
                    |      Server       |
                    +-------------------+
        Service providers lan |        |
        ...................................
        Inter-Continental link|        |
        ...................................
        Local ISP      |      |        |
        ...................................
                       |      |        |
        Service users  |      |        |
        LAN            |      |        |
                       |      |        |
                    +------+ +------+ +------+
                    |Client| |Client| |Client|
                    +------+ +------+ +------+
                    
    
To improve this scenario, a local ISP could do something like this, independently of the content provider::

                    +-------------------+
                    |      Server       |
                    +-------------------+
        Service providers lan     |
        ..........................|........
        Inter-Continental link    |
        ..........................|........
        Local ISP           +----------+
                            |0MQ Device|
        ................... +----------+...
        Service users  ------|   |     |--
        LAN            |         |       |
                       |         |       |
                    +------+ +------+ +------+
                    |Client| |Client| |Client|
                    +------+ +------+ +------+
                    
In the latter case, however, the change was done independently of both the content provider and the users. 
To put it simply, network topology of the service is out of control of the content provider. 
No single entity can control the service in its entirety. 
Instead, topology is managed in a collaborative manner by all participants.


Content is distributed efficiently, but opaquely to the publisher. 
Content provider is not even able to tell how many subscribers there are. 


Scenario #3
~~~~~~~~~~~~~~~~~~~~~~


A simple request/reply architecture::

              |     +-------------------+    |
              |     |      Server       |    |
              |     +-------------------+    |
              |      |         |       |  Request
              |      |         |       |     |
              |Reply |         |       |     |
              |   +------+ +------+ +------+ |
              |   |Client| |Client| |Client| |
                  +------+ +------+ +------+ |
                  

Interjecting devices between the endpoints in a request/reply pattern::


              |    +------+    +------+      |
              |    |server|    |server|      |
              |    +------+    +------+      |
              |          |       |        Request
              |         +----------+         |
              |         |0MQ Device|         |
              |         +----------+         |
              |              |               |
              |      -------------------     |
              |Reply |         |       |     |
              |   +------+ +------+ +------+ |
              |   |Client| |Client| |Client| |
              |   +------+ +------+ +------+ |
              

This is the famous Enterprise Service Bus architecture! 
The node in the middle (called simply "bus") provides three important features:

* There can be more than a single server which can allow scaling of servers
* The clients don't have to be aware of servers' location. They speak to the bus which in turn dispatches the messages to the servers.
* The servers can come and go, depending on need, without disrupting the clients.

However, an Enterprise Service Bus is almost by definition centralized. 





                  


                    
               