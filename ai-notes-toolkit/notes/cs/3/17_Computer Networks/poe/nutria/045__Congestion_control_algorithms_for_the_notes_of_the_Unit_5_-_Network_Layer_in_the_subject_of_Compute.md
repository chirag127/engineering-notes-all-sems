
### Congestion Control Algorithms

1. **Stop and Wait** - This is a simple algorithm used for flow and error control. It works by sending one packet at a time and waiting for an acknowledgment from the receiver before sending the next packet.

2. **Go-Back-N** - This is an improvement on the Stop and Wait algorithm. In this algorithm, multiple packets are sent without waiting for an acknowledgment. If an acknowledgment is not received, the sender sends all the packets again, starting from the one that was not acknowledged.

3. **Selective Repeat** - This algorithm is similar to Go-Back-N, but instead of sending all the packets again, only the ones that have not been acknowledged are sent.

4. **TCP** - Transmission Control Protocol is the most commonly used congestion control algorithm. It uses a sliding window mechanism to regulate the amount of data that can be sent. It also uses an algorithm called slow-start to increase the amount of data sent, and a congestion avoidance algorithm to reduce the amount of data sent if the network is congested.

5. **Explicit Congestion Notification (ECN)** - This is an algorithm that allows routers to inform the sender when the network is congested. This allows the sender to reduce the amount of data sent, thereby reducing congestion.