# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Stop and Wait Protocol

- Stop and wait protocol is a data link layer protocol that provides unidirectional data transmission over a noiseless channel.
- In this protocol, the sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender and the receiver use a sliding window of size 1, which means they can only send or receive one packet at a time.
- The sender and the receiver use two sequence numbers, 0 and 1, to identify the packets and avoid duplication.
- The efficiency of stop and wait protocol is low, as the sender has to wait for the round trip time (RTT) of each packet, which is the time taken for a packet to travel from the sender to the receiver and back.
- The efficiency of stop and wait protocol is given by:

  Efficiency = Useful time / Total cycle time = Tt / (Tt + 2Tp) = 1 / (1 + 2a) [a = Tp/Tt]

  where Tt is the transmission time of a packet, Tp is the propagation delay of the channel, and a is the ratio of Tp to Tt.

## Sliding Window Protocol

- Sliding window protocol is a data link layer protocol that provides bidirectional data transmission over a noisy channel.
- In this protocol, the sender can send multiple packets without waiting for an acknowledgment from the receiver, as long as the number of packets does not exceed the window size.
- The window size is the maximum number of packets that can be sent or received at a time, and it is determined by the bandwidth-delay product of the channel.
- The sender and the receiver use sequence numbers to identify the packets and acknowledge them, and they use a sliding window to keep track of the packets that are in transit or have been received.
- The efficiency of sliding window protocol is high, as the sender can utilize the channel capacity by sending multiple packets in a single RTT.
- The efficiency of sliding window protocol is given by:

  Efficiency = Window size / (1 + 2a) [a = Tp/Tt]

  where window size is the number of packets that can be sent or received at a time, and a is the ratio of Tp to Tt.

## References

: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.javatpoint.com/stop-and-wait-protocol
: https://www.scaler.com/topics/computer-network/stop-and-wait-protocol/
: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.geeksforgeeks.org/stop-and-wait-protocol-its-problems-and-solutions/
: https://www.javatpoint.com/sliding-window-protocol