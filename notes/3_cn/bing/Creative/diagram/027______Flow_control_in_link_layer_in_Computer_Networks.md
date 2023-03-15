#### Flow control in link layer in Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- It regulates the amount of data that a sender can send before receiving an acknowledgment from the receiver .
- It prevents the sender from overwhelming the receiver with too many frames or data units.
- It can be implemented at the data link layer using two methods: stop-and-wait and sliding window .
- Stop-and-wait flow control:
  - The sender sends one frame and waits for an acknowledgment from the receiver before sending the next frame.
  - The receiver sends an acknowledgment after receiving and processing each frame.
  - The sender and the receiver use a single bit to indicate the sequence number of the frame (0 or 1).
  - This method is simple but inefficient, as the sender has to wait for a round-trip time before sending the next frame.
- Sliding window flow control:
  - The sender can send multiple frames without waiting for acknowledgments, up to a certain window size .
  - The receiver sends an acknowledgment after receiving a frame, indicating the next expected frame .
  - The sender and the receiver use multiple bits to indicate the sequence number of the frame, allowing more frames to be sent in a window .
  - This method is more efficient and utilizes the channel capacity better than stop-and-wait .
- Flow control can also be implemented at the Ethernet level using pause frames.
  - Pause frames are special frames that are sent by the receiver to the sender, requesting the sender to stop sending data for a specified period of time.
  - Pause frames are defined by the IEEE standard 802.3x.
  - This method is useful for preventing buffer overflow and congestion at the receiver.