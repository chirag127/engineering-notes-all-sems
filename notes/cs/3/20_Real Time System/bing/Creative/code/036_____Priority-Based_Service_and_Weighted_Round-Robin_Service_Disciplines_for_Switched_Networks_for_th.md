### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a network according to their priority levels, delay bounds, jitter bounds and bandwidth requirements.
- Weighted round-robin (WRR) is a simple and fair priority-based service discipline that assigns a weight to each queue and serves them in a circular order, proportional to their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee the bandwidth and fairness requirements, but it cannot guarantee the delay jitter bound and it may not satisfy diverse delay requirements.
- A variation of WRR is the rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into two components: a rate controller and a frame-based WRR server.
- The rate controller adjusts the weights of the queues according to the arrival rates of the packets and the delay requirements of each queue.
- The frame-based WRR server serves the packets in a frame-based manner, where a frame is a fixed number of bytes that can be transmitted in one round.
- RFWRR can guarantee the delay jitter bound and satisfy diverse delay requirements, as well as the bandwidth and fairness requirements.
- Another variation of WRR is the probabilistic priority (PP) discipline, which assigns a parameter to each queue that determines the probability of serving the queue when it is polled by the server.
- The PP discipline is based on the strict priority (SP) discipline, but it allows lower priority queues to be served with some probability, thus avoiding starvation and improving fairness.
- The PP discipline can also achieve a trade-off between delay and throughput performance by adjusting the parameters of the queues.
- Other priority-based service disciplines include the class-based weighted fair queuing (CBWFQ) and the weighted fair priority queuing (WFPQ) techniques, which use a combination of fair queuing and priority queuing to provide different service classes for different types of traffic.