### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a flow control protocol that is used in data communication. It is a simple protocol that is used to ensure that the sender does not overwhelm the receiver with data. The sender sends a single data packet and then waits for an acknowledgment from the receiver before sending the next packet. This protocol is used in situations where the transmission time is much larger than the propagation delay.

The steps involved in the implementation of the Stop and Wait Protocol are as follows:

1. The sender sends a data packet to the receiver.
2. The sender starts a timer and waits for an acknowledgment from the receiver.
3. If the acknowledgment is received before the timer expires, the sender sends the next data packet.
4. If the acknowledgment is not received before the timer expires, the sender retransmits the data packet.
5. The process is repeated until all the data packets have been transmitted.

This protocol is simple to implement but has some drawbacks. The main drawback is that the sender has to wait for an acknowledgment before sending the next packet, which can result in low throughput. Additionally, if the acknowledgment is lost, the sender will retransmit the data packet, which can result in duplicate packets being received by the receiver.

Overall, the Stop and Wait Protocol is a simple and effective flow control protocol that is used in data communication. However, it may not be the most efficient protocol in all situations.