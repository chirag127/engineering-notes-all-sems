### Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data stream into segments and assign sequence numbers to each segment.
- The sender maintains a window of segments that it can send without waiting for an acknowledgment from the receiver. The window size is determined by the sender's buffer capacity and the receiver's advertised window.
- The receiver maintains a window of segments that it can accept and acknowledge. The window size is determined by the receiver's buffer capacity and the network congestion.
- The sender and receiver use the sequence numbers and acknowledgments to keep track of the segments that have been sent and received, and to adjust the window size accordingly.
- The window management technique ensures that the sender does not overwhelm the receiver or the network with too many segments, and that the receiver does not lose any segments or receive duplicate segments.
- The window management technique also enables the sender and receiver to detect and recover from errors, such as lost, corrupted, or reordered segments, by using timers, retransmissions, and cumulative or selective acknowledgments.
- There are different types of window management techniques, such as stop-and-wait, go-back-N, and selective repeat, that vary in the window size and the error recovery mechanism.