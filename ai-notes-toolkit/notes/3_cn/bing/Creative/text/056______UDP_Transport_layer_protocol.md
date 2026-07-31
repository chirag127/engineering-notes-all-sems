#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a transport layer protocol that is part of the Internet Protocol suite, also known as UDP/IP suite .
- UDP is a simple, unreliable and connectionless protocol. It does not establish a connection before sending data, nor does it guarantee the delivery, order or integrity of the data  .
- UDP has a 16-byte header that contains the source and destination port numbers, the length of the data and a checksum for error detection . The header is shown below:

| Source Port | Destination Port |
|:-----------:|:----------------:|
|  16 bits    |     16 bits      |

| Length      | Checksum         |
|:-----------:|:----------------:|
|  16 bits    |     16 bits      |

- UDP is suitable for applications that require fast, low-overhead and real-time data transmission, such as voice and video streaming, online gaming, DNS queries and SNMP  .
- UDP is also used by some transport layer protocols that provide additional features, such as Datagram Congestion Control Protocol (DCCP) and Stream Control Transmission Protocol (SCTP).