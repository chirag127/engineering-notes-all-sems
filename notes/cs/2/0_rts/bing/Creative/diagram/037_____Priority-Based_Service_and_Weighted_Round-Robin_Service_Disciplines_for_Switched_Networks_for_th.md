### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) service disciplines are used to allocate bandwidth and fairness among different classes of packets in a switched network.
- The main differences between priority-based and WRR service disciplines are:

  - Priority-based service disciplines use a sorted priority queue to store the packets, while WRR service disciplines use a round-robin queue .
  - Priority-based service disciplines may cause starvation of low-priority packets, while WRR service disciplines may cause violation of delay and jitter bounds of high-priority packets.
  - Priority-based service disciplines are suitable for real-time communication with strict delay and jitter requirements, while WRR service disciplines are suitable for non-real-time communication with flexible delay and jitter requirements.

- Some examples of priority-based service disciplines are:

  - Weighted fair queuing (WFQ), which assigns a weight to each packet based on its priority and length, and serves the packets in order of their weighted finish times.
  - Weighted fair priority queuing (WFPQ), which combines WFQ and priority queuing, and serves the packets in order of their weighted finish times within each priority class.

- Some examples of WRR service disciplines are:

  - Frame-based WRR (FWRR), which divides the packets into frames of equal size, and serves one packet from each class in a round-robin fashion within each frame.
  - Rate-controlled frame-based WRR (RFWRR), which extends FWRR by adding a rate controller that adjusts the frame size according to the delay and jitter requirements of each class.