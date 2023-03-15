TCP congestion control is a mechanism that regulates the amount of data that a sender can transmit over a network. It aims to prevent congestion collapse, which occurs when too many packets are sent to a network and cause delays and packet losses. TCP congestion control consists of three main phases: slow start, congestion avoidance, and congestion recovery. Here is a diagram that illustrates the TCP congestion control algorithm in the transport layer:

### TCP Congestion Control in Transport Layer

```
    +-----------------+     +-----------------+
    |    Sender       |     |    Receiver     |
    +-----------------+     +-----------------+
    |                 |     |                 |
    |  Congestion     |     |                 |
    |  Window (cwnd)  |     |  Receive        |
    |                 |     |  Window (rwnd)  |
    |                 |     |                 |
    +--------+--------+     +--------+--------+
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  SYN
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  SYN-ACK
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  ACK
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |  TCP connection established
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (1 segment)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  ACK (1 segment)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (2 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  ACK (2 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (4 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  ACK (4 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (8 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  ACK (8 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (16 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             <-----------------------+  ACK (16 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             |                       |
             +----------------------->  Data (32 segments)
             |                       |
             |                       |
             |                       |
             |                       |
             |