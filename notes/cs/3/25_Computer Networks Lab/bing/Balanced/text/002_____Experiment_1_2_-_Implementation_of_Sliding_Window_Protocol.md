### Experiment 1.2 - Implementation of Sliding Window Protocol

- Sliding window protocol is a feature of packet-based data transmission protocols that ensures reliable and sequential delivery of data frames .
- The protocol uses a window size that determines how many frames can be sent by the sender before receiving an acknowledgment from the receiver .
- The window slides along the sequence of frames as the sender transmits and the receiver acknowledges them .
- The protocol requires the receiver to acknowledge the receipt of each data packet, and it allows the receiver to use a single acknowledgment (ACK) to confirm the delivery of multiple packets.
- The protocol also handles the cases of lost, corrupted, or duplicated frames by using timers, sequence numbers, and retransmission mechanisms .
- There are different variants of sliding window protocol, such as stop-and-wait, go-back-N, and selective repeat  .
- Stop-and-wait is the simplest sliding window protocol, where the sender sends one frame at a time and waits for an ACK before sending the next frame .
- Go-back-N is the sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for ACKs, but the receiver can only send a cumulative ACK for the last in-order frame received  .
- Selective repeat is the sliding window protocol where the sender can send multiple frames (up to the window size) without waiting for ACKs, and the receiver can send individual ACKs for each frame received, regardless of the order  .
- The implementation of sliding window protocol involves the following steps:
  - Define the window size, the sequence number range, and the frame structure for the sender and the receiver  .
  - Initialize the window and the sequence numbers for the sender and the receiver  .
  - Implement the logic for sending and receiving frames, including the acknowledgment, timer, and retransmission mechanisms  .
  - Simulate the cases of frame loss, corruption, or duplication and observe the behavior of the protocol  .
  - Compare the performance of different variants of sliding window protocol in terms of throughput, efficiency, and reliability  .