### Process-to-process delivery in transport layer

- The transport layer is responsible for delivering data from one process to another process on different or same hosts.
- A process is an instance of a running program that can send or receive data.
- A process is identified by a port number, which is a 16-bit integer that ranges from 0 to 65535.
- The port number is appended to the IP address of the host to form a socket address, which uniquely identifies a process on a network.
- The transport layer uses two protocols to provide process-to-process delivery: TCP and UDP.
- TCP (Transmission Control Protocol) is a connection-oriented, reliable, and full-duplex protocol that provides flow control, congestion control, and error control.
- UDP (User Datagram Protocol) is a connectionless, unreliable, and simple protocol that does not provide any control mechanisms.
- TCP and UDP use different header formats to encapsulate data segments before sending them to the network layer.
- TCP header contains fields such as source port, destination port, sequence number, acknowledgment number, header length, flags, window size, checksum, urgent pointer, and options.
- UDP header contains only four fields: source port, destination port, length, and checksum.
- TCP provides reliable data transfer by using sequence numbers, acknowledgments, timers, and retransmission mechanisms.
- UDP does not guarantee reliable data transfer and does not use any acknowledgment or retransmission mechanisms.
- TCP provides flow control by using a sliding window mechanism that adjusts the size of the window based on the receiver's buffer availability and network congestion.
- UDP does not provide flow control and does not care about the receiver's buffer availability or network congestion.
- TCP provides congestion control by using algorithms such as slow start, congestion avoidance, fast retransmit, and fast recovery that adapt the sending rate based on the network conditions.
- UDP does not provide congestion control and does not adapt the sending rate based on the network conditions.
- TCP is suitable for applications that require reliable, ordered, and error-free data transfer, such as web browsing, file transfer, email, etc.
- UDP is suitable for applications that require fast, real-time, and loss-tolerant data transfer, such as video streaming, voice over IP, online gaming, etc.

A mnemonic to remember the difference between TCP and UDP is:

- TCP: Transmission Control Protocol
- UDP: Unreliable Datagram Protocol

A mnemonic to remember the fields in the TCP header is:

- SPAN: Source Port, Acknowledgment Number
- DASH: Destination Port, Sequence Number
- FLAG: Flags, Length, Window Size
- CUP: Checksum, Urgent Pointer
- OPT: Options

A mnemonic to remember the fields in the UDP header is:

- SPLC: Source Port, Length, Checksum
- DPD: Destination Port, Data

An example of a TCP header in hexadecimal format is:

| 00 50 | 00 16 | 00 00 00 01 | 00 00 00 00 |
|-------|-------|-------------|-------------|
| 50 02 | 20 00 | 00 00 00 00 | 00 00       |
| Source Port | Destination Port | Sequence Number | Acknowledgment Number |
| Header Length | Flags | Window Size | Checksum |
| Urgent Pointer | Options | Padding | Data |

An example of a UDP header in hexadecimal format is:

| 00 50 | 00 16 | 00 08 | 00 00 |
|-------|-------|-------|-------|
| 00 00 00 00 00 00 00 00       |
| Source Port | Destination Port | Length | Checksum |
| Data |