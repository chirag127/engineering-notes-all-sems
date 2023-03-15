### Priority-Based Service and Weighted Round-Robin Service Disciplines for Switched Networks

#### Priority-Based Service
- In a priority-based service discipline, packets are assigned a priority level based on their importance.
- Packets with higher priority are transmitted before packets with lower priority.
- This can be useful in real-time communication where certain packets, such as voice or video, may need to be transmitted with minimal delay.

#### Weighted Round-Robin Service
- In a weighted round-robin service discipline, packets are transmitted in a round-robin fashion, but with different weights assigned to different queues.
- Queues with higher weights are given more opportunities to transmit their packets.
- This can be useful in situations where certain traffic flows need to be given higher priority, but not at the expense of completely starving other traffic flows.

These service disciplines can be used in switched networks to improve the performance of real-time communication. They can help ensure that time-sensitive packets are transmitted with minimal delay, while still providing fair access to the network for other traffic flows.