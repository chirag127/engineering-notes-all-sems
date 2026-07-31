# Process-to-process delivery

- Process-to-process delivery is the function of the transport layer in the OSI reference model or the Internet model .
- It is the delivery of the entire message from a source process to a destination process, where a process is an application program running on a host .
- It is different from node-to-node delivery, which is the function of the data link layer, and host-to-host delivery, which is the function of the network layer.
- Process-to-process delivery requires two services: addressing and multiplexing/demultiplexing.
  - Addressing: The transport layer uses port numbers to identify the source and destination processes. A port number is a 16-bit integer that is appended to the IP address of the host.
  - Multiplexing/demultiplexing: The transport layer can combine data from multiple processes into one segment, or split one segment into data for multiple processes. This is done by using the port numbers to match the data with the corresponding processes.
- The transport layer can also provide other services, such as error control, flow control, congestion control, and quality of service, depending on the protocol used.
- The Internet model has three protocols at the transport layer: UDP, TCP, and SCTP.
  - UDP: User Datagram Protocol is a connectionless and unreliable protocol that provides minimal services. It is suitable for applications that do not require reliability, such as video streaming or voice over IP.
  - TCP: Transmission Control Protocol is a connection-oriented and reliable protocol that provides error control, flow control, congestion control, and ordered delivery. It is suitable for applications that require reliability, such as web browsing or file transfer.
  - SCTP: Stream Control Transmission Protocol is a connection-oriented and reliable protocol that provides multiple streams, message boundaries, and unordered delivery. It is suitable for applications that require both reliability and flexibility, such as telephony or multimedia.