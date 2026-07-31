Flow control in transport layer is a mechanism that regulates the rate of data transmission between two nodes to prevent data loss or buffer overflow. It is an end-to-end process that involves feedback from the receiver to the sender. There are two main types of flow control in transport layer: window-based and rate-based.

Window-based flow control uses a sliding window protocol to dynamically adjust the size of the window, which is the number of packets that can be sent without acknowledgment from the receiver. The sender maintains a send window and the receiver maintains a receive window. The sender can only send packets that fall within the send window, and the receiver can only accept packets that fall within the receive window. The receiver sends acknowledgments to the sender to indicate the status of the receive window. The sender updates the send window based on the acknowledgments. This type of flow control is used by TCP.

Rate-based flow control uses a fixed rate of transmission that does not require acknowledgment from the receiver. The sender and the receiver agree on a rate beforehand and the sender sends packets at that rate. The receiver discards any packets that exceed the rate or arrive out of order. This type of flow control is used by UDP.

### Flow control in transport layer

```
+-----------------+        +-----------------+
|     Sender      |        |    Receiver     |
+-----------------+        +-----------------+
|                 |        |                 |
|  Send window    |        | Receive window  |
|                 |        |                 |
|  +-----------+  |        |  +-----------+  |
|  | 1 | 2 | 3 |  |        |  | 1 | 2 | 3 |  |
|  +-----------+  |        |  +-----------+  |
|                 |        |                 |
|  Send buffer    |        | Receive buffer  |
|                 |        |                 |
|  +-----------+  |        |  +-----------+  |
|  | 4 | 5 | 6 |  |        |  | 4 | 5 | 6 |  |
|  +-----------+  |        |  +-----------+  |
|                 |        |                 |
+-----------------+        +-----------------+
      |   |   |                |   |   |
      |   |   +----------------+   |   |
      |   +------------------------+   |
      +---------------------------------+
```

In this diagram, the sender has a send window of size 3 and the receiver has a receive window of size 3. The sender can send packets 1, 2, and 3 without waiting for acknowledgment. The receiver can accept packets 1, 2, and 3 and store them in the receive buffer. The sender and the receiver also have send and receive buffers that store the packets that are not in the window. The sender has packets 4, 5, and 6 in the send buffer and the receiver has packets 4, 5, and 6 in the receive buffer. When the receiver acknowledges packet 1, the sender slides the send window to the right by one packet and can send packet 4. Similarly, when the receiver receives packet 1, it slides the receive window to the right by one packet and can accept packet 4. This process continues until all the packets are transmitted and received.