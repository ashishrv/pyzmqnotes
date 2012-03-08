

Learning ØMQ with pyzmq
=====================================

ØMQ is a neat messaging library that allows you that allows you to build your own messaging infrastructure.
ØMQ does not provide out of box messaging system experience like ActiveMQ or RabbitMQ.
It is higher level concept than sockets and provides as low level conceptual framework as possible to build messaging systems.
It can help build framework that scales where services could be handled by different applications that does one job well.

.. sidebar:: Disclaimer

    These are my notes based on reading the excellent articles on web, ØMQ guide and pyzmq documentation and trying out examples.
    This is still work in progress. 
    
    For feedback and issues, please send a mail to "ashish.vid" at gmail dot com.


Distributed applications are also easier to change compared to a monolithic applications.
It's expensive to try to define the behavior of each of many software applications that work together in a large network. 
It's much cheaper, and more flexible, to define the interfaces between them: the APIs. Messaging is an API that can be stretched across a network.

`pyzmq <https://github.com/zeromq/pyzmq>`_ provides python bindings for ØMQ and allows you to leverage ØMQ in python applications.
I have been using `pyzmq-static <https://bitbucket.org/brandon/pyzmq-static>`_ with virtualenv as it neatly provides isolated sandbox for my learning.

This tutorial is my journey into ØMQ programming with python. Hopefully, it will help you too. 

Code is present as folders inside each of the chapters. You can obtain them through `Github <https://github.com/ashishrv/pyzmqnotes>`_. 



.. toctree::
   :maxdepth: 3
   
   ØMQ and pyzmq         <pyzmq/pyzmq.rst>
   Various references    <references/links.rst>
   Competing products    <references/products.rst>
   

.. heartbeat, credit-based flow control, reliable pipelines, presence
.. & discovery using UDP, bridging (like VTX), file transfer, security,
.. and serialization.


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

