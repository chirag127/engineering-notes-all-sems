Hello, I am Sydney, your AI assistant. I can help you with your query.

### Congestion control algorithms in computer networks

Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse. Congestive-Avoidance Algorithms (CAA) are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network.

Some of the common congestion control algorithms are:

- **Leaky Bucket**: This algorithm discovers its use in the context of network traffic shaping or rate-limiting. The algorithm allows controlling the rate at which a record is injected into a network and managing burstiness in the data rate. It works by sending packets at a constant rate, regardless of the burstiness of the incoming traffic. The excess packets are discarded or buffered, depending on the implementation.

- **Token Bucket**: This algorithm is similar to the leaky bucket, but it allows some burstiness in the data rate. It works by generating tokens at a constant rate and storing them in a bucket. Each packet requires a token to be sent. If the bucket is empty, the packet has to wait until a token is generated. If the bucket is full, the newly generated tokens are discarded. This way, the algorithm allows some packets to be sent at a higher rate than the token generation rate, as long as there are enough tokens in the bucket.

- **Slow Start**: This algorithm is used by TCP to probe the network capacity and avoid sending more data than the network can handle. It works by starting with a small congestion window (CWND) and doubling it every round-trip time (RTT) until a threshold is reached or a packet loss occurs. The threshold is then set to half of the CWND before the loss, and the algorithm switches to congestion avoidance mode.

- **Congestion Avoidance**: This algorithm is used by TCP to maintain a steady state of data transmission and avoid congestion. It works by increasing the CWND by one segment every RTT, as long as there is no packet loss. If a packet loss occurs, the algorithm reduces the CWND by half and enters the slow start mode again.

- **Additive Increase/Multiplicative Decrease (AIMD)**: This algorithm is a generalization of the congestion avoidance algorithm, where the CWND is increased by a constant factor every RTT and decreased by a multiplicative factor when a packet loss occurs. The most common values for the factors are 1 and 0.5, respectively.

- **BIC and CUBIC**: These are two variants of the AIMD algorithm that are designed to achieve high throughput and fairness in high-speed networks. BIC uses a binary search approach to find the optimal CWND, while CUBIC uses a cubic function to adjust the CWND. Both algorithms are more aggressive than AIMD in increasing the CWND, but also more conservative in decreasing it.

- **BBR**: This is a recent algorithm that aims to achieve optimal bandwidth and minimal latency in the network. It works by estimating the bottleneck bandwidth and the minimum RTT of the network, and adjusting the CWND and the pacing rate accordingly. It does not rely on packet losses or acknowledgments as signals of congestion, but rather on the changes in the bandwidth and RTT estimates.