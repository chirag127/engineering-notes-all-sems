### Window management for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- Window management is a technique used by the transport layer protocols to control the flow of data between two end systems.
- The transport layer protocols, such as TCP, divide the data into segments and assign sequence numbers to them before sending them to the network layer.
- The receiver acknowledges the segments it receives and informs the sender about the next expected segment.
- The sender maintains a window, which is a range of sequence numbers that it can send without waiting for an acknowledgment.
- The receiver also maintains a window, which is a range of sequence numbers that it can accept without buffering.
- The sender adjusts its window size based on the feedback from the receiver and the network conditions, such as congestion and errors.
- The receiver adjusts its window size based on the available buffer space and the sender's window size.
- The window management technique ensures that the sender does not overwhelm the receiver or the network with too many segments, and that the receiver does not lose any segments or receive them out of order.
- There are different types of window management techniques, such as stop-and-wait, go-back-N, and selective repeat .
- Stop-and-wait is the simplest technique, where the sender sends one segment at a time and waits for an acknowledgment before sending the next one. The window size is one for both the sender and the receiver.
- Go-back-N is a technique where the sender can send multiple segments without waiting for acknowledgments, but the receiver can only acknowledge the last in-order segment it received. The sender's window size is N, and the receiver's window size is one. If the sender does not receive an acknowledgment within a timeout period, it retransmits all the segments in its window.
- Selective repeat is a technique where the sender can send multiple segments without waiting for acknowledgments, and the receiver can acknowledge any segment it receives. The sender's and the receiver's window sizes are both N. If the sender does not receive an acknowledgment for a segment within a timeout period, it retransmits only that segment. The receiver uses a buffer to store the out-of-order segments until the missing ones arrive.