### Process-to-process delivery in transport layer

- The transport layer is responsible for delivering data from one process to another process on different or same hosts.
- A process is an instance of a running program that can send or receive data.
- A process is identified by a port number, which is a 16-bit integer that ranges from 0 to 65535.
- The port number is appended to the IP address of the host to form a socket address, which uniquely identifies a process on a network.
- The transport layer uses two protocols to provide process-to-process delivery: TCP and UDP.
- TCP (Transmission Control Protocol) is a connection-oriented, reliable, and full-duplex protocol that provides flow control, congestion control, and error control.
- UDP (User Datagram Protocol) is a connectionless, unreliable, and simple protocol that does not provide any control mechanisms.
- TCP and UDP use header fields to carry information such as source port, destination port, sequence number, acknowledgment number, checksum, etc.
- TCP and UDP also use multiplexing and demultiplexing techniques to allow multiple processes to share the same transport layer protocol.
- Multiplexing is the process of combining data from multiple processes into a single segment with a header that contains the port numbers of the source and destination processes.
- Demultiplexing is the process of extracting data from a single segment and delivering it to the appropriate process based on the port numbers in the header.
- A mnemonic to remember the difference between TCP and UDP is: TCP is Tight Control Protocol, UDP is Unreliable Datagram Protocol.