Sliding window protocols are data link layer protocols for reliable and sequential delivery of data frames. The sliding window is also used in Transmission Control Protocol. In this protocol, multiple frames can be sent by a sender at a time before receiving an acknowledgment from the receiver.

The sliding window protocol uses a mechanism of sequence numbers to identify and track the frames. The sender and the receiver maintain a window of frames that can be sent or received at a time. The window size is determined by the buffer capacity and the bandwidth of the channel. The window slides as the sender receives acknowledgments from the receiver or as the receiver receives new frames from the sender.

There are two types of sliding window protocols: Go-Back-N ARQ and Selective Repeat ARQ. Go-Back-N ARQ is a protocol where the sender sends a window of frames and waits for the acknowledgment of the last frame. If any frame is corrupted or lost, the sender retransmits all the frames from the lost or corrupted frame onwards. The receiver discards any out-of-order frames and sends a negative acknowledgment to the sender. The receiver window size is always one in this protocol.

Selective Repeat ARQ is a protocol where the sender sends a window of frames and waits for the individual acknowledgments of each frame. If any frame is corrupted or lost, the sender retransmits only that frame. The receiver buffers any out-of-order frames and sends a positive acknowledgment to the sender. The receiver window size is equal to the sender window size in this protocol.

The following diagram illustrates the basic architecture of a sliding window protocol:

```
    Sender                          Receiver
+-------------+                 +-------------+
|             |                 |             |
|  Send      |                 |  Receive    |
|  Buffer    |                 |  Buffer     |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  Send      |                 |  Receive    |
|  Window    |                 |  Window     |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  Sequence  |                 |  Sequence  |
|  Numbers   |                 |  Numbers   |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  Frames    |                 |  Frames    |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  ACKs      |                 |  ACKs      |
|             |                 |             |
+-------------+                 +-------------+
```

The following diagram illustrates an example of a Go-Back-N ARQ protocol:

```
    Sender                          Receiver
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0          |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2 3 4  |
|             |                 |             |
+-------------+                 +-------------+
|             |                 |             |
|  0 1 2 3 4  |                 |  0 1 2