## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

- Stop and wait protocol is a data link layer protocol that provides unidirectional data transmission over a noiseless channel.
- In this protocol, the sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender and the receiver use only two sequence numbers, 0 and 1, to identify the packets and avoid duplication.
- The efficiency of stop and wait protocol is low, as it depends on the ratio of propagation delay to transmission time.
- Sliding window protocol is a data link layer protocol that provides bidirectional data transmission over a noisy channel.
- In this protocol, the sender can send multiple packets without waiting for an acknowledgment, as long as the number of packets does not exceed the window size.
- The sender and the receiver use a sliding window to keep track of the sequence numbers of the packets that are sent, received, and acknowledged.
- The efficiency of sliding window protocol is high, as it utilizes the channel bandwidth more effectively.

: https://www.geeksforgeeks.org/stop-and-wait-arq/
: https://www.javatpoint.com/stop-and-wait-protocol
: https://www.scaler.com/topics/computer-network/stop-and-wait-protocol/
: https://www.geeksforgeeks.org/stop-and-wait-protocol-its-problems-and-solutions/
: https://www.javatpoint.com/sliding-window-protocol