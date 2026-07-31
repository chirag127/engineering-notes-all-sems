### Congestion control algorithms in computer networks

- Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestive collapse is a situation where the network performance degrades drastically due to excessive traffic and congestion.
- Congestion control algorithms can be broadly classified into two categories: open loop and closed loop.
- Open loop congestion control policies are applied to prevent congestion before it happens. They involve designing the network and choosing the appropriate protocols and parameters to avoid congestion.
- Closed loop congestion control policies are applied to detect and mitigate congestion after it happens. They involve monitoring the network state and adjusting the transmission rate or window size of the senders based on feedback signals such as packet loss, delay, or explicit notifications.
- Some examples of open loop congestion control techniques are admission control, traffic shaping, and resource reservation.
- Some examples of closed loop congestion control techniques are congestion avoidance, congestion recovery, and congestion notification.
- Congestion avoidance algorithms are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network. They use packet losses and delays as signals to infer congestion and decide how fast to send data.
- Some examples of congestion avoidance algorithms are slow start, additive increase/multiplicative decrease (AIMD), congestion window (CWND), and TCP variants such as Tahoe, Reno, New Reno, Vegas, and BBR.
- Congestion recovery algorithms are implemented at the TCP layer as the mechanism to recover from packet losses due to congestion. They use retransmission timers, acknowledgments, and fast retransmit and fast recovery techniques to resend the lost packets and resume the normal transmission.
- Congestion notification algorithms are implemented at the network layer as the mechanism to notify the senders about the congestion state of the network. They use explicit congestion notification (ECN) bits in the IP header or router-generated packets such as source quench or choke packets to inform the senders to reduce their transmission rate or window size.
- A mnemonic to remember the congestion control algorithms is: **O**pen **L**oop, **C**losed **L**oop, **A**voidance, **R**ecovery, **N**otification, or **OLCARN**.
- A table to compare the congestion control algorithms is given below:

| Algorithm | Category | Layer | Signal | Action |
|-----------|----------|-------|--------|--------|
| Admission control | Open loop | Application | N/A | Reject or accept new flows based on available resources |
| Traffic shaping | Open loop | Network | N/A | Control the rate and burstiness of data entering the network |
| Resource reservation | Open loop | Network | N/A | Reserve bandwidth and buffer space for specific flows |
| Slow start | Congestion avoidance | Transport | Packet loss | Increase the window size exponentially until a threshold is reached |
| AIMD | Congestion avoidance | Transport | Packet loss | Increase the window size linearly until a packet loss occurs, then decrease it multiplicatively |
| CWND | Congestion avoidance | Transport | Packet loss | Maintain a congestion window that limits the number of packets in the network |
| TCP variants | Congestion avoidance | Transport | Packet loss | Use different algorithms to adjust the window size based on packet loss |
| Retransmission timer | Congestion recovery | Transport | Timeout | Resend the lost packet after a certain time interval |
| Acknowledgment | Congestion recovery | Transport | Duplicate ACK | Resend the lost packet after receiving a certain number of duplicate ACKs |
| Fast retransmit and fast recovery | Congestion recovery | Transport | Duplicate ACK | Resend the lost packet and reduce the window size by half after receiving a certain number of duplicate ACKs |
| ECN | Congestion notification | Network | ECN bit | Set the ECN bit in the IP header to indicate congestion |
| Source quench | Congestion notification | Network | Source quench packet | Send a source quench packet to the sender to request a reduction in transmission rate |
| Choke packet | Congestion notification | Network | Choke packet | Send a choke packet to the sender to request a reduction in window size |