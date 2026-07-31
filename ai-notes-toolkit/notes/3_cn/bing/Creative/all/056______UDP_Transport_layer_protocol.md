#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a transport layer protocol that is part of the Internet Protocol suite, also known as UDP/IP suite .
- UDP is a simple, unreliable and connectionless protocol. It does not establish a connection before sending data, nor does it guarantee that the data will be delivered or received in order or without errors  .
- UDP adds a 16-byte header to the data from the upper layer. The header contains four fields: source port, destination port, length and checksum. The source and destination ports identify the endpoints of the communication. The length field specifies the total length of the UDP datagram, including the header and the data. The checksum field provides a basic error detection mechanism by verifying the integrity of the header and the data  .

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

- UDP is suitable for applications that require speed, simplicity or low overhead, such as real-time audio or video streaming, online gaming, DNS queries, etc. UDP is also used for multicasting and broadcasting, where a single sender can transmit data to multiple receivers  .
- UDP has some disadvantages, such as lack of reliability, congestion control, flow control, error recovery, etc. UDP applications have to implement these features themselves if needed. UDP also has a limited payload size of 65,507 bytes, which is the maximum length of the UDP datagram minus the header size .
- A mnemonic to remember the four fields of the UDP header is: **S**ource **P**ort, **D**estination **P**ort, **L**ength, **C**hecksum, or **SPDLC**. Another mnemonic is: **S**end **P**ackets **D**irectly **L**ike **C**razy, or **SPDLC**.