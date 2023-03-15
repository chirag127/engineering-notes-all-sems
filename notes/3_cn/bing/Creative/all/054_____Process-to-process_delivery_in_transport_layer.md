### Process-to-process delivery in transport layer

- The transport layer is responsible for delivering data from one process to another process on different hosts across a network .
- A process is an entity of the application layer that uses the services of the transport layer.
- The transport layer uses port numbers to identify and communicate with different processes on the same host .
- Port numbers are 16-bit integers that range from 0 to 65535.
- The transport layer can use two protocols to perform process-to-process delivery: TCP (Transmission Control Protocol) and UDP (User Datagram Protocol)  .
- TCP is a connection-oriented, reliable, and full-duplex protocol that provides flow control, congestion control, and error recovery  .
- UDP is a connectionless, unreliable, and simple protocol that does not provide any of these features  .
- TCP and UDP use different header formats to encapsulate the data from the application layer  .
- TCP header contains fields such as source port, destination port, sequence number, acknowledgment number, flags, window size, checksum, and urgent pointer  .
- UDP header contains only four fields: source port, destination port, length, and checksum  .
- The transport layer segments the data from the application layer and adds a header to each segment before passing it to the network layer  .
- The network layer encapsulates the segments into packets (or datagrams) and adds a header to each packet before passing it to the data link layer   .
- The data link layer encapsulates the packets into frames and adds a header and a trailer to each frame before passing it to the physical layer   .
- The physical layer converts the frames into bits and transmits them over the physical medium   .
- The reverse process happens at the receiver side, where the transport layer receives the segments from the network layer, checks the port numbers, and delivers the data to the corresponding process   .

Figure 1 shows an example of process-to-process delivery using TCP and UDP.

```
+-----------------+          +-----------------+
|  Application    |          |  Application    |
|     Layer       |          |     Layer       |
+-----------------+          +-----------------+
|  Transport      |          |  Transport      |
|     Layer       |          |     Layer       |
+-----------------+          +-----------------+
|  Network        |          |  Network        |
|     Layer       |          |     Layer       |
+-----------------+          +-----------------+
|  Data Link      |          |  Data Link      |
|     Layer       |          |     Layer       |
+-----------------+          +-----------------+
|  Physical       |          |  Physical       |
|     Layer       |          |     Layer       |
+-----------------+          +-----------------+
       Host A                      Host B

       Process 1                  Process 2
       Port 80                    Port 80
       TCP                        TCP
       Segment 1                  Segment 1
       Packet 1                   Packet 1
       Frame 1                    Frame 1
       Bit 1                      Bit 1

       Process 3                  Process 4
       Port 53                    Port 53
       UDP                        UDP
       Segment 2                  Segment 2
       Packet 2                   Packet 2
       Frame 2                    Frame 2
       Bit 2                      Bit 2
```
Figure 1: Process-to-process delivery using TCP and UDP

Some mnemonics and learning tricks for process-to-process delivery in transport layer are:

- Remember that port numbers are 16-bit integers by thinking of PORT as an acronym for Power Of 2 Times 16.
- Remember that TCP is connection-oriented, reliable, and full-duplex by thinking of TCP as an acronym for Trust