### Window management in transport layer

- Window management is a technique used by the transport layer to control the flow of data between two end systems.
- Window management ensures that the sender does not overwhelm the receiver or the network with too many packets at once, and that the receiver can acknowledge the received packets in a timely manner.
- Window management also helps to improve the efficiency and reliability of data transmission by detecting and recovering from packet losses, errors, or delays.
- Window management involves two main concepts: sliding window and flow control.

#### Sliding window

- A sliding window is a mechanism that allows the sender and the receiver to keep track of the sequence numbers of the packets that are sent and received.
- A sliding window is a variable-sized subset of the sequence number space, which represents the range of packets that can be sent or received at any given time.
- The sender maintains a send window, which indicates the range of sequence numbers that it can send without waiting for an acknowledgment from the receiver.
- The receiver maintains a receive window, which indicates the range of sequence numbers that it can receive and acknowledge without buffering or discarding any packets.
- The size and position of the sliding window can change dynamically based on the feedback from the receiver and the network conditions.
- The sender and the receiver use the sliding window to implement two types of protocols: stop-and-wait and go-back-N.

##### Stop-and-wait

- Stop-and-wait is a simple sliding window protocol that uses a window size of one.
- The sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The receiver sends an acknowledgment for each packet it receives and discards any duplicate packets.
- The sender and the receiver use a single bit to distinguish between two consecutive packets with the same sequence number (0 or 1).
- Stop-and-wait is easy to implement but has low efficiency and throughput, as the sender has to wait for a round-trip time (RTT) between each packet transmission.

##### Go-back-N

- Go-back-N is a sliding window protocol that uses a window size of N, where N is greater than one.
- The sender can send up to N packets without waiting for an acknowledgment from the receiver, as long as they are within the send window.
- The receiver sends a cumulative acknowledgment for the highest sequence number that it has received in order, and buffers any out-of-order packets that are within the receive window.
- The sender uses a timer for each packet it sends, and retransmits all the packets from the oldest unacknowledged packet if the timer expires or a negative acknowledgment (NAK) is received from the receiver.
- Go-back-N has higher efficiency and throughput than stop-and-wait, as the sender can utilize the network bandwidth more effectively, but it also has higher overhead and complexity, as it requires more buffering and retransmission.

#### Flow control

- Flow control is a technique that allows the receiver to regulate the amount of data that the sender can send, based on the available buffer space at the receiver.
- Flow control prevents the receiver from being overwhelmed by the sender, which can cause packet losses or congestion at the receiver.
- Flow control can be implemented by using either feedback-based or rate-based mechanisms.

##### Feedback-based flow control

- Feedback-based flow control uses the feedback from the receiver to adjust the size of the send window at the sender.
- The receiver informs the sender of the amount of buffer space that it has available, which determines the maximum number of packets that the sender can send without causing overflow at the receiver.
- The receiver can use either explicit or implicit feedback to communicate with the sender.

###### Explicit feedback

- Explicit feedback is a method that uses a separate field in the acknowledgment packet to indicate the size of the receive window at the receiver.
- The sender uses this information to update the size of the send window accordingly.
- Explicit feedback is also known as advertised window or credit-based flow control.

###### Implicit feedback

- Implicit feedback is a method that uses the acknowledgment number in the acknowledgment packet to indicate the size of the receive window at the receiver.
- The sender calculates the size of the send window by subtracting the acknowledgment number from the last sequence number that it has sent.
- Implicit feedback is also known as sliding window flow control.

##### Rate-based flow control

- Rate-based flow control uses a predetermined rate or quota to limit the amount of data that the sender can send to the receiver.
- The sender and the receiver agree on a rate or quota before the data transmission begins, and the sender adheres to this rate or quota throughout the transmission.
- The sender and the receiver can use either fixed or variable rate or quota to implement rate-based flow control.

###### Fixed rate or quota

- Fixed rate or quota is a