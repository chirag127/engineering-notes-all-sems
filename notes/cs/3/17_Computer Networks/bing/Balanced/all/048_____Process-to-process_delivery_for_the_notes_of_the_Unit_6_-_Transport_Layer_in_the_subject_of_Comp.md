# Process-to-process delivery

- Process-to-process delivery is the function of the transport layer in the OSI reference model or the Internet model .
- It is the delivery of the entire message from a source process to a destination process, where a process is an application program running on a host .
- It is different from node-to-node delivery, which is the function of the data link layer, and host-to-host delivery, which is the function of the network layer.
- Process-to-process delivery requires two services: addressing and multiplexing/demultiplexing.
- Addressing is the process of identifying the source and destination processes using port numbers, which are logical addresses assigned by the transport layer .
- Multiplexing is the process of combining data from multiple processes into a single stream for transmission, and demultiplexing is the reverse process of separating data from a single stream into multiple processes .
- The transport layer protocols that provide process-to-process delivery are UDP, TCP, and SCTP in the Internet model. UDP is a connectionless and unreliable protocol, TCP is a connection-oriented and reliable protocol, and SCTP is a connection-oriented and reliable protocol that supports multiple streams .