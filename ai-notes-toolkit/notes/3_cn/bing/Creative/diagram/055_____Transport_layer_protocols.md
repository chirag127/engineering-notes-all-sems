Transport layer protocols are protocols that lie between user applications and the network. They provide end-to-end communication services for applications, such as reliable data transfer, flow control, congestion control, and multiplexing. The most common transport layer protocols in the Internet are Transmission Control Protocol (TCP) and User Datagram Protocol (UDP). TCP is a connection-oriented protocol that guarantees reliable and ordered delivery of data, while UDP is a connectionless protocol that does not provide any reliability or ordering guarantees, but has lower overhead and latency. Other transport layer protocols that have been defined and implemented include the Datagram Congestion Control Protocol (DCCP) and the Stream Control Transmission Protocol (SCTP).

A possible ASCII diagram for transport layer protocols is shown below:

### Transport layer protocols

```
+-----------------+-----------------+-----------------+
| Application     | Application     | Application     |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      TCP        |      UDP        |      DCCP       |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      IP         |      IP         |      IP         |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
| Data link layer | Data link layer | Data link layer |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
| Physical layer  | Physical layer  | Physical layer  |
+-----------------+-----------------+-----------------+
```