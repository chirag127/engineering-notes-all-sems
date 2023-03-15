### Flow control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other  .
- Flow control regulates the amount of data that a sender can send before it waits for an acknowledgment from the receiver .
- Flow control prevents a fast sender from overwhelming a slow receiver with too many frames or data units  .
- Flow control can be implemented at the data link layer or the transport layer  .
- Flow control methods at the data link layer include:
  - Stop-and-wait: The sender sends one frame and waits for an acknowledgment before sending the next frame .
  - Sliding window: The sender can send multiple frames within a window size without waiting for an acknowledgment. The window size is the number of frames that can be sent or received at a time .
- Flow control methods at the transport layer include:
  - TCP: The sender and the receiver negotiate a window size based on their buffer capacities and network conditions. The sender can send data up to the window size and the receiver can send acknowledgments and update the window size accordingly .
  - UDP: The sender does not perform any flow control and the receiver has to deal with the possibility of data loss or congestion .
- Flow control on Ethernet can be implemented by using pause frames, which are special frames that can pause the transmission of data on a link for a specified duration.