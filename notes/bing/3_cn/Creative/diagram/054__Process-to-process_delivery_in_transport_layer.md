The transport layer is responsible for process-to-process delivery, which means the delivery of a packet, part of a message, from one process to another. A process is an entity of the application layer that uses the services of the transport layer. Two processes can communicate using the client/server paradigm, where one process acts as a client and requests services from another process that acts as a server.

The transport layer uses two protocols to perform process-to-process delivery: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol). TCP is a connection-oriented protocol that provides reliable, ordered, and error-free delivery of data. UDP is a connectionless protocol that provides unreliable, unordered, and error-free delivery of data.

The transport layer uses port numbers to identify the processes on the source and destination hosts. A port number is a 16-bit integer that is added to the header of the transport layer segment. The source port number identifies the process that sends the data, and the destination port number identifies the process that receives the data.

The following diagram illustrates the process-to-process delivery in the transport layer using ASCII art:

```
+-----------------+       +-----------------+
| Application     |       | Application     |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Transport       |       | Transport       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Network         |       | Network         |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Host A     |       |      Host B     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Node X     |       |      Node Y     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Node Z     |       |      Node W     |
|                 |       |                 |
+-----------------+       +-----------------+
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
         |                         |
+-----------------+       +-----------------+
| Data Link       |       | Data Link       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Physical        |       | Physical        |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
|                 |       |                 |
|      Host C     |       |      Host D     |
|                 |       |                 |
+-----------------+       +-----------------+
| Application     |       | Application     |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Transport       |       | Transport       |
| Layer           |       | Layer           |
+-----------------+       +-----------------+
| Network         |       | Network         |
| Layer           |       | Layer