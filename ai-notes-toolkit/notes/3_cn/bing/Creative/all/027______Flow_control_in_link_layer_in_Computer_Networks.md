#### Flow control in link layer in computer networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send before receiving an acknowledgment from the receiver .
- It prevents the sender from overwhelming the receiver with too many frames or data.
- There are two main methods of flow control in the link layer: stop-and-wait and sliding window.

##### Stop-and-wait flow control

- In this method, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- The receiver sends an acknowledgment after processing the received frame and getting ready to receive the next one.
- The sender and the receiver use a single bit to indicate the sequence number of the frame (0 or 1).
- This method is simple but inefficient, as the sender has to wait for a round-trip time (RTT) between sending a frame and receiving an acknowledgment.
- The utilization of the channel is low, as the channel is idle during the waiting time.

##### Sliding window flow control

- In this method, the sender can send multiple frames without waiting for acknowledgments, as long as the number of unacknowledged frames does not exceed a predefined window size.
- The receiver sends an acknowledgment for each frame, indicating the sequence number of the next expected frame.
- The sender and the receiver use a counter to keep track of the sequence number of the frames, which can range from 0 to 2^n-1, where n is the number of bits used for the sequence number.
- This method is more efficient than stop-and-wait, as the sender can utilize the channel more effectively by sending multiple frames in a burst.
- The utilization of the channel depends on the window size and the RTT.

##### Advantages and disadvantages of flow control in link layer

- Flow control in link layer can prevent data loss and ensure reliable transmission between two stations.
- Flow control in link layer can adapt to the varying speeds and capacities of the sender and the receiver.
- Flow control in link layer can also reduce the congestion and delay in the network.
- However, flow control in link layer can also introduce overhead and complexity in the frame format and the processing of the frames.
- Flow control in link layer can also reduce the throughput and efficiency of the transmission, especially if the window size is too small or the RTT is too large.

##### Mnemonics and learning tricks for flow control in link layer

- To remember the difference between stop-and-wait and sliding window, you can use the following mnemonics:
  - Stop-and-wait: One frame at a time, wait for ACK, single bit for sequence number, low utilization, simple but slow.
  - Sliding window: Multiple frames at a time, no wait for ACK, counter for sequence number, high utilization, complex but fast.
- To remember the formula for the utilization of the channel in stop-and-wait, you can use the following trick:
  - Utilization = 1 / (1 + 2a), where a = RTT / transmission time.
  - The numerator is 1 because the sender can send only one frame per RTT.
  - The denominator is 1 + 2a because the sender has to wait for 2a time units for the ACK to return.
  - The utilization is inversely proportional to the RTT, which means the longer the RTT, the lower the utilization.
- To remember the formula for the utilization of the channel in sliding window, you can use the following trick:
  - Utilization = W / (1 + 2a), where W = window size, a = RTT / transmission time.
  - The numerator is W because the sender can send up to W frames per RTT.
  - The denominator is 1 + 2a because the sender has to wait for 2a time units for the ACK to return.
  - The utilization is directly proportional to the window size and inversely proportional to the RTT, which means the larger the window size and the shorter the RTT, the higher the utilization.