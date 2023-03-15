### Congestion Control Algorithms in Computer Networks

Congestion control is a mechanism that controls the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse. Congestive-Avoidance Algorithms (CAA) are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network.

There are two congestion control algorithms which are as follows:

1. **Leaky Bucket Algorithm**: The leaky bucket algorithm discovers its use in the context of network traffic shaping or rate-limiting. A leaky bucket execution and a token bucket execution are predominantly used for traffic shaping algorithms. This algorithm is used to control the rate at which data packets are sent into the network.

2. **Open Loop Congestion Control**: Open loop congestion control policies are applied to prevent congestion before it happens.

Congestion control algorithms use packet losses and delays as signals to infer congestion and decide how fast to send data. But the internet is complicated, and packets can be delayed and lost for reasons unrelated to network congestion.