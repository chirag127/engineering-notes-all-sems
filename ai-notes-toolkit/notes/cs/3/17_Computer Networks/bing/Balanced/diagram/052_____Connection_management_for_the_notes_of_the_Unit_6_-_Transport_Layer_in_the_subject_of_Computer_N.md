### Connection management for the transport layer

- The transport layer is the layer-4 of the OSI reference model that is responsible for the process-to-process delivery of the entire message.
- The transport layer provides two types of services to the network applications: connection-oriented and connectionless.
- Connection-oriented service establishes a logical connection between the source and destination processes before exchanging data, and terminates the connection after the data transfer is complete. An example of a connection-oriented protocol is TCP.
- Connectionless service does not require a logical connection between the source and destination processes, and sends data as independent packets. An example of a connectionless protocol is UDP.
- Connection management is the process of setting up, maintaining, and terminating a connection between two or more processes.
- Connection management involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is the phase where the source and destination processes agree on the parameters of the connection, such as the port numbers, sequence numbers, window sizes, etc. This phase usually involves a three-way handshake between the processes.
- Data transfer is the phase where the source and destination processes exchange data packets according to the agreed parameters. This phase may involve mechanisms such as flow control, error control, congestion control, etc. to ensure reliable and efficient data transfer.
- Connection termination is the phase where the source and destination processes signal each other that they have no more data to send, and release the resources allocated for the connection. This phase usually involves a four-way handshake between the processes.
- Connection management for the transport layer is important for ensuring the quality of service, security, and performance of the network applications.