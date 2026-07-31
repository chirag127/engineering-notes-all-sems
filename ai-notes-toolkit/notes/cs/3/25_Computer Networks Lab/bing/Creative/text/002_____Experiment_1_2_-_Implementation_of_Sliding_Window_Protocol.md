### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames  .
- Sliding window protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver  .
- Sliding window protocol can improve the efficiency of data transmission by sending more than one frame at a time with a larger sequence number, which is similar to pipelining in architecture.
- Sliding window protocol can handle errors and losses by using different techniques, such as stop-and-wait, go-back-N, and selective repeat   .
- Sliding window protocol can also be used in the Transmission Control Protocol (TCP) to control the flow and congestion of data packets .

The steps to implement the sliding window protocol are:

1. The sender and the receiver agree on the window size, which is the maximum number of frames that can be sent or received at a time.
2. The sender assigns a sequence number to each frame and sends them to the receiver within the window size.
3. The receiver sends an acknowledgment (ACK) to the sender for each frame it receives, indicating the next expected sequence number.
4. The sender slides the window forward by the number of frames that have been acknowledged by the receiver, and sends more frames if available.
5. The receiver slides the window forward by the number of frames that have been received and processed, and expects more frames from the sender.
6. If the sender does not receive an ACK from the receiver within a certain time, it assumes that the frame has been lost or corrupted, and retransmits the frame.
7. If the receiver receives a frame that is out of order or has an incorrect sequence number, it discards the frame and sends a negative acknowledgment (NAK) to the sender, indicating the expected sequence number.
8. The sender and the receiver repeat the steps until all the frames have been transmitted and received successfully.