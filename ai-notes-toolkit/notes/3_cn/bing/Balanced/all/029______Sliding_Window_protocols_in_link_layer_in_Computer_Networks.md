#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames  .
- Using the sliding window protocol, the sender can send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window is also used in Transmission Control Protocol (TCP), which operates at the transport layer  .
- The sliding window protocol manages the flow of data between two network nodes to ensure that the receiver can handle the incoming data and that the sender does not overwhelm the network  .
- The sliding window protocol uses two types of windows: a sender window and a receiver window  .
- The sender window is the set of frames that the sender can send without waiting for an acknowledgment  .
- The receiver window is the set of frames that the receiver can accept without sending an acknowledgment  .
- The size of the windows can vary depending on the protocol and the network conditions  .
- The sender and the receiver use sequence numbers to identify and acknowledge the frames  .
- The sender and the receiver also use timers to detect and retransmit lost or corrupted frames  .
- There are two main variants of the sliding window protocol: stop-and-wait and go-back-N  .
- In stop-and-wait, the sender sends one frame at a time and waits for an acknowledgment before sending the next frame  .
- In go-back-N, the sender can send up to N frames at a time without waiting for an acknowledgment, where N is the size of the sender window  .
- The stop-and-wait protocol is simple but inefficient, as it wastes the network bandwidth and causes long delays  .
- The go-back-N protocol is more efficient but more complex, as it requires the sender to keep track of the frames in the window and retransmit them if they are lost or corrupted  .
- A mnemonic to remember the difference between stop-and-wait and go-back-N is: stop-and-wait is like a **single-lane** road, where only one car can pass at a time, and go-back-N is like a **multi-lane** road, where multiple cars can pass at a time.
- A diagram to illustrate the sliding window protocol is:

```
Sender                          Receiver
|                              |
|  Frame 0  |                  |
|---------->|                  |
|           |  Frame 0  |      |
|           |---------->|      |
|           |  ACK 0    |      |
|<----------|<----------|      |
|  Frame 1  |                  |
|---------->|                  |
|           |  Frame 1  |      |
|           |---------->|      |
|           |  ACK 1    |      |
|<----------|<----------|      |
|  Frame 2  |                  |
|---------->|                  |
|           |  Frame 2  |      |
|           |---------->|      |
|           |  ACK 2    |      |
|<----------|<----------|      |
|  Frame 3  |                  |
|---------->|                  |
|           |  Frame 3  |      |
|           |---------->|      |
|           |  ACK 3    |      |
|<----------|<----------|      |
|                              |
```

- Some advantages of the sliding window protocol are  :
  - It improves the network efficiency and throughput by allowing multiple frames to be sent at a time.
  - It ensures the reliable and sequential delivery of the data frames by using sequence numbers and acknowledgments.
  - It prevents the network congestion and buffer overflow by controlling the flow of data between the