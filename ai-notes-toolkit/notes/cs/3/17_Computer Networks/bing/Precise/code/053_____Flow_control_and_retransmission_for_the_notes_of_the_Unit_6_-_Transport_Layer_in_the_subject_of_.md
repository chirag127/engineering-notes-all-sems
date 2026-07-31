### Flow control and retransmission for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

Flow control and retransmission are two important mechanisms used in the transport layer of computer networks to ensure reliable data transmission.

1. **Flow control** is the process of managing the rate of data transmission between two nodes to prevent a fast sender from overwhelming a slow receiver. This is achieved by using a sliding window protocol, where the receiver sends a window size to the sender, indicating how many packets it can receive at a time. The sender then sends packets within the window size and waits for an acknowledgment from the receiver before sending more packets.

2. **Retransmission** is the process of re-sending packets that have been lost or corrupted during transmission. This is achieved by using a timeout mechanism, where the sender sets a timer for each packet it sends. If the sender does not receive an acknowledgment for a packet within the timeout period, it assumes that the packet has been lost and retransmits it.

These two mechanisms work together to ensure that data is transmitted reliably and efficiently between two nodes in a computer network. They are essential for the proper functioning of the transport layer and are implemented in transport layer protocols such as TCP (Transmission Control Protocol).