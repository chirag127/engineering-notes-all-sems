### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol in which the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving a frame and checking it for errors.

The steps involved in the implementation of Stop and Wait Protocol are as follows:

1. The sender sends a frame to the receiver.
2. The receiver checks the frame for errors.
3. If the frame is error-free, the receiver sends an acknowledgment to the sender.
4. If the frame contains errors, the receiver discards the frame and does not send an acknowledgment.
5. The sender waits for an acknowledgment from the receiver before sending the next frame.
6. If the sender does not receive an acknowledgment within a specified time, it assumes that the frame was lost or corrupted and retransmits the frame.
7. This process continues until all frames have been transmitted and acknowledged.

This protocol is simple to implement but has a low efficiency due to the time spent waiting for acknowledgments. It is suitable for use in low error rate and low data rate communication channels.