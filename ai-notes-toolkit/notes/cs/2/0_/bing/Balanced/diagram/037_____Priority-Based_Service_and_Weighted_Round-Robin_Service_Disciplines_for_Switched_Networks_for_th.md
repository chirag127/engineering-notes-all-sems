### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different packets or flows in a network and serve them accordingly.
- Weighted round-robin (WRR) service discipline is a type of priority-based service discipline that assigns different weights to different queues and serves them in a circular order with a proportionate number of packets from each queue.
- The advantages of priority-based service disciplines are that they can provide different levels of quality of service (QoS) to different applications or users, such as delay, jitter, throughput, and loss rate.
- The disadvantages of priority-based service disciplines are that they can cause starvation or unfairness to lower-priority packets or flows, especially when the network is congested or the higher-priority packets or flows are bursty.
- The advantages of WRR service discipline are that it can avoid starvation and provide some degree of fairness to lower-priority packets or flows, while still maintaining the QoS differentiation among different queues.
- The disadvantages of WRR service discipline are that it can introduce additional delay and jitter to higher-priority packets or flows, and that it can be difficult to determine the optimal weights for different queues.
- Some examples of priority-based service disciplines are:
  - Strict priority (SP) service discipline, which serves the highest-priority queue first and only serves the lower-priority queues when the higher-priority queues are empty.
  - Weighted fair queuing (WFQ) service discipline, which assigns different weights to different flows and serves them in a fair manner according to their weights and arrival times.
  - Probabilistic priority (PP) service discipline, which assigns different probabilities to different queues and serves them randomly according to their probabilities when they are polled by the server.
  - Class-based weighted fair queuing (CBWFQ) service discipline, which combines WFQ and SP by dividing the flows into different classes and applying WFQ within each class and SP among different classes.
  - Weighted fair priority queuing (WFPQ) service discipline, which combines WFQ and SP by applying WFQ among different priority levels and SP within each priority level.
- Some examples of WRR service disciplines are:
  - Round-robin (RR) service discipline, which assigns equal weights to all queues and serves them in a circular order with one packet from each queue.
  - Deficit round-robin (DRR) service discipline, which assigns different weights to different queues and serves them in a circular order with a variable number of packets from each queue based on their weights and deficits.
  - Frame-based weighted round-robin (FWRR) service discipline, which assigns different weights to different queues and serves them in a circular order with a fixed number of packets from each queue within a frame.
  - Rate-controlled frame-based weighted round-robin (RFWRR) service discipline, which assigns different weights to different queues and serves them in a circular order with a variable number of packets from each queue within a frame based on their weights and rates.