## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Stop and Wait Protocol
- Stop and Wait Protocol is a flow control protocol.
- It is used in data communication to prevent the sender from overwhelming the receiver with data.
- In this protocol, the sender sends a single data frame and waits for an acknowledgment from the receiver before sending the next frame.
- If the acknowledgment is not received within a specified time, the sender retransmits the frame.
- This protocol is simple to implement but has low efficiency due to the time spent waiting for acknowledgments.

### Sliding Window Protocol
- Sliding Window Protocol is another flow control protocol.
- It is an improvement over the Stop and Wait Protocol as it allows the sender to transmit multiple frames before waiting for an acknowledgment.
- The sender maintains a window of frames that can be sent without waiting for an acknowledgment.
- The receiver also maintains a window of frames that it can receive.
- As the receiver acknowledges the receipt of frames, the sender's window slides forward, allowing the transmission of more frames.
- This protocol is more efficient than the Stop and Wait Protocol as it reduces the time spent waiting for acknowledgments.