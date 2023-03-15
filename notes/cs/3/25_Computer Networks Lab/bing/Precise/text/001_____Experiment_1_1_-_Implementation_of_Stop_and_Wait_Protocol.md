### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol that is used in data communication. It is a simple protocol that ensures reliable data transmission by sending one data frame at a time and waiting for an acknowledgment before sending the next frame. Here are the steps to implement the Stop and Wait Protocol:

1. The sender sends a data frame to the receiver.
2. The sender starts a timer and waits for an acknowledgment from the receiver.
3. The receiver receives the data frame and sends an acknowledgment back to the sender.
4. The sender receives the acknowledgment and stops the timer.
5. If the timer expires before the sender receives the acknowledgment, the sender retransmits the data frame.
6. The process repeats until all data frames have been transmitted and acknowledged.

This protocol is simple to implement but has some drawbacks. It can be inefficient in situations where the transmission time is much shorter than the round-trip time, as the sender has to wait for the acknowledgment before sending the next frame. Additionally, if the acknowledgment is lost, the sender will retransmit the data frame, even if the receiver has already received it. This can lead to duplicate data frames being received by the receiver.

Despite these drawbacks, the Stop and Wait Protocol is still widely used in data communication due to its simplicity and reliability. It is a good starting point for understanding flow control protocols in data communication.