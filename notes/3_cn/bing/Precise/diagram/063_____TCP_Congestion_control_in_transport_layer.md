### TCP Congestion control in transport layer

Here is an ASCII diagram that illustrates the TCP Congestion control in the transport layer:

```
          +------------+
          | Application|
          +------+-----+
                 |
          +------+-----+
          |   Transport|
          |  +-------+ |
          |  |  TCP  | |
          |  +---+---+ |
          |      |     |
          |Congestion  |
          | Control    |
          +------+-----+
                 |
          +------+-----+
          |   Network  |
          +------+-----+
                 |
          +------+-----+
          | Data Link  |
          +------+-----+
                 |
          +------+-----+
          |  Physical  |
          +------------+
```

TCP congestion control is a mechanism used by the transport layer to control the flow of data in a network. It aims to prevent network congestion by regulating the amount of data that can be sent at any given time. This is achieved by adjusting the size of the congestion window, which determines the maximum amount of data that can be sent before receiving an acknowledgment from the receiver. The size of the congestion window is adjusted based on network conditions, such as packet loss or delay, to ensure that the network is not overwhelmed with traffic.
