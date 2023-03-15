## Unit 6 - Transport Layer

The transport layer is responsible for providing end-to-end communication services for applications. It provides logical communication between application processes running on different hosts. Some of the key responsibilities of the transport layer include:

1. **Process-to-process communication:** The transport layer provides a logical communication channel between processes running on different hosts. This is achieved through the use of port numbers, which uniquely identify the processes.

2. **Reliable data transfer:** The transport layer is responsible for ensuring that data is transferred reliably between hosts. This is achieved through the use of error detection and correction mechanisms, as well as flow control and congestion control.

3. **Segmentation and reassembly:** The transport layer is responsible for dividing the data into smaller segments that can be transmitted over the network. It is also responsible for reassembling the segments into their original order at the destination.

4. **Multiplexing and demultiplexing:** The transport layer is responsible for multiplexing multiple application-layer conversations onto a single transport-layer connection, and demultiplexing the data at the destination.

The two most common transport layer protocols are the Transmission Control Protocol (TCP) and the User Datagram Protocol (UDP). TCP provides reliable, connection-oriented communication, while UDP provides unreliable, connectionless communication. The choice of protocol depends on the requirements of the application.