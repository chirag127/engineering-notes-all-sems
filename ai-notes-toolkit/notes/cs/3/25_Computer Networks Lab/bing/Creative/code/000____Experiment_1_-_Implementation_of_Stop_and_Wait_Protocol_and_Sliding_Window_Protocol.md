# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Stop and Wait Protocol

- Stop and wait protocol is a data link layer protocol that provides unidirectional data transmission over a noiseless channel.
- In this protocol, the sender sends one data packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender and the receiver use two sequence numbers, 0 and 1, to identify the data packets and the acknowledgments.
- The sender sets a timer for each packet it sends and retransmits the packet if the timer expires before receiving an acknowledgment.
- The efficiency of stop and wait protocol is low, as the sender remains idle for most of the time waiting for acknowledgments.
- The efficiency of stop and wait protocol can be calculated as:

  - Efficiency = Useful time / Total cycle time = Tt / (Tt + 2Tp)
  - Where Tt is the transmission time of a packet, and Tp is the propagation delay of the channel.
  - The efficiency decreases as the propagation delay increases compared to the transmission time.

## Sliding Window Protocol

- Sliding window protocol is a data link layer protocol that provides bidirectional data transmission over a noisy channel.
- In this protocol, the sender can send multiple data packets without waiting for acknowledgments, as long as the number of packets does not exceed the window size.
- The window size is the maximum number of packets that can be sent or received at a time.
- The sender and the receiver use sequence numbers to identify the data packets and the acknowledgments, and maintain a send window and a receive window respectively.
- The send window and the receive window slide along the sequence number space as the sender and the receiver exchange data packets and acknowledgments.
- The sender sets a timer for each packet it sends and retransmits the packet if the timer expires before receiving an acknowledgment.
- The efficiency of sliding window protocol is high, as the sender can utilize the channel bandwidth more effectively by sending multiple packets at a time.
- The efficiency of sliding window protocol can be calculated as:

  - Efficiency = Window size / (1 + 2a)
  - Where a is the ratio of propagation delay to transmission time.
  - The efficiency increases as the window size increases or the propagation delay decreases compared to the transmission time.