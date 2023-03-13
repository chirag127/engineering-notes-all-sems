The sliding window protocol is a technique for controlling the flow of data between two network nodes. It is used in the data link layer of the OSI model and in the TCP protocol. The sliding window protocol allows the sender to send multiple frames at a time before receiving an acknowledgment from the receiver. The sliding window protocol uses sequence numbers to identify each frame and to keep track of the frames that have been sent and received. The sliding window protocol also uses timers to detect and retransmit lost or corrupted frames.

#### Sliding Window protocols in link layer in Computer Networks

The following diagram illustrates the basic architecture of a sliding window protocol in the data link layer of a computer network.

```
+----------------+      +----------------+
|                |      |                |
|    Sender      |      |    Receiver    |
|                |      |                |
+----------------+      +----------------+
|                |      |                |
|    Data Link   |      |    Data Link   |
|    Layer       |      |    Layer       |
|                |      |                |
+----------------+      +----------------+
|                |      |                |
|    Physical    |      |    Physical    |
|    Layer       |      |    Layer       |
|                |      |                |
+----------------+      +----------------+
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     |    |                  |    |
     +----+                  +----+
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          |                  |
          +------------------+
                 Channel
```

The sender and the receiver each have a window of frames that they can send or receive at a time. The window size is determined by the available buffer space and the network conditions. The sender maintains a send window that contains the frames that have been sent but not yet acknowledged. The receiver maintains a receive window that contains the frames that have been received but not yet delivered to the upper layer. The sender and the receiver exchange window information using special control frames.

There are different types of sliding window protocols, such as stop-and-wait, go-back-N, and selective repeat. Each protocol has different rules for managing the window size, the sequence numbers, the acknowledgments, and the retransmissions. The main difference between these protocols is the amount of data that is retransmitted in case of an error. The stop-and-wait protocol retransmits the entire window, the go-back-N protocol retransmits from the first unacknowledged frame, and the selective repeat protocol retransmits only the lost or corrupted frames. The selective repeat protocol is the most efficient but also the most complex of the three.