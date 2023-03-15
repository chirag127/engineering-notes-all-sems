### Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data stream into segments and assign sequence numbers to each segment.
- The sender maintains a window of segments that it can send without waiting for an acknowledgment from the receiver. The window size is determined by the sender's buffer capacity and the receiver's advertised window.
- The receiver maintains a window of segments that it can accept and acknowledge. The window size is determined by the receiver's buffer capacity and the network congestion.
- The sender and the receiver use the sequence numbers and the acknowledgments to keep track of the segments that have been sent and received, and to adjust the window size accordingly.
- The sliding window technique is a common window management method that allows the sender and the receiver to move their windows along the data stream as segments are transmitted and acknowledged.
- The sliding window technique can be implemented in different ways, such as stop-and-wait, go-back-N, and selective repeat, depending on the error recovery and retransmission strategies.
- The sliding window technique can improve the efficiency and reliability of data transmission by avoiding buffer overflow, underutilization, and duplicate segments.