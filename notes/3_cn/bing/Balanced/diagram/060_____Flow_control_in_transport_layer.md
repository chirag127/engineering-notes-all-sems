Flow control in transport layer is a mechanism that regulates the rate of data transmission between two nodes to prevent data loss or buffer overflow. It can be implemented by using feedback-based or rate-based techniques. Feedback-based flow control relies on acknowledgments from the receiver to adjust the sender's window size. Rate-based flow control limits the sender's transmission rate without requiring acknowledgments from the receiver. Flow control in transport layer is different from flow control in data link layer, which operates on a single link and not on an end-to-end basis.

### Flow control in transport layer

```
+-----------------+        +-----------------+
|   Application   |        |   Application   |
+-----------------+        +-----------------+
|   Transport     |        |   Transport     |
+-----------------+        +-----------------+
|   Network       |        |   Network       |
+-----------------+        +-----------------+
|   Data Link     |        |   Data Link     |
+-----------------+        +-----------------+
|   Physical      |        |   Physical      |
+-----------------+        +-----------------+
|                 |        |                 |
|     Sender      |        |    Receiver     |
|                 |        |                 |
+-----------------+        +-----------------+
        |                          ^
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        |                          |
        v                          |
+-----------------+        +-----------------+
|   Physical      |        |   Physical      |
+-----------------+        +-----------------+
|   Data Link     |        |   Data Link     |
+-----------------+        +-----------------+
|   Network       |        |   Network       |
+-----------------+        +-----------------+
|   Transport     |        |   Transport     |
+-----------------+        +-----------------+
|   Application   |        |   Application   |
+-----------------+        +-----------------+
```

The transport layer segments the data from the application layer and adds a header with sequence number, acknowledgment number, window size, and other fields. The transport layer also maintains a buffer for storing the segments before sending or receiving them. The transport layer uses flow control to ensure that the sender does not overwhelm the receiver's buffer or the network capacity. The transport layer can use feedback-based or rate-based flow control techniques.

Feedback-based flow control:

- The receiver sends acknowledgments to the sender for the segments it receives and indicates the amount of buffer space available for receiving more segments. This is called the receiver's window size.
- The sender keeps track of the segments it has sent and not yet acknowledged. This is called the sender's window size.
- The sender adjusts its window size according to the receiver's window size and the network congestion. The sender does not send more segments than the minimum of the receiver's window size and the network capacity.
- The sender also uses timers and retransmission mechanisms to handle lost or corrupted segments.
- An example of feedback-based flow control is the TCP protocol.

Rate-based flow control:

- The sender limits its transmission rate to a predefined value without requiring acknowledgments from the receiver.
- The sender does not keep track of the segments it has sent and does not use retransmission mechanisms.
- The sender relies on the network layer to handle congestion and error control.
- The receiver discards any segments that arrive when its buffer is full or out of order.
- An example of rate-based flow control is the UDP protocol.