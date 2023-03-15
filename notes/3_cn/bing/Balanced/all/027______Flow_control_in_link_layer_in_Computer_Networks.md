#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send before receiving an acknowledgment from the receiver .
- It prevents the sender from overwhelming the receiver with too many frames or data.
- There are two main methods of flow control in the link layer: stop-and-wait and sliding window.

##### Stop-and-wait

- In this method, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The sender can only send one frame in each transmission round.
- The receiver sends an acknowledgment after receiving and processing each frame.
- The acknowledgment can be positive (ACK) or negative (NAK) depending on whether the frame was received correctly or not.
- If the sender receives a positive acknowledgment, it sends the next frame. If it receives a negative acknowledgment or no acknowledgment within a timeout period, it retransmits the same frame.
- The advantage of this method is that it is simple and reliable.
- The disadvantage of this method is that it is inefficient and slow, especially when the transmission delay is large compared to the processing time.

##### Sliding window

- In this method, the sender can send multiple frames in each transmission round without waiting for acknowledgments.
- The sender maintains a window of frames that it can send at any time. The size of the window is determined by the receiver's buffer capacity.
- The receiver also maintains a window of frames that it can receive at any time. The size of the window is determined by the sender's window size and the sequence numbers of the frames.
- The receiver sends an acknowledgment after receiving and processing each frame. The acknowledgment indicates the next expected frame and the current window size.
- The sender slides its window forward by the number of frames acknowledged by the receiver. The sender can send new frames that fall within the window.
- The receiver slides its window forward by the number of frames received correctly. The receiver can accept new frames that fall within the window.
- The advantage of this method is that it is efficient and fast, especially when the transmission delay is small compared to the processing time.
- The disadvantage of this method is that it is complex and requires more buffer space and sequence numbers.

##### Mnemonics and learning tricks

- To remember the difference between stop-and-wait and sliding window, you can use the following mnemonics:
  - Stop-and-wait: One frame at a time, wait for ACK or NAK, simple and slow.
  - Sliding window: Multiple frames at a time, slide the window, complex and fast.
- To remember the formula for the efficiency of stop-and-wait, you can use the following trick:
  - Efficiency = 1 / (1 + 2a), where a = transmission delay / processing time.
  - The numerator is 1 because the sender can only send one frame in each round.
  - The denominator is 1 + 2a because the sender has to wait for the round-trip time of the frame and the acknowledgment, which is twice the transmission delay, plus the processing time of the receiver.
  - The efficiency is inversely proportional to the transmission delay and directly proportional to the processing time.