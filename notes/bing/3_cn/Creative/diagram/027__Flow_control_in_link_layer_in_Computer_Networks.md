Flow control is a technique that allows two stations working at different speeds to communicate with each other. It regulates the amount of data that a sender can send before waiting for an acknowledgment from the receiver. There are two main methods of flow control in the data link layer: stop-and-wait and sliding window.

Stop-and-wait is a simple method where the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing each frame. This method is easy to implement but has low efficiency and high delay.

Sliding window is a more advanced method where the sender can send multiple frames without waiting for an acknowledgment from the receiver. The sender and the receiver maintain a window of frames that can be sent or received at any time. The window size is determined by the available buffer space and the bandwidth-delay product of the link. The sender slides the window forward when it receives an acknowledgment from the receiver. The receiver slides the window forward when it receives a frame from the sender. This method is more efficient and has lower delay than stop-and-wait.

The following diagram illustrates the basic architecture of a flow control in the data link layer using the sliding window method:

```
Sender                          Receiver
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+
|                  |            |                  |
+------------------+            +------------------+


  Frame 1  Frame 2  Frame 3  Frame 4  Frame 5  Frame 6  Frame 7  Frame 8
  |       |       |       |       |       |       |       |       |
  |       |       |       |       |       |       |       |       |
  |       |