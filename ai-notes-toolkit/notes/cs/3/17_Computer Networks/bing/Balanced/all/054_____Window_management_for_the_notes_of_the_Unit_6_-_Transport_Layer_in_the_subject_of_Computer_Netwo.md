# Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data stream into segments and assign sequence numbers to each segment.
- The sender maintains a window of segments that it can send without waiting for an acknowledgment from the receiver. The window size is determined by the available buffer space at the receiver and the network congestion level.
- The receiver maintains a window of segments that it can accept and acknowledge. The window size is determined by the available buffer space at the receiver and the network delay.
- The sender and the receiver exchange window information using control messages, such as SYN, ACK, and FIN.
- The sender slides its window forward when it receives an acknowledgment from the receiver for the segments it has sent. The sender can then send more segments from its window.
- The receiver slides its window forward when it receives segments from the sender that are in order and within its window. The receiver can then accept and acknowledge more segments from the sender.
- The sliding window technique ensures that the sender and the receiver are synchronized and that the data is transmitted reliably and efficiently.