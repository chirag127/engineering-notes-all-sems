# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) service discipline is a type of priority-based service discipline that assigns a weight to each priority queue and serves the queues in a circular order according to their weights .
- WRR does not require a sorted priority queue, only a round-robin queue, which reduces the complexity and overhead of the scheduler.
- WRR can guarantee both bandwidth and fairness among different priority queues, but it cannot guarantee the delay jitter bound or satisfy diverse delay requirements.
- To overcome the limitations of WRR, some variations have been proposed, such as:
  - Weighted fair queuing (WFQ), which assigns a virtual finish time to each packet based on its weight and serves the packets in increasing order of their virtual finish times.
  - Probabilistic priority (PP), which assigns a probability parameter to each priority queue and serves the queue with the highest probability when it is polled by the server.
  - Rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server, and adjusts the frame size and the weights of the queues according to the delay and jitter requirements of the packets.
  - Class-based weighted fair queuing (CBWFQ) and weighted fair priority queuing (WFPQ), which combine the features of WFQ and priority queuing to provide different service classes for different types of traffic.
- Priority-based service disciplines and WRR service discipline are suitable for real-time communication in switched networks, as they can provide quality of service (QoS) guarantees, such as bandwidth, delay, jitter and fairness, for different types of applications and users.