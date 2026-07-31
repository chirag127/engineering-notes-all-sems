# Flow control for the notes of the Unit 3 - Link layer in the subject of Computer Networks

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- Flow control restricts and coordinates the amount of data that a sender can send before it waits for an acknowledgment from the receiver .
- Flow control prevents the sender from overwhelming the receiver with more data than it can handle, which may cause data loss or buffer overflow.
- Flow control can be implemented at the data link layer or the transport layer, depending on the protocol and the network architecture .
- Flow control methods can be classified into two categories: stop-and-wait and sliding window .
  - Stop-and-wait: The sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. This method is simple but inefficient, as it wastes bandwidth and introduces delays .
  - Sliding window: The sender can send multiple frames without waiting for acknowledgments, as long as the number of unacknowledged frames does not exceed a predefined window size. This method is more efficient and flexible, as it utilizes the bandwidth and adapts to the network conditions .
- Flow control can also be combined with error control, which is a technique that detects and corrects errors in data transmission. Error control methods include parity check, checksum, cyclic redundancy check (CRC), and automatic repeat request (ARQ) .