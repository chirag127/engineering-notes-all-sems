# Connection Management for the Transport Layer

- The transport layer is the layer-4 of the OSI reference model that is responsible for the process-to-process delivery of the entire message.
- The transport layer provides two types of services to the network applications: connection-oriented and connectionless.
- Connection-oriented service is provided by the Transmission Control Protocol (TCP), which establishes a logical connection between the source and destination processes before exchanging data.
- Connectionless service is provided by the User Datagram Protocol (UDP), which does not require any connection establishment or termination and sends data as independent packets.
- Connection management is the process of creating, maintaining, and terminating a connection between two or more processes.
- Connection management involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is the phase where the source and destination processes agree on the parameters of the connection, such as the port numbers, sequence numbers, window sizes, etc.
- Connection establishment in TCP uses a three-way handshake mechanism, where the source sends a SYN segment, the destination replies with a SYN-ACK segment, and the source acknowledges with an ACK segment.
- Connection establishment in UDP does not involve any handshake, as UDP is a connectionless protocol.
- Data transfer is the phase where the source and destination processes exchange data segments over the established connection.
- Data transfer in TCP is reliable, as TCP uses mechanisms such as sequence numbers, acknowledgments, timers, retransmissions, flow control, and congestion control to ensure that all segments are delivered correctly and in order.
- Data transfer in UDP is unreliable, as UDP does not use any of the mechanisms that TCP uses, and simply sends and receives datagrams without any error or flow control.
- Connection termination is the phase where the source and destination processes close the connection after the data transfer is completed.
- Connection termination in TCP uses a four-way handshake mechanism, where the source sends a FIN segment, the destination replies with an ACK segment, the destination sends a FIN segment, and the source replies with an ACK segment.
- Connection termination in UDP does not involve any handshake, as UDP does not maintain any connection state.
- Connection management for the transport layer is important for ensuring the quality of service, security, and efficiency of the network communication.