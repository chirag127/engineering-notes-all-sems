### Window management in transport layer

- The transport layer is the fourth layer of the OSI model and provides end-to-end communication services for applications.
- The transport layer is responsible for flow control, which is the regulation of the rate and order of data transmission between two hosts.
- Flow control is necessary to prevent congestion, loss, and reordering of packets in the network.
- One of the techniques used by the transport layer for flow control is the sliding window technique, which is implemented by the Transmission Control Protocol (TCP).
- The sliding window technique involves the use of a window, which is a range of sequence numbers that indicate the packets that can be sent or received by a host at any given time.
- The window size can vary depending on the buffer availability, network conditions, and feedback from the receiver.
- The sender maintains a send window, which indicates the packets that can be sent without waiting for an acknowledgment from the receiver.
- The receiver maintains a receive window, which indicates the packets that can be received and buffered without overflowing the buffer.
- The sender and receiver exchange window information using special control packets called acknowledgments (ACKs).
- The sender adjusts its send window based on the receive window advertised by the receiver in the ACKs.
- The receiver adjusts its receive window based on the packets received and buffered.
- The sliding window technique allows the sender and receiver to dynamically adapt to the network conditions and achieve optimal throughput and reliability.