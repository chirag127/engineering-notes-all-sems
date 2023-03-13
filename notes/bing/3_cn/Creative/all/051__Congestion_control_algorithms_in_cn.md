### Congestion control algorithms in cn

Congestion control algorithms are techniques to prevent or reduce network congestion by regulating the amount of data that can be sent by the source nodes. Congestion occurs when the demand for network resources exceeds the available capacity, resulting in packet loss, delay, and reduced throughput.

Some of the common congestion control algorithms are:

- **Additive Increase Multiplicative Decrease (AIMD):** This algorithm increases the window size by one segment for every successful transmission (additive increase) and halves the window size for every packet loss (multiplicative decrease). This algorithm is fair and stable, but it is slow to converge to the optimal window size and it may cause oscillations around the equilibrium point.

- **Multiplicative Increase Multiplicative Decrease (MIMD):** This algorithm multiplies the window size by a constant factor for every successful transmission (multiplicative increase) and multiplies the window size by another constant factor for every packet loss (multiplicative decrease). This algorithm is faster to converge to the optimal window size, but it is unfair and unstable, as it may cause some flows to dominate the network and others to starve.

- **Additive Increase Additive Decrease (AIAD):** This algorithm increases the window size by a constant amount for every successful transmission (additive increase) and decreases the window size by a constant amount for every packet loss (additive decrease). This algorithm is fair and stable, but it is slow to converge to the optimal window size and it may cause underutilization of the network.

- **Multiplicative Increase Additive Decrease (MIAD):** This algorithm multiplies the window size by a constant factor for every successful transmission (multiplicative increase) and decreases the window size by a constant amount for every packet loss (additive decrease). This algorithm is faster to converge to the optimal window size, but it is unfair and unstable, as it may cause some flows to dominate the network and others to starve.

- **Binary Exponential Backoff (BEB):** This algorithm is used in Ethernet networks to resolve collisions. It works by doubling the random waiting time after each collision, until a maximum value is reached or the transmission is successful. This algorithm reduces the probability of collisions, but it may cause long delays and waste bandwidth.

- **Slow Start:** This algorithm is used in TCP to avoid sending too many packets at the beginning of a connection. It works by starting with a small window size and doubling it for every successful transmission, until a threshold value is reached or a packet loss occurs. This algorithm allows the sender to probe the network capacity and avoid congestion, but it may cause slow transmission rates for short-lived connections.

- **Congestion Avoidance:** This algorithm is used in TCP to avoid congestion after the slow start phase. It works by increasing the window size by one segment for every round trip time (RTT), until a packet loss occurs. Then, it reduces the window size by half and enters the slow start phase again. This algorithm maintains a balance between efficiency and fairness, but it may cause oscillations around the optimal window size.

- **Fast Retransmit:** This algorithm is used in TCP to detect and recover from packet losses. It works by using duplicate acknowledgments (ACKs) to infer packet losses. If the sender receives three duplicate ACKs for the same segment, it assumes that the segment was lost and retransmits it without waiting for a timeout. This algorithm reduces the delay and improves the throughput, but it may not work well for multiple packet losses or out-of-order segments.

- **Fast Recovery:** This algorithm is used in TCP to avoid reducing the window size too much after a packet loss. It works by using the duplicate ACKs to estimate the new window size, instead of halving it. The sender sets the window size to the number of outstanding segments plus the number of duplicate ACKs, and continues the congestion avoidance phase. This algorithm avoids the slow start phase and maintains a high transmission rate, but it may cause unfairness and instability in some scenarios.