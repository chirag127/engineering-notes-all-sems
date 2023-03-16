### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Switched networks are networks that use switches to connect different nodes and forward packets based on their destination addresses.
- Switched networks can support multiple types of traffic, such as voice, video, and data, with different quality of service (QoS) requirements, such as delay, jitter, bandwidth, and loss.
- To provide QoS guarantees, switched networks need to use appropriate service disciplines to schedule the packets at the switches.
- Service disciplines are algorithms that determine the order and the rate of packet transmission at the switches.
- Priority-based service disciplines are service disciplines that assign different priority levels to different types of packets, and serve the packets according to their priority levels.
- Weighted round-robin service disciplines are service disciplines that assign different weights to different types of packets, and serve the packets in a round-robin fashion according to their weights.

#### Priority-Based Service Disciplines

- Priority-based service disciplines can be classified into two categories: strict priority (SP) and weighted fair queuing (WFQ).
- SP service discipline serves the packets in the order of their priority levels, without considering the packet size or the arrival rate. SP service discipline can provide low delay and jitter for high-priority packets, but it can starve low-priority packets if the high-priority traffic is heavy.
- WFQ service discipline serves the packets in a fair manner, by allocating a fraction of the bandwidth to each priority level according to a predefined weight. WFQ service discipline can provide proportional delay guarantees for different priority levels, but it can introduce high delay and jitter for all packets if the traffic is bursty.

#### Weighted Round-Robin Service Disciplines

- Weighted round-robin service disciplines can be classified into two categories: weighted round-robin (WRR) and rate-controlled frame-based weighted round-robin (RFWRR).
- WRR service discipline serves the packets in a round-robin fashion, by transmitting a fixed number of bytes from each priority level according to a predefined weight. WRR service discipline can provide proportional bandwidth guarantees for different priority levels, but it can introduce high delay and jitter for all packets if the packet size is variable.
- RFWRR service discipline serves the packets in a frame-based manner, by transmitting a fixed number of packets from each priority level according to a predefined weight and a rate controller. RFWRR service discipline can provide delay jitter bounds and diverse delay guarantees for different priority levels, by adjusting the frame size and the rate according to the traffic characteristics.