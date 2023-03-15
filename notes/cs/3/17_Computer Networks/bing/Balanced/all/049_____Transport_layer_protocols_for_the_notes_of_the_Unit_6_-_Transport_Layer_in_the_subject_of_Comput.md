# Transport layer protocols

The transport layer is the fourth layer in the OSI model, which provides communication services between the computers connected in the network. The transport layer is responsible for:

- Process-to-process delivery: The transport layer ensures that the data packets are delivered from the source process to the destination process, regardless of the physical addresses of the hosts.
- Segmentation and reassembly: The transport layer divides the data stream into smaller segments that can fit into the network layer packets, and reassembles them at the destination.
- Flow control: The transport layer regulates the rate of data transmission between the sender and the receiver, to avoid congestion and buffer overflow.
- Error control: The transport layer detects and corrects errors that may occur during the data transmission, such as lost, duplicated, or corrupted segments.
- Multiplexing and demultiplexing: The transport layer allows multiple processes to share the same network connection, by assigning each segment a port number that identifies the source and destination processes.
- Connection management: The transport layer establishes, maintains, and terminates the logical connections between the processes.

The two main transport layer protocols are:

- Transmission Control Protocol (TCP): It provides reliable, connection-oriented, and byte-stream communication between two hosts. TCP uses a three-way handshake to establish a connection, and a four-way handshake to terminate it. TCP uses sequence numbers, acknowledgments, timers, and windowing to ensure reliable data delivery and error control. TCP also provides congestion control mechanisms to avoid network overload.
- User Datagram Protocol (UDP): It provides unreliable, connectionless, and datagram-oriented communication between two hosts. UDP does not guarantee data delivery, error control, or congestion control. UDP is faster and simpler than TCP, and is suitable for real-time applications that can tolerate some data loss. UDP also supports multicast and broadcast communication.