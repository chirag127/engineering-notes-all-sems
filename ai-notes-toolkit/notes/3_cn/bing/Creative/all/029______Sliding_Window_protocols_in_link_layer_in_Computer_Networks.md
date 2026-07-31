#### Sliding Window Protocols in Link Layer in Computer Networks

- Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames  .
- The sliding window is also used in Transmission Control Protocol (TCP), which operates at the transport layer .
- In sliding window protocols, the sender has a buffer called the sending window and the receiver has a buffer called the receiving window .
- The sender can send multiple frames at a time before receiving an acknowledgment (ACK) from the receiver .
- The receiver can send back an ACK for each frame or for a group of frames.
- The size of the window determines how many frames can be sent or received at a time  .
- The window slides along the sequence of frames as the sender and receiver exchange data and ACKs  .
- The sliding window protocol ensures that the frames are delivered in order and without errors  .
- There are different types of sliding window protocols, such as stop-and-wait, go-back-N, and selective repeat  .
- Each type of sliding window protocol has different advantages and disadvantages in terms of efficiency, complexity, and error recovery  .