#### UDP Transport layer protocol

UDP is a simple, connectionless and unreliable transport layer protocol that is part of the Internet Protocol suite. It does not provide any guarantees for message delivery, ordering or duplicate protection. It only provides checksums for data integrity and port numbers for addressing different functions at the source and destination of the datagram. UDP is suitable for applications that require low-latency, high-performance and loss-tolerating connections, such as real-time voice or video communication, gaming, live streaming, etc. UDP was designed by David P. Reed in 1980 and formally defined in RFC 768.

The following diagram illustrates the basic structure of a UDP datagram, which consists of an 8-byte header and a variable-length data section. The header contains four fields: source port, destination port, length and checksum. The source and destination port fields identify the endpoints of the communication, the length field specifies the total size of the datagram, and the checksum field provides a way to verify the integrity of the header and data.

```
  0      7 8     15 16    23 24    31  
 +--------+--------+--------+--------+ 
 |     Source      |   Destination   | 
 |      Port       |      Port       | 
 +--------+--------+--------+--------+ 
 |                 |                 | 
 |     Length      |    Checksum     | 
 +--------+--------+--------+--------+ 
 |                                     
 |          data octets ...            
 +---------------- ...                 
```