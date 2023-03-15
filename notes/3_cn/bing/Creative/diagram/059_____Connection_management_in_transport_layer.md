Connection management in transport layer is the process of establishing, maintaining and terminating a logical connection between two end hosts. The transport layer protocols, such as TCP and UDP, provide different types of connection management services. TCP is a connection-oriented protocol that uses a three-way handshake to establish a reliable and bidirectional connection between two end hosts. UDP is a connectionless protocol that does not use any handshake or connection state to send or receive datagrams between two end hosts.

A possible ASCII diagram for connection management in transport layer using TCP is:

```
Client                                  Server
  |                                       |
  |  SYN (seq=x)                          |
  |-------------------------------------->|
  |                                       | Passive open
  |                                       |
  |  SYN (seq=y) ACK (ack=x+1)            |
  |<--------------------------------------|
  |                                       | Active open
  |  ACK (ack=y+1)                        |
  |-------------------------------------->|
  |                                       |
  |  Connection established               |
  |<=====================================>|
  |                                       |
  |  Data (seq=x+1, len=n)                |
  |-------------------------------------->|
  |                                       |
  |  ACK (ack=x+n+1)                      |
  |<--------------------------------------|
  |                                       |
  |  Data (seq=y+1, len=m)                |
  |<--------------------------------------|
  |                                       |
  |  ACK (ack=y+m+1)                      |
  |-------------------------------------->|
  |                                       |
  |  Data transfer                        |
  |<=====================================>|
  |                                       |
  |  FIN (seq=x+n+1)                      |
  |-------------------------------------->|
  |                                       | Close
  |  ACK (ack=x+n+2)                      |
  |<--------------------------------------|
  |                                       |
  |  FIN (seq=y+m+1)                      |
  |<--------------------------------------|
  |                                       | Close
  |  ACK (ack=y+m+2)                      |
  |-------------------------------------->|
  |                                       |
  |  Connection terminated                |
  |<=====================================>|
  |                                       |
```