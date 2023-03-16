# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a circular order based on their weights.
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of scheduling.
- WRR can guarantee both bandwidth and fairness requirements for different priority classes, but it may not satisfy the delay and jitter requirements for real-time communication.
- A variation of WRR is the rate-controlled frame-based WRR (RFWRR), which divides the scheduler into two components: a rate controller and a frame-based WRR server.
- The rate controller adjusts the weights of the priority classes based on their delay requirements and the network conditions, while the frame-based WRR server serves packets within a fixed frame size.
- RFWRR can guarantee the delay jitter bound and satisfy a diverse set of delay requirements for different priority classes, while maintaining the bandwidth and fairness properties of WRR.
- Another variation of WRR is the class-based WRR (CBWRR), which uses a hierarchical structure of priority classes and sub-classes, and applies WRR at each level.
- CBWRR can provide finer granularity and flexibility for differentiating the service quality of different priority classes and sub-classes, while preserving the bandwidth and fairness properties of WRR.
- Priority-based service disciplines, such as WRR and its variations, are suitable for switched networks that need to support real-time communication with different quality of service requirements .