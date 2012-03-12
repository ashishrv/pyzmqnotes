

Learning ØMQ with pyzmq
=====================================

ØMQ is a neat messaging library that allows you that allows you to build your own messaging infrastructure.
ØMQ does not provide out of box messaging system experience like ActiveMQ or RabbitMQ.
It is higher level concept than sockets and provides as low level conceptual framework as possible to build messaging systems.
It can help build framework that scales where services could be handled by different applications that does one job well.

.. sidebar:: Note

    These are my notes based on reading the excellent articles on web, ØMQ guide and pyzmq documentation and trying out examples.
    This is still a work in progress.     


Distributed applications are also easier to change compared to a monolithic applications.
It's expensive to try to define the behavior of each of many software applications that work together in a large network. 
It's much cheaper, and more flexible, to define the interfaces between them: the APIs. Messaging is an API that can be stretched across a network.

`pyzmq <https://github.com/zeromq/pyzmq>`_ provides python bindings for ØMQ and allows you to leverage ØMQ in python applications.
I have been using `pyzmq-static <https://bitbucket.org/brandon/pyzmq-static>`_ with virtualenv as it neatly provides isolated sandbox for my learning.

This tutorial is my journey into ØMQ programming with python. Hopefully, it will help you too. 





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

Code
-----------

Code is present as folders inside each of the chapters. 
You can obtain them through `github pyzmqnotes project <https://github.com/ashishrv/pyzmqnotes>`_. 

Acknowledgements
--------------------

Learning and experimenting with `ØMQ <http://www.zeromq.org/>`_ through python adaptor `pyzmq <https://github.com/zeromq/pyzmq>`_ has been a very exciting experience.
Thanks to all those who have contributed to it. Many folks have written articles and blogged on ØMQ. 
I wouldn't have stumbled on this great tool without that. 
I have tried to mention some of the excellent articles that I happened to read on this subject in the reference section.

I always begrudged writing documents till `Sphinx <http://sphinx.pocoo.org>`_ came along. 
It is quite exciting to be able to share my notes through `readthedocs <http://readthedocs.org/>`_.
Of course, all these has been made very easy through `github <https://github.com/>`_.

Contact
-----------------

Do send your suggestions/corrections for improvement at "ashish.vid" at gmail dot com (Ashish Vidyarthi).
 

