## Unit 4 - Transport Layer in Computer Networks

- The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model.
- The protocols of this layer provide end-to-end communication services for applications, such as reliable data transfer, flow control, congestion control, multiplexing, and error detection .
- The transport layer takes data from the upper layer (i.e. application layer) and then breaks it into smaller size segments, numbers each byte, and hands over to the lower layer (network layer) for delivery.
- The transport layer also reassembles the segments at the destination and delivers the complete message to the upper layer.
- The transport layer provides the user address which is specified as a station or port. The port variable represents a specific process within a host that is running an application program.
- The transport layer protocols need to know the network layer address of the destination host to deliver the segments. This is done by using a name resolution service, such as DNS, to map the user-friendly name to the network layer address.
- The transport layer can be either connection-oriented or connectionless, depending on the protocol used. The connection-oriented protocols establish a logical connection between the source and destination before transferring data, such as TCP. The connectionless protocols do not require a connection establishment and send data as independent datagrams, such as UDP .
- The transport layer can also provide different levels of service quality, such as throughput, delay, jitter, and reliability, depending on the application requirements and the network conditions.