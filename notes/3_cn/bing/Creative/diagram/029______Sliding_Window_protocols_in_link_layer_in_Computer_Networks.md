#### Sliding Window protocols in link layer in Computer Networks

The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames. Using the sliding window protocol, the sender can send multiple frames at a time. When the receiver receives the frame, it sends back an ACK (acknowledgment) to the sender. The sliding window protocol uses a mechanism of sequence numbers to identify and order the frames. The sender and the receiver maintain a window of frames that can be sent or received at a time. The window size is determined by the available buffer space and the bandwidth of the channel.

A possible ASCII diagram for the sliding window protocol is shown below. The diagram assumes a window size of 4 and a sequence number range of 8. The sender and the receiver exchange frames and ACKs using the sliding window technique. The sender can send up to 4 frames without waiting for an ACK, and the receiver can accept up to 4 frames without sending an ACK. The sender and the receiver slide their windows when they receive an ACK or a frame, respectively.

```
Sender: 0 1 2 3 4 5 6 7
        | | | | | | | |
        V V V V V V V V
        ----------------
        | 0 | 1 | 2 | 3 |  --> Send frames 0, 1, 2, 3
        ----------------
          ^   ^   ^   ^
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          V   V   V   V
        ----------------
        | 0 | 1 | 2 | 3 |  --> Receive frames 0, 1, 2, 3
        ----------------
Receiver: 0 1 2 3 4 5 6 7
        | | | | | | | |
        V V V V V V V V
        ----------------
        | 0 | 1 | 2 | 3 |  --> Send ACK 4
        ----------------
          ^   ^   ^   ^
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          V   V   V   V
        ----------------
        | 4 | 5 | 6 | 7 |  --> Send frames 4, 5, 6, 7
        ----------------
Sender: 0 1 2 3 4 5 6 7
        | | | | | | | |
        V V V V V V V V
        ----------------
        | 4 | 5 | 6 | 7 |  --> Receive ACK 4 and slide window
        ----------------
          ^   ^   ^   ^
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          V   V   V   V
        ----------------
        | 4 | 5 | 6 | 7 |  --> Receive frames 4, 5, 6, 7
        ----------------
Receiver: 0 1 2 3 4 5 6 7
        | | | | | | | |
        V V V V V V V V
        ----------------
        | 4 | 5 | 6 | 7 |  --> Send ACK 0
        ----------------
          ^   ^   ^   ^
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |   |   |   |
          |