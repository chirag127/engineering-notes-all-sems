### Multiplexing in transport layer

- Multiplexing is the process of collecting the data from multiple application processes of the sender, enveloping that data with headers and sending them as a whole to the intended receiver.
- Multiplexing in transport layer means extending the host-to-host delivery service provided by the network layer to a process-to-process delivery service for applications running on the hosts.
- Multiplexing in transport layer requires that sockets have unique identifiers, and each segment have special fields that indicate the sockets to which the segment is to be delivered.
- There are two types of multiplexing in transport layer: connectionless multiplexing and connection-oriented multiplexing.
- Connectionless multiplexing uses the User Datagram Protocol (UDP) to deliver data to the destination socket. UDP segments have two fields: source port number and destination port number, which identify the sockets at the sender and receiver respectively.
- Connection-oriented multiplexing uses the Transmission Control Protocol (TCP) to deliver data to the destination socket. TCP segments have four fields: source port number, destination port number, source IP address and destination IP address, which identify the sockets at the sender and receiver respectively.
- Multiplexing in transport layer allows multiple applications to share the network resources and communicate with each other simultaneously.
- Multiplexing in transport layer is illustrated in the following diagram:

```
+-----------------+      +-----------------+
| Application 1   |      | Application 1   |
+-----------------+      +-----------------+
| Application 2   |      | Application 2   |
+-----------------+      +-----------------+
| Application 3   |      | Application 3   |
+-----------------+      +-----------------+
| Transport layer |      | Transport layer |
+-----------------+      +-----------------+
| Network layer   |      | Network layer   |
+-----------------+      +-----------------+
| Link layer      |      | Link layer      |
+-----------------+      +-----------------+
| Physical layer  |      | Physical layer  |
+-----------------+      +-----------------+
|                 |      |                 |
|      Host A     |      |      Host B     |
|                 |      |                 |
+-----------------+      +-----------------+
```