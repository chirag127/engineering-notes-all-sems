#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful for the sequential and reliable delivery of data frames between two network nodes  .
- The sliding window protocol allows the sender to send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window protocol uses a window size to control the number of frames that can be sent or received at a time. The window size is the number of frames that fit in the buffer of the sender or the receiver  .
- The sliding window protocol has two variants: stop-and-wait and go-back-N  .
- In the stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The window size is one for both the sender and the receiver  .
- In the go-back-N protocol, the sender can send up to N frames at a time, where N is the window size of the sender. The receiver can only send cumulative acknowledgments for the frames it has received in order. If the receiver detects a missing or corrupted frame, it discards all the subsequent frames and sends a negative acknowledgment to the sender. The sender then retransmits all the frames from the last unacknowledged frame  .
- The sliding window protocol improves the efficiency and throughput of data transmission by reducing the idle time of the sender and the receiver  .
- The sliding window protocol also ensures that the receiver can handle the incoming data without being overwhelmed by the sender  .
- The sliding window protocol is also used in the transport layer by the Transmission Control Protocol (TCP), which manages the flow of packets between two computers or network hosts.