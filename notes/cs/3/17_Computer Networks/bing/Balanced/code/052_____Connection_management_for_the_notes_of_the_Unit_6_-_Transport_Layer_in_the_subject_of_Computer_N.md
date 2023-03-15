# Connection Management for the Transport Layer

- The transport layer is the layer-4 of the OSI reference model that is responsible for the process-to-process delivery of the entire message.
- The transport layer provides two types of services to the network applications: connection-oriented and connectionless.
- Connection-oriented service establishes a logical connection between the source and destination processes before exchanging data. Connectionless service does not require a connection and sends data as independent packets.
- The connection management for the transport layer involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is the process of creating a connection between the source and destination processes. It involves the exchange of messages to negotiate the parameters and state of the connection.
- Data transfer is the process of sending and receiving data over the established connection. It involves the use of mechanisms to ensure reliable, ordered, and error-free delivery of data.
- Connection termination is the process of closing the connection between the source and destination processes. It involves the exchange of messages to release the resources and state of the connection.
- The most common transport layer protocol that provides connection-oriented service is the Transmission Control Protocol (TCP). TCP uses a three-way handshake to establish a connection, a sliding window protocol to transfer data, and a four-way handshake to terminate a connection.
- The most common transport layer protocol that provides connectionless service is the User Datagram Protocol (UDP). UDP does not use any handshake to establish or terminate a connection, and does not guarantee reliable, ordered, or error-free delivery of data.
- The connection management for the transport layer is important for ensuring the quality of service and the performance of the network applications. It also enables the transport layer to provide different levels of abstraction and functionality to the network applications.