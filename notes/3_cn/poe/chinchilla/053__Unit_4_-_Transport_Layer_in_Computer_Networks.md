## Unit 4 - Transport Layer in Computer Networks

The transport layer is the fourth layer of the OSI model, responsible for the end-to-end delivery of data between applications. This layer provides services such as connection-oriented and connectionless communication, flow control, error control, and congestion control.

### Key Concepts:

1. **Transmission Control Protocol (TCP):** TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications. It establishes a virtual circuit between the sender and receiver, and ensures that all packets are delivered successfully, retransmitting any packets that are lost or damaged during transmission.

2. **User Datagram Protocol (UDP):** UDP is a connectionless protocol that provides unreliable, unordered, and unchecked delivery of data between applications. It does not establish a virtual circuit between the sender and receiver, and does not guarantee delivery of packets. However, it is faster and more efficient than TCP, and is often used for applications that do not require reliable delivery of data, such as video streaming and online gaming.

3. **Port Numbers:** Port numbers are used to identify the applications running on a device. They are 16-bit numbers that range from 0 to 65535. The well-known port numbers (0 to 1023) are reserved for use by system services and applications, while the registered port numbers (1024 to 49151) are assigned to user applications by the Internet Assigned Numbers Authority (IANA). The dynamic port numbers (49152 to 65535) are used by applications for ephemeral connections.

4. **Flow Control:** Flow control is the process of managing the rate of data transmission between sender and receiver. It prevents the receiver from being overwhelmed by a large amount of data, and ensures that the sender does not transmit data faster than the receiver can process it. TCP uses a sliding window mechanism to implement flow control.

5. **Error Control:** Error control is the process of detecting and correcting errors that occur during data transmission. TCP uses a checksum to detect errors in packets, and retransmits any packets that are lost or damaged during transmission.

6. **Congestion Control:** Congestion control is the process of preventing network congestion by regulating the amount of traffic that is allowed on the network. TCP uses a variety of congestion control algorithms, such as slow start, congestion avoidance, and fast retransmit, to adjust the rate of data transmission based on network conditions.

### Summary:

The transport layer is responsible for the end-to-end delivery of data between applications. TCP is a connection-oriented protocol that provides reliable delivery of data, while UDP is a connectionless protocol that provides faster but less reliable delivery of data. Port numbers are used to identify the applications running on a device. Flow control, error control, and congestion control are important mechanisms used by the transport layer to ensure the efficient and reliable delivery of data between applications.