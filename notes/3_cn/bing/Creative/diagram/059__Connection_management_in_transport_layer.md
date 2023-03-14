Connection management in transport layer is the process of establishing, maintaining and terminating a logical connection between two end hosts. The transport layer protocols, such as TCP and UDP, provide connection management services to the application layer. TCP is a connection-oriented protocol that uses a three-way handshake to establish a reliable and bidirectional connection between two hosts. UDP is a connectionless protocol that does not use any handshake mechanism to establish a connection, but simply sends datagrams to the destination host.

The following diagram illustrates the basic architecture of connection management in transport layer using TCP and UDP:

```
+----------------+     +----------------+     +----------------+
| Application    |     | Application    |     | Application    |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
| Transport      |     | Transport      |     | Transport      |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
| Network        |     | Network        |     | Network        |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
| Data Link      |     | Data Link      |     | Data Link      |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
| Physical       |     | Physical       |     | Physical       |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
      Host A                Router                Host B

TCP Connection Management:

Host A                                    Host B
  |                                         |
  | SYN(seq=x)                             |
  |---------------------------------------->|
  |                                         | SYN(seq=y)
  |                                         |<---------------------------------|
  |                                         |                                  |
  | SYN(seq=x+1), ACK(seq=y+1)             |                                  |
  |<----------------------------------------|                                  |
  |                                         |                                  |
  |                                         | ACK(seq=x+2)
  |                                         |--------------------------------->|
  |                                         |
  | Connection Established                  |
  |<--------------------------------------->|
  |                                         |
  | Data Transfer                          |
  |<--------------------------------------->|
  |                                         |
  | FIN(seq=z)                             |
  |---------------------------------------->|
  |                                         | FIN(seq=w)
  |                                         |<---------------------------------|
  |                                         |                                  |
  | ACK(seq=w+1)                           |                                  |
  |<----------------------------------------|                                  |
  |                                         |                                  |
  |                                         | ACK(seq=z+1)
  |                                         |--------------------------------->|
  |                                         |
  | Connection Terminated                  |
  |<--------------------------------------->|
  |                                         |

UDP Connection Management:

Host A                                    Host B
  |                                         |
  | Data Transfer                          |
  |<--------------------------------------->|
  |                                         |
```

: Connection management for the transport layer: service specification and protocol verification, S. Murphy and A. Shankar, IEEE Transactions on Communications, 1991.

: Transport Layer responsibilities, GeeksforGeeks, https://www.geeksforgeeks.org/transport-layer-responsibilities/