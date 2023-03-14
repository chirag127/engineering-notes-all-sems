TCP Congestion control is a mechanism that regulates the amount of data that a sender can transmit over a network, based on the network conditions and the receiver's feedback. TCP Congestion control aims to achieve high throughput, low delay, and fair bandwidth allocation among competing flows.

The following ASCII diagram illustrates the basic architecture of TCP Congestion control in transport layer:

```
+----------------+     +----------------+     +----------------+
| Application    |     | Application    |     | Application    |
| Layer          |     | Layer          |     | Layer          |
+----------------+     +----------------+     +----------------+
| Transport      |     | Transport      |     | Transport      |
| Layer          |     | Layer          |     | Layer          |
|                |     |                |     |                |
|  +----------+  |     |  +----------+  |     |  +----------+  |
|  | TCP      |  |     |  | TCP      |  |     |  | TCP      |  |
|  |          |  |     |  |          |  |     |  |          |  |
|  | Congestion|  |     |  | Congestion|  |     |  | Congestion|  |
|  | Control   |  |     |  | Control   |  |     |  | Control   |  |
|  | Algorithm |  |     |  | Algorithm |  |     |  | Algorithm |  |
|  +----------+  |     |  +----------+  |     |  +----------+  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
| Network       |     | Network       |     | Network       |
| Layer         |     | Layer         |     | Layer         |
+----------------+     +----------------+     +----------------+
| Link          |     | Link          |     | Link          |
| Layer         |     | Layer         |     | Layer         |
+----------------+     +----------------+     +----------------+
| Physical      |     | Physical      |     | Physical      |
| Layer         |     | Layer         |     | Layer         |
+----------------+     +----------------+     +----------------+

```

The diagram shows three TCP senders, each with a congestion control algorithm that adjusts the size of the congestion window (cwnd) based on the network conditions and the receiver's feedback. The congestion window is the amount of data that a sender can transmit without receiving an acknowledgment from the receiver. The congestion control algorithm can be in one of four phases: slow start, congestion avoidance, fast recovery, or fast retransmit.

- Slow start: The sender starts with a small cwnd and increases it exponentially for every acknowledgment received, until it reaches a threshold (ssthresh) or detects congestion.
- Congestion avoidance: The sender increases the cwnd linearly for every acknowledgment received, until it detects congestion.
- Fast recovery: The sender reduces the cwnd by half and enters the congestion avoidance phase, after receiving three duplicate acknowledgments (indicating a packet loss).
- Fast retransmit: The sender retransmits the lost packet and reduces the cwnd by half, after receiving a timeout (indicating a long delay).

The diagram also shows the network layer, which is responsible for routing the packets from the sender to the receiver, and the link and physical layers, which are responsible for transmitting the packets over the physical medium. The network layer may drop packets due to congestion, which triggers the congestion control algorithm to reduce the cwnd and avoid further congestion. The network layer may also reorder or delay packets, which affects the performance of the congestion control algorithm.