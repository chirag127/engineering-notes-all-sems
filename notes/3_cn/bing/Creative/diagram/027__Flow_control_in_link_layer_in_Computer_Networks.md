Flow control in the data link layer is a technique that controls the rate of data transmission between the sender and receiver. It is a set of measures taken to regulate the amount of data that a sender sends so that a fast sender does not overwhelm a slow receiver. 

There are two main techniques of flow control in the data link layer: stop-and-wait and sliding window. 

Stop-and-wait flow control is a simple method where the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after processing the received frame. This method is inefficient if the propagation delay is much longer than the transmission delay. 

Sliding window flow control is a more advanced method where the sender can send multiple frames without waiting for acknowledgments. The sender maintains a window of frames that it can send at any time. The receiver also maintains a window of frames that it can receive at any time. The receiver sends acknowledgments for the frames it has received and also indicates the size of its window. The sender adjusts its window size according to the receiver's window size. This method is more efficient and can utilize the channel capacity better. 

#### Flow control in link layer in Computer Networks

The following diagram illustrates the basic architecture of a flow control in link layer in computer networks. It shows how the sender and receiver exchange frames and acknowledgments using the sliding window technique. The sender's window size is 4 and the receiver's window size is 3. The sender has 8 frames to send, numbered from 0 to 7. The receiver has a buffer to store the received frames.

```
    Sender                          Receiver
+------------+                  +------------+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |            |  Buffer
+------------+                  +------------+
|<---------->|                    |<-------->|
  Window size = 4                  Window size = 3
    |  |  |  |                      |  |  |
    |  |  |  +----------------------+  |  |
    |  |  +---------------------------+  |
    |  +---------------------------------+
    +------------------------------------+
       Frames sent without waiting for ACKs

+------------+                  +------------+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 | 1 | 2 |  Buffer
+------------+                  +------------+
    |<---------->|                |<-------->|
      Window size = 4              Window size = 3
       |  |  |  |                  |  |  |  |
       |  |  |  |                  |  |  |  +---+
       |  |  |  |                  |  |  +------+|
       |  |  |  |                  |  +---------+|
       |  |  |  |                  +------------+|
       |  |  |  +--------------------------------+
       |  |  +-----------------------------------+
       |  +--------------------------------------+
       +-----------------------------------------+
              ACKs received, window slides

+------------+                  +------------+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 0 | 1 | 2 |  Buffer
+------------+                  +------------+
       |<---------->|            |<-------->|
         Window size = 4          Window size = 3
          |  |  |  |              |  |  |  |
          |  |  |  +--------------+  |  |  |
          |  |  +---------------------+  |
          |  +---------------------------+
          +------------------------------+
             Frames sent without waiting for ACKs

+------------+                  +------------+
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 3 | 4 | 5 |  Buffer
+------------+                  +------------+
          |<---------->|        |<-------->|
            Window size = 4      Window size = 3
             |  |  |  |          |  |  |  |
             |  |  |  |          |  |  |  +---+
             |  |  |  |          |  |  +------+|
             |  |  |  |          |