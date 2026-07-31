### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, proportional to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue. It can guarantee the minimum bandwidth for each queue and avoid starvation of low-priority queues.
- However, WRR cannot provide strict delay and jitter bounds for different classes of packets, as it does not consider the packet size or arrival rate.
- To overcome this limitation, some variants of WRR have been proposed, such as:
  - Rate-controlled frame-based WRR (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server. The rate controller adjusts the weights of the queues according to their delay requirements, and the frame-based WRR server serves the packets within a fixed frame size.
  - Probabilistic priority (PP) scheduling, which assigns a parameter to each priority queue that determines the probability of serving the queue when it is polled by the server. The parameter can be adjusted dynamically to balance the trade-off between fairness and priority.
  - Class-based WRR (CBWRR), which groups the queues into different classes and applies WRR within each class. The classes are served according to their priority levels, and the weights of the queues within each class can be changed to achieve different service objectives.
- These variants of WRR can provide better performance than the basic WRR in terms of delay, jitter, fairness and bandwidth allocation for different classes of packets in a switched network.