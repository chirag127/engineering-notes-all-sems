### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time. It is a simple protocol that allows the sender to send the next packet when the acknowledgment of the previous packet is received from the receiver. It is also known as a sliding window protocol with window size 1. It requires only two sequence numbers, 0 and 1, to distinguish between the packets.

The steps involved in the stop and wait protocol are:

- The sender sends a data packet to the receiver and starts a timer.
- The receiver receives the data packet and sends an acknowledgment (ACK) packet back to the sender.
- The sender receives the ACK packet and stops the timer. It then sends the next data packet and repeats the process.
- If the sender does not receive the ACK packet within the timeout period, it assumes that the data packet or the ACK packet was lost. It then retransmits the same data packet and restarts the timer.

The advantages of the stop and wait protocol are:

- It is easy to implement and understand.
- It ensures reliable data transmission over noiseless channels.
- It avoids congestion and buffer overflow at the receiver side.

The disadvantages of the stop and wait protocol are:

- It has low efficiency and throughput, as the sender has to wait for the ACK packet before sending the next data packet.
- It wastes the channel bandwidth and time, as the channel remains idle during the waiting period.
- It does not handle the case of duplicate packets, as the receiver cannot distinguish between the original and the retransmitted packets. This may lead to data corruption or duplication at the receiver side.