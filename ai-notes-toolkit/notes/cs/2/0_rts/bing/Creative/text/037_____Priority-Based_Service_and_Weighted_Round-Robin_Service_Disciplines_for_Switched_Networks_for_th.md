### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Priority-based service disciplines can provide different delay and jitter bounds for different classes of packets, as well as guarantee bandwidth and fairness requirements.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns a weight to each queue and serves packets from each queue in a round-robin fashion according to their weights .
- WRR can be implemented without a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can also be combined with other techniques, such as rate control and frame-based scheduling, to improve the performance and flexibility of the service discipline.
- Some examples of WRR-based service disciplines are:
  - Weighted fair queuing (WFQ), which assigns weights to queues based on the packet arrival rates and the desired bandwidth allocation.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and guarantees the delay jitter bound and satisfies diverse delay requirements.
  - Class-based weighted fair queuing (CBWFQ), which extends WFQ to support multiple classes of traffic with different priority levels and bandwidth guarantees.
  - Weighted fair priority queuing (WFPQ), which combines WFQ and strict priority queuing to provide both bandwidth and priority guarantees to different classes of traffic.