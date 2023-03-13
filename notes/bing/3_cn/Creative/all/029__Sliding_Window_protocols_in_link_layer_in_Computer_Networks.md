#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames  .
- Using the sliding window protocol, the sender can send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window protocol uses a mechanism of sequence numbers to identify and order the frames .
- The sender and the receiver maintain a window of frames that can be sent or received at a time   .
- The window size is determined by the available buffer space and the bandwidth-delay product.
- The window slides forward when the sender receives an acknowledgment or the receiver sends an acknowledgment   .
- There are two types of sliding window protocols: stop-and-wait and go-back-N  .
- In stop-and-wait protocol, the sender sends one frame at a time and waits for an acknowledgment before sending the next frame  .
- In go-back-N protocol, the sender can send up to N frames at a time without waiting for an acknowledgment, where N is the window size  .
- The sliding window protocol is also used in Transmission Control Protocol (TCP), which operates at the transport layer  .

##### Advantages of sliding window protocol
- It improves the efficiency and throughput of data transmission by allowing multiple frames to be sent at a time  .
- It provides flow control and error control by using acknowledgments and sequence numbers   .
- It adapts to the varying network conditions by adjusting the window size dynamically.

##### Disadvantages of sliding window protocol
- It may cause duplication of frames due to lost or delayed acknowledgments  .
- It may cause wastage of bandwidth and resources due to retransmission of frames in case of errors  .
- It may cause deadlock or starvation if the sender or the receiver does not send or receive any frames for a long time  .

##### Examples of sliding window protocol
- The following is an example of stop-and-wait protocol, where the sender sends one frame at a time and waits for an acknowledgment before sending the next frame. The window size is 1 for both the sender and the receiver.

| Sender | Receiver |
|--------|----------|
| S0     |          |
|        | R0       |
| S1     |          |
|        | R1       |
| S2     |          |
|        | R2       |
| S3     |          |
|        | R3       |

- The following is an example of go-back-N protocol, where the sender can send up to N frames at a time without waiting for an acknowledgment, where N is the window size. The window size is 3 for the sender and 1 for the receiver. The sender retransmits all the frames from the last unacknowledged frame in case of an error.

| Sender | Receiver |
|--------|----------|
| S0     |          |
| S1     |          |
| S2     |          |
|        | R0       |
| S3     |          |
|        | R1       |
| S4     |          |
|        | R2       |
| S5     |          |
|        | R3       |
| S6     |          |
|        | R4       |
| S7     |          |
|        | R5       |
| S8     |          |
|        | R6       |
|        |          |
|        | Error    |
| S6     |          |
| S7     |          |
| S8     |          |
|        | R6       |
|        | R7       |
|        | R8       |

##### Mnemonics and learning tricks for sliding window protocol
-