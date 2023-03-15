Connection management in transport layer is the process of establishing, maintaining, and terminating a logical connection between two service access points. The transport layer can use different protocols to provide connection management, such as TCP or UDP. TCP is a connection-oriented protocol that uses a three-way handshake to establish a reliable and bidirectional connection. UDP is a connectionless protocol that does not use any handshake or acknowledgment to send or receive datagrams.

A possible ASCII diagram for connection management in transport layer using TCP is:

### Connection management in transport layer

```
Client                      Server
  |                           |
  |  SYN (seq=x)              |
  |-------------------------->|
  |                           |
  |  SYN-ACK (seq=y, ack=x+1) |
  |<--------------------------|
  |                           |
  |  ACK (seq=x+1, ack=y+1)   |
  |-------------------------->|
  |                           |
  |  ESTABLISHED              |
  |<------------------------->|
  |                           |
  |  DATA (seq=x+2, ack=y+1)  |
  |-------------------------->|
  |                           |
  |  DATA (seq=y+1, ack=x+3)  |
  |<--------------------------|
  |                           |
  |  FIN (seq=x+3, ack=y+2)   |
  |-------------------------->|
  |                           |
  |  ACK (seq=y+2, ack=x+4)   |
  |<--------------------------|
  |                           |
  |  FIN (seq=y+2, ack=x+4)   |
  |<--------------------------|
  |                           |
  |  ACK (seq=x+4, ack=y+3)   |
  |-------------------------->|
  |                           |
  |  CLOSED                   |
  |<------------------------->|
  |                           |
```

A possible ASCII diagram for connection management in transport layer using UDP is:

### Connection management in transport layer

```
Client                      Server
  |                           |
  |  DATA (src_port=a,        |
  |  dest_port=b, data=d1)    |
  |-------------------------->|
  |                           |
  |  DATA (src_port=b,        |
  |  dest_port=a, data=d2)    |
  |<--------------------------|
  |                           |
  |  DATA (src_port=a,        |
  |  dest_port=b, data=d3)    |
  |-------------------------->|
  |                           |
  |  DATA (src_port=b,        |
  |  dest_port=a, data=d4)    |
  |<--------------------------|
  |                           |
```