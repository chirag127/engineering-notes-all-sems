#### Elementary Data Link Protocols in link layer in Computer Networks

The data link layer is responsible for providing reliable data transfer between two adjacent nodes in a network. This layer is responsible for framing, flow control, error control, and media access control. The data link layer is divided into two sublayers: the Logical Link Control (LLC) and the Media Access Control (MAC).

Elementary Data Link Protocols are the basic protocols used in the data link layer to provide reliable data transfer. Some of the commonly used Elementary Data Link Protocols are:

1. **Stop-and-Wait ARQ**: This protocol uses a stop-and-wait mechanism for flow control and error control. In this protocol, the sender sends a frame and waits for an acknowledgment from the receiver before sending the next frame. If the acknowledgment is not received within a specified time, the sender retransmits the frame.

2. **Go-Back-N ARQ**: This protocol uses a sliding window mechanism for flow control and error control. In this protocol, the sender can send multiple frames without waiting for an acknowledgment, but the number of unacknowledged frames cannot exceed the window size. If an error is detected, the sender retransmits all the frames starting from the erroneous frame.

3. **Selective Repeat ARQ**: This protocol also uses a sliding window mechanism for flow control and error control. In this protocol, the sender can send multiple frames without waiting for an acknowledgment, but the number of unacknowledged frames cannot exceed the window size. If an error is detected, the sender only retransmits the erroneous frame.

These protocols have their own advantages and disadvantages. For example, the Stop-and-Wait ARQ protocol is simple to implement but has low efficiency due to the waiting time. The Go-Back-N ARQ protocol has higher efficiency but may result in the retransmission of correctly received frames. The Selective Repeat ARQ protocol has the highest efficiency but is more complex to implement.

A mnemonic to remember these protocols is **"Stop, Go back, Selectively Repeat"**. This can help you remember the order and names of the protocols.

These protocols are used in various applications such as wireless networks, satellite communication, and computer networks. They are essential for providing reliable data transfer in these networks.