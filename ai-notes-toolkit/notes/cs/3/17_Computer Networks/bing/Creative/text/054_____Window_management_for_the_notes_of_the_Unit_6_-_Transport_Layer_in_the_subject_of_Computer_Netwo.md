### Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data into segments and assign sequence numbers to them before sending them to the network layer.
- The receiver acknowledges the segments that it receives and informs the sender about the next expected segment.
- The sender maintains a window, which is a range of sequence numbers that it can send without waiting for an acknowledgment.
- The receiver also maintains a window, which is a range of sequence numbers that it can accept without buffering.
- The sender adjusts its window size based on the feedback from the receiver and the network conditions, such as congestion and errors.
- The receiver adjusts its window size based on its buffer availability and the sender's window size.
- The window management technique ensures that the sender does not overwhelm the receiver or the network with too many segments, and that the receiver does not lose any segments or receive them out of order.
- The window management technique can be implemented using different algorithms, such as stop-and-wait, go-back-N, and selective repeat.