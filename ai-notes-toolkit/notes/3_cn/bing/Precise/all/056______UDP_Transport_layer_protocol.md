#### UDP Transport layer protocol
- UDP stands for User Datagram Protocol.
- It is a transport layer protocol used for transmitting data over the internet.
- UDP is a connectionless protocol, meaning it does not establish a connection before transmitting data.
- It is a simple protocol that does not provide error checking or flow control.
- UDP is faster than TCP because it does not have the overhead of error checking and flow control.
- UDP is used for applications that require fast transmission of data, such as online gaming, voice over IP, and video streaming.
- A mnemonic to remember the characteristics of UDP is "Unreliable, Datagram, Protocol".
- UDP packets are called datagrams.
- Each datagram contains a header and a payload.
- The header contains information such as the source and destination port numbers, the length of the datagram, and a checksum.
- The payload contains the data being transmitted.
- UDP is not suitable for applications that require reliable transmission of data, such as file transfers.
- Advantages of UDP:
  - Faster transmission of data
  - Lower overhead
  - Suitable for real-time applications
- Disadvantages of UDP:
  - No error checking
  - No flow control
  - Not suitable for reliable transmission of data
- Example applications that use UDP:
  - Online gaming
  - Voice over IP
  - Video streaming
  - DNS queries
- ASCII diagram of a UDP datagram:
```
  0      7 8     15 16    23 24    31  
  +--------+--------+--------+--------+ 
  | Source | Destin | Length | Checksum| 
  |  Port  |  ation |        |         | 
  |        |   Port |        |         | 
  +--------+--------+--------+--------+ 
  |                                       | 
  |          Payload Data                 | 
  |                                       | 
  +---------------------------------------+ 
```