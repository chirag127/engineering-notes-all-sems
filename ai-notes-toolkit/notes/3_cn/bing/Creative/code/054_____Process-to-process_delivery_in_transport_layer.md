### Process-to-process delivery in transport layer

The transport layer is responsible for delivering data from one process to another process on different hosts. A process is an entity of the application layer that uses the services of the transport layer. For example, a web browser is a process that communicates with a web server, which is another process.

To achieve process-to-process delivery, the transport layer needs to perform the following tasks:

- Identify the processes: The transport layer needs to identify the source and destination processes by using port numbers. A port number is a 16-bit integer that uniquely identifies a process on a host. For example, port 80 is usually used for web servers, and port 25 is used for email servers. The transport layer adds the port numbers to the data segments before sending them to the network layer.

- Segment and reassemble the data: The transport layer needs to divide the data from the application layer into smaller segments that can fit into the network layer packets. Each segment has a sequence number that indicates its position in the original data. The transport layer also needs to reassemble the segments at the destination host and deliver them to the correct process.

- Provide reliable and/or unreliable delivery: The transport layer can provide different types of delivery services depending on the requirements of the application layer. Some applications need reliable delivery, which means that the transport layer ensures that all the segments are delivered correctly and in order. This can be achieved by using acknowledgments, timers, and retransmissions. Some applications can tolerate unreliable delivery, which means that the transport layer does not guarantee that all the segments are delivered or that they are delivered in order. This can be achieved by using checksums and error detection.

- Control the flow and congestion: The transport layer needs to regulate the rate of data transmission between the source and destination hosts to avoid overflowing the network or the receiver's buffer. This can be achieved by using flow control and congestion control mechanisms. Flow control is the technique of adjusting the window size of the sender based on the feedback from the receiver. Congestion control is the technique of adjusting the window size of the sender based on the network conditions.