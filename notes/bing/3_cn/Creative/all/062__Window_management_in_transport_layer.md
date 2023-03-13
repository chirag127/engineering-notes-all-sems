### Window management in transport layer

- Window management is a technique used by the transport layer to control the flow of data between two end systems.
- Window management ensures that the sender does not overwhelm the receiver or the network with too many packets at once, and that the receiver can acknowledge the received packets in a timely manner.
- Window management also helps to improve the efficiency and reliability of data transmission by detecting and recovering from packet losses, errors, or delays.
- Window management can be implemented using two main methods: **stop-and-wait** and **sliding window**.

#### Stop-and-wait

- In stop-and-wait, the sender sends one packet at a time and waits for an acknowledgment from the receiver before sending the next packet.
- The sender maintains a **window size** of one, which means it can have only one unacknowledged packet in the network at any time.
- The receiver sends an acknowledgment for each packet it receives, and discards any duplicate packets.
- The sender uses a **timer** to detect packet losses or delays. If the timer expires before receiving an acknowledgment, the sender retransmits the packet.
- Stop-and-wait is simple and easy to implement, but it has low efficiency and throughput, especially for long-distance or high-speed networks, because the sender has to wait for a round-trip time (RTT) between each packet transmission.

#### Sliding window

- In sliding window, the sender can send multiple packets without waiting for acknowledgments, as long as the number of unacknowledged packets does not exceed the window size.
- The sender maintains a **sending window**, which is a range of sequence numbers of packets that can be sent at any time. The sender also keeps track of the **last acknowledgment received (LAR)** and the **last packet sent (LPS)**.
- The receiver maintains a **receiving window**, which is a range of sequence numbers of packets that can be received and acknowledged at any time. The receiver also keeps track of the **last packet received (LPR)** and the **largest acceptable packet (LAP)**.
- The receiver sends a **cumulative acknowledgment** for the last packet it received in order, and also indicates the size of its receiving window. The receiver can also use **selective acknowledgments** to inform the sender of specific packets that have been received out of order.
- The sender uses a timer to detect packet losses or delays. If the timer expires for a packet, the sender retransmits the packet and all subsequent packets in the sending window.
- Sliding window can be further classified into two types: **go-back-N** and **selective repeat**.

##### Go-back-N

- In go-back-N, the sender retransmits all the packets in the sending window when a packet loss or delay is detected.
- The sender uses a fixed window size of N, which is usually equal to the size of the receiver's window.
- The receiver discards any out-of-order packets and sends a cumulative acknowledgment for the last packet received in order.
- Go-back-N is simple and easy to implement, but it has low efficiency and reliability, especially for networks with high error rates, because it wastes bandwidth and time by retransmitting packets that have already been received by the receiver.

##### Selective repeat

- In selective repeat, the sender retransmits only the packets that have been lost or delayed when a packet loss or delay is detected.
- The sender uses a variable window size, which is usually smaller than the size of the receiver's window, to avoid sending too many packets at once.
- The receiver buffers any out-of-order packets and sends a selective acknowledgment for each packet received, indicating the sequence number and the size of its receiving window.
- Selective repeat is more complex and difficult to implement, but it has high efficiency and reliability, especially for networks with high error rates, because it avoids retransmitting packets that have already been received by the receiver.