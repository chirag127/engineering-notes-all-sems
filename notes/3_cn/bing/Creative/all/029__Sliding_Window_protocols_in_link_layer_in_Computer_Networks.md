#### Sliding Window protocols in link layer in Computer Networks

- Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames.
- The sliding window is also used in Transmission Control Protocol (TCP) at the transport layer.
- In this protocol, multiple frames can be sent by a sender at a time before receiving an acknowledgment (ACK) from the receiver.
- The sliding window protocol uses a mechanism of sequence numbers to identify and track the frames.
- The sender and the receiver maintain a window of frames that can be sent or received at a time.
- The window size is determined by the buffer size of the receiver and the bandwidth of the channel.
- The window can slide along the sequence of frames as the sender transmits and the receiver acknowledges them.
- The sliding window protocol can improve the efficiency and throughput of data transmission by avoiding idle time and utilizing the channel capacity.
- There are two types of sliding window protocols: Go-Back-N ARQ and Selective Repeat ARQ.

##### Go-Back-N ARQ
- Go-Back-N ARQ protocol is also known as Go-Back-N Automatic Repeat Request.
- In this protocol, the sender can send up to N frames at a time, where N is the window size.
- The receiver can only accept frames in order and sends an ACK for the last received frame.
- The receiver discards any out-of-order or corrupted frames and does not send any ACK for them.
- The sender uses a timer for each frame and retransmits all the frames from the last unacknowledged frame if the timer expires.
- This protocol is simple and easy to implement, but it can waste a lot of bandwidth if there are many errors in the channel.
- A mnemonic to remember this protocol is: Go back to the last unacknowledged frame and send again.
- An example of Go-Back-N ARQ protocol is shown below in the figure.

```
Sender:  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
         |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
         |<----------------- Window Size = 8 ----------------->|
         |<----------------- Sent but not ACKed --------------->|
         |<----------------- Sent and ACKed ------------------->|
         |<----------------- Not sent and not ready ----------->|

Receiver:| 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
         |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
         |<----------------- Window Size = 1 ----------------->|
         |<----------------- Received and ACKed --------------->|
         |<----------------- Received but not ACKed ----------->|
         |<----------------- Not received and not ready ------->|

Scenario: Frame 6 is corrupted and frame 7 is lost in transmission.

Sender:  | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10| 11| 12| 13| 14| 15| 16| 17| 18| 19| 20|
         |___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|___|
         |<----------------- Window Size = 8 ----------------->|
         |                  |<----------------- Sent but not ACKed --------------->|
         |<----------------- Sent and ACKed ------------------->|
         |<----------------- Not sent and not ready ----------->|

Receiver:| 1 | 2