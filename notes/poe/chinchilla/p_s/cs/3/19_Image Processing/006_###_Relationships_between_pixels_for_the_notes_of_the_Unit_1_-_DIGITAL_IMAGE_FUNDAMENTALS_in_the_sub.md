#### TCP Transport layer protocol

TCP (Transmission Control Protocol) is a connection-oriented, reliable, and stream-oriented protocol that operates in the transport layer of the OSI model. TCP is used for transmitting data over the internet and is responsible for ensuring that data is received correctly, in order, and without errors. 

Below are some of the key features of TCP:

- **Reliability:** TCP is a reliable protocol as it guarantees that the data packets are delivered to the destination in the correct order and without any errors. If a packet is lost during transmission, TCP will retransmit the packet until it is received by the destination.

- **Connection-oriented:** TCP establishes a connection between the sender and the receiver before transmitting data. This connection ensures that the data is transmitted in a sequential order and without any errors.

- **Flow control:** TCP uses flow control mechanisms to ensure that the sender does not overwhelm the receiver with data. The receiver sends back acknowledgments to the sender indicating the amount of data it can receive at a time.

- **Congestion control:** TCP uses congestion control mechanisms to prevent the network from becoming congested. This is achieved by adjusting the rate at which data is sent based on the network conditions.

- **Full-duplex communication:** TCP allows for full-duplex communication, which means that data can be transmitted in both directions simultaneously.

TCP uses a three-way handshake to establish a connection between the sender and the receiver. The three-way handshake involves the following steps:

1. The sender sends a SYN (synchronize) packet to the receiver.
2. The receiver sends a SYN-ACK (synchronize-acknowledgment) packet to the sender.
3. The sender sends an ACK (acknowledgment) packet to the receiver.

Once the connection is established, data can be transmitted between the sender and the receiver. TCP breaks the data into smaller segments and adds a header to each segment containing information such as the sequence number, acknowledgment number, and checksum.

TCP is used for a variety of applications such as web browsing, email, file transfer, and remote access. It is a reliable protocol that ensures that data is transmitted correctly and without errors. However, due to its connection-oriented nature, it is slower than UDP (User Datagram Protocol), which is a connectionless protocol.