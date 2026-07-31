# Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

## Stop and Wait Protocol
- Stop and Wait Protocol is a flow control protocol.
- It is used in data communication to prevent the sender from overwhelming the receiver with data.
- In this protocol, the sender sends a single data packet and waits for an acknowledgment from the receiver before sending the next packet.
- If the acknowledgment is not received within a certain time frame, the sender assumes that the packet was lost and retransmits it.
- This protocol is simple to implement but can be inefficient in terms of data transmission speed.

## Sliding Window Protocol
- Sliding Window Protocol is another flow control protocol.
- It is an improvement over the Stop and Wait Protocol as it allows the sender to transmit multiple packets before waiting for an acknowledgment.
- The sender maintains a window of packets that can be sent without waiting for an acknowledgment.
- The size of the window determines the number of packets that can be sent at once.
- As the receiver acknowledges the receipt of packets, the window slides forward, allowing the sender to transmit more packets.
- This protocol is more efficient than the Stop and Wait Protocol in terms of data transmission speed.