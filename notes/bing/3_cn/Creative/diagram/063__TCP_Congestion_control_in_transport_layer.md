TCP congestion control is a mechanism that aims to avoid network congestion by regulating the amount of data that a sender can transmit over a TCP connection. TCP congestion control consists of three phases: slow start, congestion avoidance, and congestion detection.

### TCP Congestion Control in Transport Layer

The following diagram illustrates the basic architecture of TCP congestion control in the transport layer:

```
+-----------------+    +-----------------+
| Application     |    | Application     |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Transport       |    | Transport       |
| Layer           |    | Layer           |
| +-------------+ |    | +-------------+ |
| | TCP Header  | |    | | TCP Header  | |
| | +---------+ | |    | | +---------+ | |
| | | Seq No. | | |    | | | Ack No. | | |
| | +---------+ | |    | | +---------+ | |
| | | Ack No. | | |    | | | Seq No. | | |
| | +---------+ | |    | | +---------+ | |
| | | Window  | | |    | | | Window  | | |
| | +---------+ | |    | | +---------+ | |
| | | Options | | |    | | | Options | | |
| | +---------+ | |    | | +---------+ | |
| +-------------+ |    | +-------------+ |
+-----------------+    +-----------------+
| Network         |    | Network         |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Data Link       |    | Data Link       |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
| Physical        |    | Physical        |
| Layer           |    | Layer           |
+-----------------+    +-----------------+
```

The sender and the receiver exchange TCP segments that contain a header and a payload. The TCP header contains several fields that are relevant for congestion control, such as:

- Sequence number (Seq No.): the number of the first byte in the segment's payload.
- Acknowledgment number (Ack No.): the number of the next expected byte from the other end of the connection.
- Window size (Window): the number of bytes that the sender or the receiver can accept at a time.
- Options: additional information that can be used for various purposes, such as specifying the maximum segment size (MSS), the congestion window (CWND), the slow start threshold (SSTHRESH), or the selective acknowledgment (SACK) option.

The sender maintains two variables that control the amount of data that it can send: the congestion window (CWND) and the receiver's advertised window (RWND). The sender can send up to min(CWND, RWND) bytes at a time, and it updates these variables based on the feedback from the receiver and the network conditions.

The receiver maintains a variable that indicates the amount of data that it can receive: the receiver's advertised window (RWND). The receiver sends this value to the sender in the window field of the TCP header, and it updates this value based on the amount of buffer space that it has available.

The sender and the receiver use the sequence number and the acknowledgment number fields to keep track of the data that has been sent and received. The sender expects to receive an acknowledgment (ACK) from the receiver for each segment that it sends, and the receiver expects to receive a segment with the next expected sequence number from the sender. If the sender does not receive an ACK within a certain time, it assumes that the segment has been lost or corrupted, and it retransmits the segment. If the receiver receives a segment with an out-of-order sequence number, it discards the segment and sends a duplicate ACK to the sender, indicating the next expected sequence number.

The sender and the receiver use the options field to exchange additional information that can improve the performance and reliability of the TCP connection. For example, the sender and the receiver can negotiate the maximum segment size (MSS) that they can use, which is the largest amount of data that can be sent in a single TCP segment. The sender and the receiver can also use the selective acknowledgment (SACK) option, which allows the receiver to acknowledge non-contiguous segments that it has received, and the sender to retransmit only the missing segments.

The sender uses the congestion window (CWND) and the slow start threshold (SSTHRESH) variables to adjust the rate