# Flow control and retransmission for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- The transport layer is the fourth layer of the OSI model that provides end-to-end communication services for applications.
- The transport layer ensures the reliable arrival of messages across a network and provides error-checking mechanisms and data flow controls.
- Flow control is the process of regulating the rate of data transmission between two nodes to prevent data loss or congestion  .
- Flow control can be performed at the sender side, the receiver side, or both, depending on the protocol used.
- Some of the common flow control techniques are:
  - Stop-and-wait: The sender sends one packet and waits for an acknowledgment from the receiver before sending the next packet.
  - Sliding window: The sender and the receiver maintain a window of packets that can be sent or received without waiting for an acknowledgment. The window size can be fixed or variable.
  - Flow control using TCP: TCP uses a combination of sliding window and congestion control algorithms to adjust the window size dynamically based on the network conditions.
- Retransmission is the process of resending packets that are corrupted, lost, or delayed in the network.
- Retransmission can be triggered by different events, such as:
  - Timeout: The sender sets a timer for each packet and retransmits the packet if the timer expires before receiving an acknowledgment from the receiver.
  - Duplicate acknowledgment: The receiver sends an acknowledgment for the last packet received in order. If the sender receives multiple acknowledgments for the same packet, it indicates that some packets are missing and need to be retransmitted.
  - Selective acknowledgment: The receiver sends an acknowledgment for a range of packets received, not just the last one. This allows the sender to know which packets are missing and retransmit only those packets.
  - Retransmission using TCP: TCP uses a combination of timeout, duplicate acknowledgment, and selective acknowledgment to detect and recover from packet losses. TCP also uses fast retransmit and fast recovery algorithms to reduce the retransmission delay and avoid unnecessary timeouts.