### Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data stream into segments and assign sequence numbers to them.
- The sender maintains a window of segments that it can send without waiting for an acknowledgment from the receiver.
- The receiver maintains a window of segments that it can accept and acknowledge without buffering them.
- The size of the window depends on the available buffer space, the network congestion, and the reliability of the transmission.
- The sender and the receiver exchange window information using control messages, such as SYN, ACK, and FIN.
- The sender adjusts its window size based on the feedback from the receiver and the network conditions.
- The receiver adjusts its window size based on the available buffer space and the sequence numbers of the received segments.
- The sliding window technique is a common window management scheme that allows the sender and the receiver to move their windows along the data stream as segments are transmitted and acknowledged.
- The sliding window technique can be implemented using different algorithms, such as stop-and-wait, go-back-N, and selective repeat.