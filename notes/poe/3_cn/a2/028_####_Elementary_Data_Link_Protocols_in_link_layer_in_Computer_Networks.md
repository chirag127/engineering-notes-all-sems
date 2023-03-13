 Here is the content in markdown format on the topic #### Elementary Data Link Protocols in link layer in Computer Networks:

#### Elementary Data Link Protocols in link layer in Computer Networks

The data link layer is responsible for transferring data between adjacent network nodes in a network, providing physical addressing, network interface, flow control, error checking, and recovery. Some of the fundamental protocols at the data link layer are:

- Stop-and-wait protocol: In this protocol, the sender sends a frame and waits for an acknowledgement (ACK) from the receiver before sending the next frame. If an ACK is not received within a timeout period, the frame is retransmitted. Though simple, this protocol leads to inefficient use of bandwidth as the sender remains idle waiting for the ACK.
- Go-back-N protocol: In this protocol, the sender can have N unacknowledged frames outstanding. If an ACK is not received for a frame, all N frames are retransmitted. This protocol is more efficient than stop-and-wait but can still lead to unnecessary retransmissions.
- Selective repeat protocol: This is the most efficient protocol. The receiver acknowledges each frame with a specific sequence number and the sender only retransmits the missed or corrupted frames. There is no fixed window size. This protocol achieves maximum throughput but requires more complexity.

Some mnemonics or learning tricks for these protocols:

- Stop-and-wait: Sender stops and waits, inefficient but simple.
- Go-back-N: N frames can be out, if one is lost all N are resent, more efficient but can lead to unnecessary retransmissions.
- Selective repeat: Most efficient, each frame ack'd individually, only corrupted/lost frames resent.

The choice of protocol depends on bandwidth-delay product and acceptable complexity. More detailed diagrams, examples, advantages, and disadvantages can be included if required. The protocols can be applied to various network technologies like Ethernet, Token Ring, FDDI, etc.