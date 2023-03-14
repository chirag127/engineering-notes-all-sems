#### Sliding Window protocols in link layer in Computer Networks

- Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames.
- The sliding window is also used in Transmission Control Protocol (TCP) which operates at the transport layer.
- The sliding window technique controls and optimizes the packet flow between a sender and a receiver, while ensuring a balanced approach to packet delivery.
- The sender and the receiver maintain a buffer to manage the flow of data packets. The buffer size is called the window size.
- Each data packet is numbered sequentially so that the sender and the receiver can track the delivery and acknowledgment of the packets.
- The receiver sends back an acknowledgment (ACK) to the sender for each data packet or a group of data packets that it receives.
- The sender cannot send more data packets than the amount of space available in the receiver's buffer.
- There are two types of sliding window protocols: Go-Back-N ARQ and Selective Repeat ARQ.
- Go-Back-N ARQ protocol sends multiple frames at a time and retransmits all the frames after a corrupted or lost frame. The receiver window size is always 1 and the sender window size is N.
- Selective Repeat ARQ protocol sends multiple frames at a time and retransmits only the corrupted or lost frames. The receiver window size is equal to the sender window size and is greater than 1.
- Selective Repeat ARQ protocol is more complex and efficient than Go-Back-N ARQ protocol.