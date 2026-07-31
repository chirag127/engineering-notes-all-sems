### Flow Control and Retransmission

Flow control and retransmission are two important mechanisms used in the transport layer of computer networks to ensure reliable data transmission.

#### Flow Control
Flow control is the process of managing the rate of data transmission between two nodes to prevent a fast sender from overwhelming a slow receiver. This is achieved by using various flow control techniques such as:
- **Stop-and-wait**: The sender sends one packet and waits for an acknowledgment from the receiver before sending the next packet.
- **Sliding window**: The sender can send multiple packets without waiting for an acknowledgment, but the number of unacknowledged packets is limited by the size of the window.

#### Retransmission
Retransmission is the process of re-sending packets that have been lost or corrupted during transmission. This is achieved by using various retransmission techniques such as:
- **Automatic Repeat reQuest (ARQ)**: The sender retransmits a packet if it does not receive an acknowledgment from the receiver within a certain time period.
- **Selective Repeat**: Only the lost or corrupted packets are retransmitted, rather than retransmitting all packets since the last acknowledgment.

These mechanisms work together to ensure reliable data transmission in the transport layer of computer networks. They are essential for applications that require reliable data transmission, such as file transfers and streaming media.