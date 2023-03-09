### Congestion control algorithms for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

Congestion control is a vital aspect of network performance as it ensures that the network does not get overloaded with traffic. Congestion occurs when the network receives more traffic than it can handle, leading to packet loss, delay, and reduced throughput. Congestion control algorithms are used to manage the flow of traffic and prevent congestion in the network. In this section, we will explore the different congestion control algorithms used in computer networks.

#### 1. Window-based congestion control algorithms

Window-based congestion control algorithms are the most commonly used algorithms for congestion control. In these algorithms, a sender maintains a congestion window that limits the number of packets it can send at a time. The sender adjusts the size of the congestion window dynamically based on the network conditions. The most widely used window-based congestion control algorithms are:

- TCP Reno: TCP Reno is a popular congestion control algorithm used in TCP connections. It uses a combination of additive increase and multiplicative decrease to adjust the congestion window size. TCP Reno reduces the congestion window size by half when congestion is detected, and then gradually increases it until congestion occurs again.

- TCP Vegas: TCP Vegas is a congestion control algorithm that uses a different approach than TCP Reno. It measures the round-trip time (RTT) of the packets and uses it to estimate the available bandwidth in the network. It then adjusts the congestion window size accordingly. TCP Vegas is known for its low delay and high throughput.

#### 2. Rate-based congestion control algorithms

Rate-based congestion control algorithms are based on regulating the rate of traffic instead of the window size. In these algorithms, a sender sends packets at a constant rate, and the rate is adjusted based on the network conditions. The most widely used rate-based congestion control algorithms are:

- TCP CUBIC: TCP CUBIC is a congestion control algorithm that uses a cubic function to adjust the sending rate. It measures the congestion window size and the RTT to estimate the available bandwidth. It then increases or decreases the sending rate based on the cubic function.

- TCP BBR: TCP BBR is a congestion control algorithm that uses a model-based approach to estimate the available bandwidth. It measures the bottleneck bandwidth and the round-trip time to adjust the sending rate. TCP BBR is known for its low delay and high throughput.

#### Advantages of congestion control algorithms

- Prevents network congestion and reduces packet loss
- Improves network efficiency and throughput
- Maintains fairness among different flows in the network
- Enhances user experience by reducing delay and increasing reliability

#### Disadvantages of congestion control algorithms

- Can cause underutilization of network resources
- Can lead to performance degradation in certain network conditions
- May require complex algorithms and configurations

#### Examples of applications of congestion control algorithms

- Video streaming services like Netflix and YouTube use congestion control algorithms to ensure smooth playback and reduce buffering.
- Cloud computing services like AWS and Azure use congestion control algorithms to manage the flow of traffic between different data centers and servers.
- Online gaming services use congestion control algorithms to reduce latency and ensure a smooth gaming experience.

In conclusion, congestion control algorithms play a crucial role in ensuring efficient and reliable network performance. Window-based and rate-based congestion control algorithms are the most widely used algorithms, and they have their advantages and disadvantages. By understanding these algorithms, network engineers can design and implement efficient and reliable network infrastructures.