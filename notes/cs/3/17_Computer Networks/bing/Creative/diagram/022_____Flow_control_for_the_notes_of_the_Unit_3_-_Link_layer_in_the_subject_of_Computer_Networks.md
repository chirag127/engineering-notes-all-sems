### Flow control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other  .
- Flow control regulates the amount of data that a sender can send before it waits for an acknowledgment from the receiver .
- Flow control prevents a fast sender from overwhelming a slow receiver with too many frames or data packets  .
- Flow control can be implemented at the data link layer or the transport layer  .
- Flow control methods at the data link layer include:
  - Stop-and-wait: The sender sends one frame and waits for an acknowledgment from the receiver before sending the next frame .
  - Sliding window: The sender can send multiple frames within a window size without waiting for an acknowledgment from the receiver. The window size is the number of frames that can be sent or received at a time .
  - Pause frame: The receiver can send a special frame to the sender to pause the transmission for a specified period of time. This is used in full duplex Ethernet link segments.