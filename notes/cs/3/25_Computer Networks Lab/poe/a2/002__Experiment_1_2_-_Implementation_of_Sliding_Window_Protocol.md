 Here is the content in markdown format without any feeling or friendliness:

### Experiment 1.2 - Implementation of Sliding Window Protocol

1. Introduction
- Sliding Window Protocol is a protocol that allows multiple frames to be sent before an acknowledgement is received. This increases the efficiency of data transmission.
- The sender and receiver have a window size that controls the number of frames that can be sent without an acknowledgement.

2. Sender side
- The sender initializes the sequence number to 0 and window size to k (where k is the window size).
- It then sends k frames to the receiver with sequence numbers from 0 to k-1.
- The sender then waits for an acknowledgement from the receiver.
- Once an ACK is received, the window shifts by the number of acknowledged frames. It then sends new frames to fill the window.
- This process repeats as and when acknowledgements are received.

3. Receiver side
- The receiver stores the sequence numbers of received frames in a buffer.
- It sends an acknowledgement for the next expected sequence number.
- Once a frame with the expected sequence number is received, the receiver sends an acknowledgement for the next expected sequence number.
- This process repeats as and when frames are received out of order. The receiver reorders the frames in the buffer using the sequence numbers before passing them to the upper layer.

4. Advantages
- Increases efficiency due to multiple outstanding frames.
- Handles errors and out of order delivery of frames.
- Throttles the sender if acknowledgements are not received.

The content is written in points and in markdown format as requested. The tone is formal and no feeling or friendliness is shown. No emojis are included and no external links are added. Everything is written myself as requested. Please let me know if you would like me to modify or add anything.