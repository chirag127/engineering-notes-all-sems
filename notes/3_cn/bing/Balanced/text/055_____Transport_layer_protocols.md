### Transport layer protocols

- Transport layer protocols are responsible for providing end-to-end communication services for applications over a network.
- Transport layer protocols lie between the application layer and the network layer in the protocol stack, and they use the services of the lower layers to send and receive data packets.
- Transport layer protocols can be classified into two types: connection-oriented and connectionless.
- Connection-oriented protocols establish a logical connection between the sender and the receiver before exchanging data, and they ensure reliable and ordered delivery of data. An example of a connection-oriented protocol is the Transmission Control Protocol (TCP).
- Connectionless protocols do not require a prior connection between the sender and the receiver, and they do not guarantee reliable or ordered delivery of data. An example of a connectionless protocol is the User Datagram Protocol (UDP).
- Transport layer protocols also provide other functions, such as flow control, congestion control, error detection, and multiplexing.
- Flow control is the mechanism that regulates the amount of data that the sender can transmit to the receiver, based on the receiver's buffer capacity and processing speed.
- Congestion control is the mechanism that prevents the network from being overloaded with too many packets, by adjusting the sending rate of the sender according to the network conditions.
- Error detection is the mechanism that detects and corrects errors in the data packets, such as lost, duplicated, corrupted, or out-of-order packets.
- Multiplexing is the mechanism that allows multiple applications to share the same transport layer protocol and the same network connection, by using port numbers to identify different processes.