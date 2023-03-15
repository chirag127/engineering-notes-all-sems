### TCP Congestion Control in Transport Layer

- TCP stands for Transmission Control Protocol. It is a connection-oriented and reliable transport layer protocol that facilitates the transmission of packets from source to destination.
- TCP congestion control is the main technique that prevents the Internet from slowing down due to over-utilization of network resources. It is the process of adjusting the sending rate of TCP packets based on the network conditions and feedback signals.
- TCP congestion control has three main objectives:
  - Efficiency: To utilize the network capacity as much as possible without causing congestion.
  - Fairness: To allocate the network resources fairly among competing TCP flows.
  - Stability: To avoid oscillations in the sending rate and maintain a smooth traffic pattern.
- TCP congestion control consists of four main components:
  - Congestion window (cwnd): The amount of data that the sender can transmit without receiving an acknowledgment from the receiver. It is dynamically adjusted by the sender based on the network conditions and feedback signals.
  - Slow start threshold (ssthresh): The threshold that determines the mode of congestion control. If cwnd is below ssthresh, the sender is in slow start mode and increases cwnd exponentially. If cwnd is above ssthresh, the sender is in congestion avoidance mode and increases cwnd linearly.
  - Acknowledgment (ACK): The message that the receiver sends to the sender to confirm the receipt of a packet or a group of packets. It also indicates the next expected sequence number from the sender.
  - Congestion signal: The signal that indicates the presence of congestion in the network. It can be either an explicit signal, such as an Explicit Congestion Notification (ECN) bit in the packet header, or an implicit signal, such as a packet loss or a timeout event.
- TCP congestion control has three main phases:
  - Slow start: The initial phase of congestion control, where the sender starts with a small cwnd and increases it exponentially for every ACK received, until it reaches ssthresh or a congestion signal occurs.
  - Congestion avoidance: The normal phase of congestion control, where the sender increases cwnd linearly for every ACK received, until a congestion signal occurs.
  - Congestion detection: The recovery phase of congestion control, where the sender detects a congestion signal and reduces cwnd and ssthresh accordingly, and then resumes slow start or congestion avoidance mode.
- TCP congestion control uses different algorithms to implement the above components and phases, such as Reno, NewReno, Tahoe, Vegas, Cubic, BBR, etc. Each algorithm has its own advantages and disadvantages in terms of performance, fairness, and stability .
- TCP congestion control is a complex and evolving topic that requires a deep understanding of the network dynamics and the trade-offs involved. It is also influenced by various factors, such as the operating system, the application, the router, the link, etc.

: http://witestlab.poly.edu/blog/tcp-congestion-control-basics/
: https://www.javatpoint.com/tcp
: https://www.geeksforgeeks.org/tcp-congestion-control/
: https://www.baeldung.com/cs/tcp-flow-control-vs-congestion-control
: https://networkengineering.stackexchange.com/questions/69932/congestion-control-in-transport-and-network-layers-in-tcp-ip