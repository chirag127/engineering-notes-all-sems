### Process-to-process delivery

- Process-to-process delivery is the function of the transport layer in the OSI reference model or the internet model .
- It is the delivery of the entire message from a source process to a destination process, where a process is an application program running on a host .
- It is different from node-to-node delivery (data link layer) or host-to-host delivery (network layer), which only deliver frames or datagrams between two nodes or two hosts, respectively .
- Process-to-process delivery requires two services: addressing and multiplexing/demultiplexing .
- Addressing is the process of identifying the source and destination processes by using port numbers, which are logical identifiers assigned to each process .
- Multiplexing is the process of combining data from multiple processes into a single stream for transmission, while demultiplexing is the process of separating data from a single stream into multiple processes for reception .
- The transport layer protocols, such as UDP, TCP, and SCTP, provide process-to-process delivery by using port numbers and multiplexing/demultiplexing techniques .
- The transport layer protocols also provide other services, such as error control, flow control, congestion control, and reliability, depending on the requirements of the application processes .