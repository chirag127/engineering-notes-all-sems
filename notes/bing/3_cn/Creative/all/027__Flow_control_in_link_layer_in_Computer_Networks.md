#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver .
- It makes the sender wait until an acknowledgment is received from the receiver's end .
- Methods of flow control are stop-and-wait, and sliding window .

##### Stop-and-wait

- In this method, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment after receiving and processing the frame.
- The sender can send the next frame only after receiving the acknowledgment.
- This method is simple but inefficient, as the sender has to wait for a round-trip time (RTT) between each frame.
- The utilization of the channel is low, as the channel is idle during the waiting time.

##### Sliding window

- In this method, the sender can send multiple frames without waiting for acknowledgments, as long as the number of frames does not exceed a predefined window size.
- The receiver sends an acknowledgment for each frame, indicating the next expected frame.
- The sender slides the window forward as it receives acknowledgments, and can send new frames that fall within the window.
- This method is more efficient and utilizes the channel better, as the sender does not have to wait for a RTT between each frame.
- The window size can be adjusted dynamically based on the network conditions and the receiver's buffer capacity.

##### Mnemonics and learning tricks

- To remember the difference between stop-and-wait and sliding window, you can use the following mnemonics:
  - Stop-and-wait: SAW (Slow And Wasteful)
  - Sliding window: SW (Swift and Wise)
- To remember the formula for the utilization of the channel in stop-and-wait, you can use the following trick:
  - Utilization = 1 / (1 + 2a), where a = RTT / transmission time
  - Think of a as the ratio of the waiting time to the sending time
  - The higher the a, the lower the utilization
  - The lower the a, the higher the utilization
  - When a = 0, the utilization is 1 (maximum)
  - When a = infinity, the utilization is 0 (minimum)