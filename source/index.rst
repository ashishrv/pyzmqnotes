

Learning ØMQ with pyzmq
=====================================

Messaging connects applications running on a variety of platforms, and written in a variety of languages, across a network. 
It is one of the solution in decoupling and creating distributed applications. 
It helps in scaling where services could be handled by different applications that does one job well.

.. sidebar:: Disclaimer

    These are my notes based on reading the excellent articles on web, ØMQ guide and pyzmq documentation and trying out examples.
    This is still work in progress. 


Distributed applications are also easier to change compared to a monolithic applications.
It's expensive to try to define the behavior of each of many software applications that work together in a large network. 
It's much cheaper, and more flexible, to define the interfaces between them: the APIs. Messaging is an API that can be stretched across a network

ZeroMQ does not provide out of box messaging system experience like ActiveMQ or RabbitMQ. 
It is more of a messaging library that allows you to build your own messaging infrastructure. 
It is higher level concept than sockets and provides as lower level conceptual framework as possible to build messaging systems.


.. toctree::
   :maxdepth: 3
   
   ØMQ and pyzmq         <pyzmq/pyzmq.rst>
   Various references    <references/links.rst>
   Competing products    <references/products.rst>
   




* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

