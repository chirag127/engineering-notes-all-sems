 Here is the content in markdown format for the given topic:

## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

**Stop and Wait Protocol:**

- It is a simple flow control protocol.
- The sender sends one frame and waits for an acknowledgement (ACK) from the receiver before sending the next frame.
- If ACK is not received within a timeout period, the frame is retransmitted.
- Advantage: Simple to implement.
- Disadvantage: Low throughput as sender is idle waiting for ACK most of the time.

**Sliding Window Protocol:**

- It is a flow and error control technique that allows multiple frames to be transmitted before an ACK is received.
- The sender maintains a window of size `w` which is the number of frames that can be sent without an ACK.
- Once the window is full, the sender waits for an ACK. The window then slides to allow next `w` frames to be sent.
- This ensures high throughput as sender is not idle most of the time waiting for ACK.
- However, it requires buffering of frames at the sender and receiver and more complex logic to handle ACKs and timeouts.

**Examples and Applications:** FTP, TCP are some examples that use sliding window protocol. It is useful in network conditions with high latency or bandwidth-delay product as it provides higher throughput than stop and wait protocol.

[Detailed diagrams and codes can be included here to illustrate the concepts]

[Other points on advantages, disadvantages and applications can be added as required.]