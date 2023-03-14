## Unit 4 - Transport Layer in Computer Networks

The transport layer is an essential part of the computer network architecture. It ensures the reliable delivery of data between sender and receiver applications. In this unit, we will learn about the transport layer's functions, protocols, and their applications.

### Functions of Transport Layer

The transport layer has two main functions:

1. **Segmentation and Reassembly**: The transport layer breaks down the data received from the application layer into smaller units called segments. These segments are then transmitted over the network. At the receiving end, the transport layer reassembles the segments back into the original data.

2. **Reliable Data Transfer**: The transport layer ensures that the data sent from the sender reaches the receiver without any loss, duplication, or error. The transport layer achieves this by using error detection and correction mechanisms, flow control, and congestion control.

### Transport Layer Protocols

There are two widely used transport layer protocols:

1. **Transmission Control Protocol (TCP)**: TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications. It uses a three-way handshake to establish a connection between sender and receiver before transmitting any data. TCP is used for applications that require reliable data transfer, such as email, file transfer, and web browsing.

2. **User Datagram Protocol (UDP)**: UDP is a connectionless protocol that provides fast, unreliable, and unordered delivery of data between applications. Unlike TCP, UDP does not establish a connection before transmitting data. UDP is used for applications that can tolerate some loss of data, such as video streaming, online gaming, and real-time communication.

### Mnemonics and Learning Tricks

- To remember the functions of the transport layer, you can use the mnemonic "SRF": Segmentation and Reassembly, Reliable Data Transfer.

- To remember the differences between TCP and UDP, you can use the mnemonic "CUT": Connection-oriented, Reliable, Ordered (TCP) vs Connectionless, Unreliable, and Unordered (UDP).

### Conclusion

The transport layer plays a crucial role in ensuring reliable data transfer between applications in a computer network. TCP and UDP are the two primary transport layer protocols used in the internet. Understanding the functions and differences between these protocols is essential for network administrators and developers.