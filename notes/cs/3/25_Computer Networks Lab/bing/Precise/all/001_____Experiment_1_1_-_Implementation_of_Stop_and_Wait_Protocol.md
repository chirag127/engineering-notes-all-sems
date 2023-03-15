### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol in which the sender sends a single frame at a time and waits for an acknowledgment from the receiver before sending the next frame. This protocol is used to ensure reliable data transmission over an unreliable communication channel.

The steps involved in the implementation of the Stop and Wait Protocol are as follows:

1. The sender sends a single frame to the receiver.
2. The receiver receives the frame and sends an acknowledgment back to the sender.
3. The sender waits for the acknowledgment from the receiver before sending the next frame.
4. If the acknowledgment is not received within a specified time period, the sender retransmits the frame.
5. This process is repeated until all the frames are transmitted and acknowledged.

The Stop and Wait Protocol is simple to implement but has a low efficiency due to the time spent waiting for acknowledgments. It is suitable for use in scenarios where the communication channel has a low error rate and the data transmission rate is not a critical factor.