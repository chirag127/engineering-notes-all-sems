#### Datagram in Networking

A datagram is a self-contained, independent entity of data carrying sufficient information to be routed from the source to the destination computer without relying on earlier exchanges between the source and destination computers or the transporting network. They are used in packet-switched networks like the Internet.

Datagrams are also known as packets, segments, or frames depending on the network architecture. They contain a header and payload. The header contains information about the source and destination IP addresses, the protocol in use, and the length of the payload. The payload contains the actual data being sent.

Datagrams are used in the following protocols:

1. Internet Protocol (IP) - Used in the Internet for routing packets between networks.

2. User Datagram Protocol (UDP) - Used for simple, connectionless communication between applications.

3. Datagram Congestion Control Protocol (DCCP) - Used for congestion-controlled transmission of datagrams.

Mnemonics and Learning Tricks:

1. Remember the word "DATAGRAM" and use it as an acronym to remember the various components of a datagram:

- D - Destination Address
- A - Application Data
- T - Type of Service
- A - Additional Header Information
- G - Gateway IP Address
- R - Routing Information
- A - Action Information
- M - Maximum Segment Size

2. Remember the phrase "Data Goes Right After the Header" to remember the order of the components in a datagram.

Advantages of Datagram:

1. Datagram-based networks are more scalable and efficient than circuit-switched networks.

2. They allow for greater flexibility and speed in data transmission.

Disadvantages of Datagram:

1. Datagrams are subject to packet loss and duplication due to network congestion.

2. They do not guarantee reliable delivery of data.

Examples of Datagram Applications:

1. Videoconferencing

2. Online Gaming

3. Voice over IP (VoIP)