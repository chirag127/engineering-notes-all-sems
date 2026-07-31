# Flow Control and Retransmission

Flow control and retransmission are two important mechanisms used in the transport layer of computer networks to ensure reliable data transmission.

## Flow Control

Flow control is the process of managing the rate of data transmission between two nodes to prevent a fast sender from overwhelming a slow receiver. This is achieved by using various flow control techniques, such as:

- **Stop-and-wait**: In this technique, the sender sends one packet and waits for an acknowledgment from the receiver before sending the next packet.

- **Sliding window**: In this technique, the sender can send multiple packets without waiting for an acknowledgment, but the number of unacknowledged packets is limited by the size of the window.

## Retransmission

Retransmission is the process of re-sending packets that have been lost or corrupted during transmission. This is achieved by using various retransmission techniques, such as:

- **Automatic Repeat reQuest (ARQ)**: In this technique, the sender waits for an acknowledgment from the receiver for each packet sent. If the acknowledgment is not received within a certain time period, the sender assumes that the packet has been lost and retransmits it.

- **Selective Repeat**: In this technique, the receiver sends a negative acknowledgment for any packet that is lost or corrupted. The sender then retransmits only the lost or corrupted packets.

These mechanisms help ensure reliable data transmission in the transport layer of computer networks. They are essential for maintaining the integrity and efficiency of data communication.