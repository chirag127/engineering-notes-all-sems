Flow control in transport layer is a mechanism that regulates the amount of data that can be sent by a sender to a receiver, to avoid congestion and data loss. It is performed end-to-end, meaning that the sender and receiver communicate with each other using feedback messages, such as acknowledgments and window sizes, to adjust the rate of data transmission.

### Flow control in transport layer

The following diagram illustrates the basic architecture of flow control in transport layer using the TCP protocol:

```
    Sender                          Receiver
+------------+                  +------------+
| Application|                  | Application|
+------------+                  +------------+
|    TCP     |                  |    TCP     |
+------------+                  +------------+
|    IP      |                  |    IP      |
+------------+                  +------------+
|  Network   |                  |  Network   |
+------------+                  +------------+
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
|            |                  |            |
+------------+                  +------------+
|    Data    |                  |    Data    |
+------------+                  +------------+
|    ACK     |<-----------------|    ACK     |
+------------+                  +------------+
|    Win     |----------------->|    Win     |
+------------+                  +------------+
```

The sender and receiver have a buffer to store the data that is sent or received. The sender maintains a variable called the **congestion window** (Win), which indicates the maximum amount of data that can be sent without receiving an acknowledgment (ACK) from the receiver. The receiver maintains a variable called the **receive window** (RWin), which indicates the amount of free space in the buffer that can receive more data. The sender adjusts the congestion window based on the feedback from the receiver, such as the ACKs and the receive window.

The sender sends data in segments, each with a sequence number, and waits for an ACK from the receiver. The receiver sends an ACK for each segment that it receives and stores in the buffer. The ACK also contains the receive window size, which informs the sender how much more data can be sent. The sender updates the congestion window based on the receive window size and the number of ACKs received. The sender can send more data if the congestion window is larger than the amount of data in transit, or wait if the congestion window is smaller.

The receiver can also use a technique called **flow control by discarding** to signal the sender to slow down. This technique involves dropping some segments that arrive when the buffer is full, and sending a smaller receive window size or a zero window to the sender. The sender will then reduce the congestion window and retransmit the dropped segments.

Flow control in transport layer ensures that the sender and receiver are synchronized and that the data is delivered reliably and efficiently. It is different from flow control in data link layer, which is performed locally between two physically connected nodes, and uses techniques such as stop-and-wait, sliding window, or backpressure.