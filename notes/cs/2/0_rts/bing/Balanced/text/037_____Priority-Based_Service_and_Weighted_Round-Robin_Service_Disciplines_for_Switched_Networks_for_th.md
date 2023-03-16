### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are scheduling algorithms that assign different priorities to different classes of packets in a switched network, such as a router or a switch.
- The packets with higher priority are transmitted before the packets with lower priority, according to some predefined order or policy.
- Priority-based service disciplines can improve the quality of service (QoS) for real-time communication, such as voice or video, by reducing the delay and jitter of the packets.
- However, priority-based service disciplines can also cause starvation or unfairness for the packets with lower priority, especially when the network is congested or overloaded.
- Weighted round-robin (WRR) is a simple and popular priority-based service discipline that can provide some degree of fairness and differentiation among different classes of packets.
- WRR assigns a weight to each priority queue, which determines the number of packets or bytes that can be transmitted from that queue in each round.
- WRR cycles through the non-empty priority queues in a circular order, and transmits a fixed amount of packets or bytes from each queue, according to its weight, before moving to the next queue.
- WRR can guarantee a minimum bandwidth allocation for each priority queue, and can also accommodate different packet sizes and arrival rates.
- However, WRR can also introduce large delay and jitter variations for the packets, especially when the weights are not proportional to the traffic demands or the packet sizes of each priority queue.
- Moreover, WRR can be inefficient or unfair when some priority queues are empty or underutilized, as it wastes the transmission opportunities or bandwidth that could be used by other queues.
- To overcome these limitations, several variants or extensions of WRR have been proposed, such as weighted fair queuing (WFQ), class-based weighted fair queuing (CBWFQ), weighted fair priority queuing (WFPQ), and rate-controlled frame-based weighted round robin (RFWRR).
- These algorithms aim to provide better QoS guarantees, such as delay bounds, jitter bounds, or proportional fairness, for different classes of packets, by using more sophisticated mechanisms, such as virtual time, virtual finish time, rate control, or frame size, to schedule the packets.