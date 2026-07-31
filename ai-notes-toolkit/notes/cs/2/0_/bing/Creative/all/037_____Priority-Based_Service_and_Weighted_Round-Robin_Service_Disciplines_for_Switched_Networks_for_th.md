# Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- In real-time communication networks, packets need to be transmitted with certain quality of service (QoS) guarantees, such as delay, jitter, throughput, and loss rate.
- Priority-based service disciplines are a class of scheduling algorithms that assign different priorities to different packets or flows, and serve them according to their priority levels.
- Weighted round-robin (WRR) service disciplines are a class of scheduling algorithms that assign different weights to different packets or flows, and serve them in a circular order with a proportion of the server capacity proportional to their weights.
- Both priority-based and WRR service disciplines can be used to achieve QoS differentiation and fairness among different packets or flows in switched networks, such as routers, switches, and multiplexers.

## Priority-Based Service Disciplines

- According to a priority-based service discipline, the transmission of ready packets are scheduled in a priority-driven manner. The packets or flows with higher priority are served before the packets or flows with lower priority.
- Priority-based service disciplines can be classified into two types: strict priority (SP) and weighted fair queuing (WFQ).
- SP discipline serves the packets or flows in the order of their priority levels, without any regard to their arrival times or sizes. SP discipline can achieve the highest QoS for the highest priority packets or flows, but it may starve the lower priority packets or flows if the higher priority traffic is heavy or bursty.
- WFQ discipline serves the packets or flows in a weighted order of their virtual finish times, which are calculated based on their arrival times, sizes, and weights. WFQ discipline can achieve both QoS differentiation and fairness among different packets or flows, by giving more service to the higher priority packets or flows, but also guaranteeing a minimum service to the lower priority packets or flows.

## Weighted Round-Robin Service Disciplines

- According to a WRR service discipline, the transmission of ready packets are scheduled in a circular order, with each packet or flow getting a share of the server capacity proportional to its weight. The packets or flows with higher weights are served more frequently and for longer durations than the packets or flows with lower weights.
- WRR service disciplines can be classified into two types: simple WRR (SWRR) and frame-based WRR (FWRR).
- SWRR discipline serves the packets or flows in a circular order, with each packet or flow getting a fixed number of bytes or slots per round. SWRR discipline can achieve QoS differentiation among different packets or flows, by giving more service to the higher weight packets or flows, but it may cause large delay jitter and unfairness if the packet or flow sizes are variable or bursty.
- FWRR discipline serves the packets or flows in a circular order, with each packet or flow getting a fixed amount of time or rate per round. FWRR discipline can achieve both QoS differentiation and fairness among different packets or flows, by giving more service to the higher weight packets or flows, but also guaranteeing a maximum delay jitter and a minimum service rate to the lower weight packets or flows.