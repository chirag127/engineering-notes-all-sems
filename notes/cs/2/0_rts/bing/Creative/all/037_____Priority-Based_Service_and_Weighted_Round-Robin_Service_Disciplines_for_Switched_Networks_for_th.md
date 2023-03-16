# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Priority-based service disciplines can provide different delay and jitter bounds, bandwidth guarantees, and fairness properties for different classes of packets  .
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns a weight to each class of packets and serves them in a circular order according to their weights  .
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can guarantee the minimum bandwidth for each class of packets, but it cannot guarantee the maximum delay or jitter bound for each class of packets.
- WRR can also suffer from the problem of head-of-line blocking, where a large packet at the head of a queue can delay the transmission of smaller packets in the same queue.
- To overcome the limitations of WRR, some variations and extensions of WRR have been proposed, such as:
  - Weighted fair queuing (WFQ), which serves packets in proportion to their weights and lengths, and can provide delay and jitter bounds for each class of packets.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and can guarantee the delay jitter bound and satisfy diverse delay requirements for each class of packets.
  - Class-based weighted fair queuing (CBWFQ) and weighted fair priority queuing (WFPQ), which combine the features of WFQ and priority queuing, and can provide different service levels for different classes of packets.