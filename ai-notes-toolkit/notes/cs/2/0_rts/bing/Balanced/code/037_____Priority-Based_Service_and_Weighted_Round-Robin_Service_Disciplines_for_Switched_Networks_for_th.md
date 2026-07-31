### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

- Priority-based service disciplines are used to schedule the transmission of packets in a switched network according to their priority levels.
- Weighted round-robin (WRR) is a common priority-based service discipline that assigns different weights to different priority classes and serves packets in a circular order based on their weights.
- WRR does not require a sorted priority queue, only a round-robin queue.
- WRR can guarantee bandwidth and fairness requirements, but it cannot guarantee delay and jitter bounds for different classes of packets.
- A variation of WRR is weighted fair queuing (WFQ), which assigns different weights to different flows of packets and serves packets in a proportional fair manner based on their weights and arrival times.
- WFQ can guarantee delay and jitter bounds for different flows of packets, but it requires more computation and memory than WRR.
- Another variation of WRR is rate-controlled frame-based weighted round-robin (RFWRR), which divides the scheduler into a rate controller and a frame-based WRR server.
- RFWRR can guarantee delay jitter bounds and satisfy diverse delay requirements for different classes of packets, but it requires more complexity and overhead than WRR.
- A different priority-based service discipline is class-based weighted fair queuing (CBWFQ), which combines WFQ and priority queuing to provide different service levels for different classes of packets.
- CBWFQ can guarantee bandwidth, delay, and jitter bounds for different classes of packets, but it requires more computation and memory than WRR.
- Another different priority-based service discipline is weighted fair priority queuing (WFPQ), which combines WFQ and strict priority queuing to provide different service levels for different classes of packets.
- WFPQ can guarantee bandwidth, delay, and jitter bounds for different classes of packets, but it requires more computation and memory than WRR and may cause starvation for low-priority packets.