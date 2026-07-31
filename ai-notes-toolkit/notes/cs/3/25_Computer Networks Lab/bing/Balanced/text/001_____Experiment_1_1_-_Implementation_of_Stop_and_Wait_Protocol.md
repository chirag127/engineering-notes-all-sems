### Experiment 1.1 - Implementation of Stop and Wait Protocol

The stop and wait protocol is a flow control protocol that belongs to the data link layer. It is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time.

The main idea of the stop and wait protocol is that the sender will not send the next packet to the receiver until the acknowledgment of the previous packet is received. This ensures that the packets are delivered in order and without errors.

The steps involved in the implementation of the stop and wait protocol are:

- The sender sends a data packet to the receiver and starts a timer.
- The receiver receives the data packet and sends an acknowledgment (ACK) packet back to the sender.
- The sender receives the ACK packet and stops the timer. Then it sends the next data packet and repeats the process.
- If the sender does not receive the ACK packet within the timeout period, it assumes that the data packet or the ACK packet was lost and retransmits the data packet.

The stop and wait protocol has some advantages and disadvantages. Some of the advantages are:

- It is simple and easy to implement.
- It avoids the problem of buffer overflow at the receiver side, as the receiver can process one packet at a time.
- It ensures reliable and in-order delivery of data packets.

Some of the disadvantages are:

- It has low efficiency, as the sender has to wait for the ACK packet before sending the next packet. The efficiency of the stop and wait protocol is given by:

  Efficiency = Useful time / Total cycle time = Tt / (Tt + 2Tp) = 1 / (1 + 2a) [a = Tp/Tt]

  where Tt is the transmission time of a packet, Tp is the propagation delay of the channel, and a is the ratio of Tp to Tt.

- It does not utilize the full bandwidth of the channel, as the channel is idle during the waiting time of the sender.
- It is vulnerable to errors and delays in the channel, as a single lost or corrupted packet can cause retransmission of the same packet.