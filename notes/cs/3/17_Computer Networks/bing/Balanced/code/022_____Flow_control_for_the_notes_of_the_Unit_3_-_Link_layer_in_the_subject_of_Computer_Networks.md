### Flow control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other  .
- Flow control regulates the amount of data that a sender can send before it waits for an acknowledgment from the receiver .
- Flow control prevents a fast sender from overwhelming a slow receiver with too many frames or data units  .
- Flow control can be implemented at the data link layer or the transport layer  .
- Flow control methods at the data link layer include:
  - Stop-and-wait: The sender sends one frame and waits for an acknowledgment before sending the next frame .
  - Sliding window: The sender can send multiple frames within a window size without waiting for an acknowledgment. The window size is determined by the receiver's buffer capacity .
- Flow control methods at the transport layer include:
  - TCP: The sender and the receiver negotiate a window size based on the available buffer space and the network congestion. The sender adjusts the window size dynamically according to the feedback from the receiver and the network .
  - UDP: The sender does not perform any flow control and relies on the application layer to handle the data rate and the reliability .
- Flow control on Ethernet can be implemented by using pause frames, which are special frames that instruct the sender to stop transmitting for a specified period of time.