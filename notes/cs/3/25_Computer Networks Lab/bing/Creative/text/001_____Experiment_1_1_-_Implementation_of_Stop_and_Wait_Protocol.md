### Experiment 1.1 - Implementation of Stop and Wait Protocol

- The stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels.
- It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time.
- It is a special category of sliding window protocol where the window size is 1 .
- It requires only two sequence numbers, 0 and 1, to distinguish between the packets.
- The sender sends a data packet and waits for an acknowledgment from the receiver before sending the next packet.
- The receiver sends an acknowledgment after receiving a data packet and waits for the next packet.
- The sender and the receiver use timers to detect and handle lost or corrupted packets .
- The efficiency of the stop and wait protocol is low, as the sender remains idle for most of the time.
- The efficiency can be calculated as: Efficiency = Tt / (Tt + 2Tp), where Tt is the transmission time and Tp is the propagation time.