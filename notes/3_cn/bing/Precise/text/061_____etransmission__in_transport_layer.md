### etransmission in transport layer

- The transport layer is responsible for ensuring that the entire message arrives at the receiving transport layer without any error (damage, loss or duplication) .
- Error Correction is achieved through retransmission of the packet .
- The transport layer checks whether the data has arrived or not and checks for the integrity of data .
- It uses the ACK and NACK services to inform the sender .
- Retransmission of lost packets is provided by both TCP and UDP .
- The transport layer enables a fast process to keep pace with a slow one .
- Acknowledgements are sent back to manage end-to-end flow control .
- Go back N algorithms are used to request retransmission of packets starting with packet number N .
- Selective Repeat is used to request specific packets to be retransmitted .
- The Transmission Control Protocol (TCP) is a transport protocol that is used on top of IP to ensure reliable transmission of packets .
- TCP includes mechanisms to solve many of the problems that arise from packet-based messaging, such as lost packets, out of order packets, duplicate packets, and corrupted packets .