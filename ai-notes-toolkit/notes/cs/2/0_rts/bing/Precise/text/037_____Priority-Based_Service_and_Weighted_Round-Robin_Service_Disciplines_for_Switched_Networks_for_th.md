### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- According to a priority-based service discipline, the transmission of ready packets is scheduled in a priority-driven manner. 
- Waited fair queuing (WFQ) and Waited round-robin scheduling are common approaches for scheduling the packets in real-time communication networks .
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion. It does not have to wait for the arrival of the rest of the message .
- The weighted round-robin approach does not require a sorted priority queue, only a round-robin queue .
- Queue service disciplines are used to determine service priority, delay bound, jitter bound, and bandwidth .
- Among them, the Weighted Round Robin (WRR) technique has provided the most reasonable performance in guaranteeing both bandwidth and fairness requirements .
- A new WRR algorithm, called Rate-controlled Frame-based Weighted Round Robin (RFWRR), guarantees the delay jitter bound and satisfies a diverse set of delay requirements .
- Many class service disciplines used for output queued switches have been proposed in the literature. These disciplines include the Class-Based Weighted Fair Queuing (CBWFQ) and the Weighted Fair Priority Queuing (WFPQ) techniques .