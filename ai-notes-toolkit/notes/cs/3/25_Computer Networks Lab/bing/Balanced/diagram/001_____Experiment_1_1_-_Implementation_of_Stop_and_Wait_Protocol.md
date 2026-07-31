### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that ensures reliable data transmission over a noisy channel. It works as follows:

- The sender sends one data packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The receiver sends an acknowledgment after receiving a data packet without any error. If the packet is corrupted or lost, the receiver does not send any acknowledgment.
- The sender uses a timer to detect the timeout of an acknowledgment. If the timer expires, the sender assumes that the packet or the acknowledgment was lost and retransmits the same packet.
- The sender and the receiver use sequence numbers to distinguish between new and retransmitted packets. The sequence numbers alternate between 0 and 1.

The following diagram shows the implementation of the stop and wait protocol:

![stop and wait protocol diagram](https://www.geeksforgeeks.org/wp-content/uploads/stop-and-wait-protocol.png)

The following are the steps to perform the experiment:

- Set up a network simulator such as NS2 or OPNET to create a sender node, a receiver node, and a channel with some error rate and propagation delay.
- Write a program for the sender node that implements the stop and wait protocol. The program should send data packets with sequence numbers and wait for acknowledgments with timers. The program should also handle timeout and retransmission events.
- Write a program for the receiver node that implements the stop and wait protocol. The program should receive data packets and check for errors. The program should also send acknowledgments with sequence numbers and discard duplicate packets.
- Run the simulation and observe the data transmission and reception. Measure the throughput, efficiency, and delay of the protocol. Compare the results with the theoretical values. Analyze the effect of error rate and propagation delay on the performance of the protocol.