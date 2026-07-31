Flow control is a technique that allows two stations working at different speeds to communicate with each other. It is a set of measures taken to regulate the amount of data that a sender can send so that a fast sender does not overwhelm a slow receiver. Flow control in data link layer restricts the number of frames the sender can send before it waits for an acknowledgment from the receiver . There are two main approaches of flow control: stop-and-wait and sliding window .

#### Flow control in link layer in Computer Networks

```
+-----------------+     +-----------------+
|     Sender      |     |    Receiver     |
+-----------------+     +-----------------+
|                 |     |                 |
|  Data Link      |     |  Data Link      |
|  Layer          |     |  Layer          |
|                 |     |                 |
|  +-----------+  |     |  +-----------+  |
|  | Flow      |  |     |  | Flow      |  |
|  | Control   |  |     |  | Control   |  |
|  | Protocol  |  |     |  | Protocol  |  |
|  +-----------+  |     |  +-----------+  |
|                 |     |                 |
|  +-----------+  |     |  +-----------+  |
|  | Frame     |  |     |  | Frame     |  |
|  | Buffer    |  |     |  | Buffer    |  |
|  +-----------+  |     |  +-----------+  |
|                 |     |                 |
+-----------------+     +-----------------+
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       | | | | |             | | | | |
       v v v v v             v v v v v
+-----------------+     +-----------------+
|     Physical    |     |    Physical     |
|     Layer       |     |    Layer        |
+-----------------+     +-----------------+
```

The diagram above shows the flow control in link layer in computer networks. The sender and the receiver have a data link layer that implements a flow control protocol. The protocol regulates the number of frames that the sender can transmit before waiting for an acknowledgment from the receiver. The sender and the receiver also have a frame buffer that stores the frames before they are sent or processed. The physical layer is responsible for transmitting and receiving the frames over the medium. The flow control protocol can use different methods to control the flow of frames, such as stop-and-wait or sliding window.