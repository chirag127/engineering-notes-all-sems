### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a round-robin fashion according to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee both bandwidth and fairness requirements, but it may not satisfy the delay and jitter requirements of real-time packets.
- A variation of WRR is the rate-controlled frame-based WRR (RFWRR), which divides the scheduler into two components: a rate controller and a frame-based WRR server.
- The rate controller adjusts the weights of the priority classes based on their delay requirements and the network conditions.
- The frame-based WRR server serves packets in fixed-size frames, where each frame consists of a number of slots proportional to the weights of the priority classes.
- RFWRR can guarantee the delay jitter bound and satisfy a diverse set of delay requirements for real-time packets.
- Other priority-based service disciplines include the class-based weighted fair queuing (CBWFQ) and the weighted fair priority queuing (WFPQ), which use different algorithms to allocate bandwidth and priority to different classes of packets.