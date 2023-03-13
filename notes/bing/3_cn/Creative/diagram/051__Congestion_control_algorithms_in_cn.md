Congestion control algorithms are mechanisms that control the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse. Congestive-Avoidance Algorithms (CAA) are implemented at the TCP layer as the mechanism to avoid congestive collapse in a network.

There are different types of congestion control algorithms, such as:

- Leaky Bucket: This algorithm discovers its use in the context of network traffic shaping or rate-limiting. The algorithm allows controlling the rate at which a record is injected into a network and managing burstiness in the data rate. It works like a leaky bucket with a constant hole at the bottom. The bucket can hold a fixed amount of water, and any excess water will overflow and be lost. Similarly, the algorithm can accept a fixed amount of data, and any excess data will be discarded and lost.
- Token Bucket: This algorithm is similar to the leaky bucket, but it allows some burstiness in the data rate. It works like a leaky bucket with tokens instead of water. The bucket can hold a fixed number of tokens, and tokens are generated at a constant rate. A packet can be sent only if there is a token available in the bucket. If the bucket is full, any new tokens will be discarded. This algorithm allows sending data at a higher rate than the token generation rate, as long as there are enough tokens in the bucket.
- Additive Increase Multiplicative Decrease (AIMD): This algorithm is used by TCP to adjust the congestion window (CWND), which is the amount of data that can be sent without waiting for an acknowledgment. The algorithm works by increasing the CWND by one segment for every acknowledgment received (additive increase), and decreasing the CWND by half for every packet loss detected (multiplicative decrease). This algorithm ensures that the CWND grows slowly when the network is close to congestion, and shrinks quickly when congestion occurs.
- Slow Start: This algorithm is used by TCP to initialize the CWND at the beginning of a connection or after a packet loss. The algorithm works by setting the CWND to one segment, and doubling it for every acknowledgment received. This algorithm allows the CWND to grow exponentially until it reaches a threshold value, or a packet loss occurs. The threshold value is then set to half of the CWND before the packet loss. This algorithm ensures that the CWND grows rapidly when the network is underutilized, and avoids sending too much data too quickly.

The following diagram illustrates the basic architecture of a TCP congestion control algorithm:

```
+-----------------+        +-----------------+
|   Application   |        |   Application   |
+-----------------+        +-----------------+
|      TCP        |        |      TCP        |
+-----------------+        +-----------------+
|  Congestion     |        |  Congestion     |
|  Control        |        |  Control        |
+-----------------+        +-----------------+
|  CWND           |        |  CWND           |
+-----------------+        +-----------------+
|  ACK            |<------>|  ACK            |
+-----------------+        +-----------------+
|  Packet Loss    |<------>|  Packet Loss    |
+-----------------+        +-----------------+
|  IP             |        |  IP             |
+-----------------+        +-----------------+
|  Network        |<-----> |  Network        |
+-----------------+        +-----------------+
```