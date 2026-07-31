### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames .
- Sliding window protocol uses a window size to control how many frames can be sent by the sender before receiving an acknowledgment from the receiver  .
- The window size can vary depending on the protocol and the network conditions .
- The sender maintains a send window that indicates the range of sequence numbers of frames that it can send .
- The receiver maintains a receive window that indicates the range of sequence numbers of frames that it can accept .
- The sender and the receiver exchange window information using control frames such as ACK, NAK, or SREJ .
- There are two main types of sliding window protocols: Go-Back-N ARQ and Selective Repeat ARQ .
- Go-Back-N ARQ allows the sender to send multiple frames without waiting for acknowledgments, but the receiver can only send a cumulative acknowledgment for the last correctly received frame  .
- If the sender does not receive an acknowledgment within a timeout period, it retransmits all the frames in its window, assuming that they are lost or corrupted  .
- Selective Repeat ARQ allows the sender to send multiple frames without waiting for acknowledgments, and the receiver can send individual acknowledgments for each correctly received frame  .
- If the sender does not receive an acknowledgment for a specific frame within a timeout period, it only retransmits that frame, assuming that the other frames are received correctly  .
- Selective Repeat ARQ can achieve higher efficiency and throughput than Go-Back-N ARQ, but it requires more buffer space and complexity at the sender and the receiver  .