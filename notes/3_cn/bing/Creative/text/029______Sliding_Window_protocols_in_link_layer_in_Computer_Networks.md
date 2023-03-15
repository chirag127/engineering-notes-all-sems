#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames  .
- Using the sliding window protocol, the sender can send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window is also used in Transmission Control Protocol (TCP), which operates at the transport layer  .
- The sliding window protocol manages the flow of data between two network nodes to ensure that the receiver can handle the incoming data and that the sender does not overwhelm the network  .
- The sliding window protocol uses two types of windows: a send window and a receive window  .
- The send window is the set of frames that the sender can transmit without waiting for an acknowledgment  .
- The receive window is the set of frames that the receiver can accept without sending an acknowledgment  .
- The size of the send window and the receive window can vary depending on the network conditions and the protocol parameters  .
- The sliding window protocol can be classified into two types: stop-and-wait and go-back-N  .
- In stop-and-wait, the sender sends one frame at a time and waits for an acknowledgment before sending the next frame  .
- In go-back-N, the sender can send up to N frames at a time without waiting for an acknowledgment, where N is the size of the send window  .
- The receiver sends an acknowledgment for the last frame it received in order, and the sender retransmits all the frames from that point onwards in case of a lost or corrupted frame  .
- The sliding window protocol improves the efficiency and reliability of data transmission over a network   .