### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- According to a priority-based service discipline, the transmission of ready packets is scheduled in a priority-driven manner. 
- Weighted Fair Queuing (WFQ) and Weighted Round Robin (WRR) scheduling are common approaches for scheduling packets in real-time communication networks .
- The PP discipline is based on the Strict Priority (SP) discipline with the difference that each priority queue is assigned a parameter as in Weighted Fair Queueing (WFQ) and Weighted Round Robin (WRR) disciplines .
- In a switched network, a downstream switch can begin to transmit an earlier portion of the message as soon as it receives the portion. It does not have to wait for the arrival of the rest of the message .
- The weighted round-robin approach does not require a sorted priority queue, only a round-robin queue .
- Many class service disciplines used for output queued switches have been proposed in the literature. These disciplines include the Class-Based Weighted Fair Queuing (CBWFQ) and the Weighted Fair Priority Queuing (WFPQ) techniques .
- A new WRR algorithm, called Rate-controlled Frame-based Weighted Round Robin (RFWRR) has been proposed which guarantees the delay jitter bound and satisfies a diverse set of delay requirements. The proposed algorithm divides the scheduler into two components: a rate controller and a frame-based WRR server .