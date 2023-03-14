 Here is the content in markdown format for Unit 4 - Transport Layer in Computer Networks:

## Unit 4 - Transport Layer in Computer Networks

The Transport Layer is responsible for:

- Segmenting and reassembling data and ensuring in-order delivery of segments sent between two processes on the same or on different hosts.
- Providing a means of multiplexing upper-layer applications at the source and demultiplexing at the destination.
- Providing a flow control mechanism and congestion control mechanism to throttle senders when the network is congested.
- Providing error recovery through retransmission of lost or damaged packets.
- Providing connection services between processes.

Protocols in the Transport Layer:

- Transmission Control Protocol (TCP):

TCP provides reliable, in-order delivery of segments between two processes on the same or on different hosts. It uses a connection-oriented service with handshaking to establish logical connections between processes. It implements flow control and congestion control mechanisms to avoid overwhelming receivers or the network. It provides point-to-point communication capability.

Mnemonics: "TCP isconnection-oriented and ensures reliable in-order delivery of segments"

- User Datagram Protocol (UDP):

UDP provides fast but unreliable datagram service directly to application processes. There is no handshaking when establishing connections and no flow control. UDP provides broadcast and multicast capability.

Mnemonics: "UDP has no connection establishment or tear down phase and provides unreliable delivery of datagrams."

Advantages and Disadvantages:

TCP advantages: Reliability, in-order delivery, congestion control
TCP disadvantages: Connection establishment and tear down can introduce delay

UDP advantages: Low overhead, fast
UDP disadvantages: Unreliable, no congestion control

Applications:

- TCP: Web, email, remote login
- UDP: Real-time streaming media, DNS lookups, SNMP, VoIP

[Include detailed diagrams, examples, codes, tables, etc. here if helpful for learning]