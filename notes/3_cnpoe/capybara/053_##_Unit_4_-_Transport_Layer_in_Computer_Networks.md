## Unit 4 - Transport Layer in Computer Networks

The transport layer is the fourth layer of the OSI model and is responsible for providing reliable communication between processes running on different hosts. It is responsible for end-to-end communication over a network and ensures that the data reaches the destination in the same order in which it was sent.

### Functions of the Transport Layer

1. **Segmentation and Reassembly**: The transport layer divides the data received from the application layer into smaller segments which can be transmitted over the network. At the receiving end, it reassembles the segments into the original data.

2. **Flow Control**: The transport layer ensures that the sender does not overwhelm the receiver by controlling the amount of data that can be transmitted at a time.

3. **Error Control**: The transport layer provides error detection and correction mechanisms to ensure that data is transmitted reliably.

4. **Multiplexing and Demultiplexing**: The transport layer enables multiple applications to use the network simultaneously by assigning a unique identifier to each application.

### Protocols of the Transport Layer

1. **Transmission Control Protocol (TCP)**: TCP is a connection-oriented protocol that provides reliable, ordered, and error-checked delivery of data between applications. It is widely used for applications that require guaranteed delivery of data, such as email, file transfer, and web browsing.

2. **User Datagram Protocol (UDP)**: UDP is a connectionless protocol that provides unreliable, unordered, and unacknowledged delivery of data between applications. It is used for applications that can tolerate some loss of data, such as video streaming and online gaming.

### Mnemonics and Learning Tricks

1. **TCP: Tightly Controlled Protocol**: This mnemonic can help you remember that TCP is a connection-oriented protocol that provides reliable delivery of data.

2. **UDP: Unreliable Datagram Protocol**: This mnemonic can help you remember that UDP is a connectionless protocol that provides unreliable delivery of data.

3. **SR: Segment and Reassemble**: This mnemonic can help you remember that the transport layer segments the data received from the application layer and reassembles it at the receiving end.

### Advantages of the Transport Layer

1. Provides reliable communication between processes running on different hosts.
2. Enables multiple applications to use the network simultaneously.
3. Provides error detection and correction mechanisms to ensure reliable data transmission.

### Disadvantages of the Transport Layer

1. Overhead of error control mechanisms can reduce network performance.
2. Connection-oriented protocols like TCP can increase latency due to the overhead of establishing and maintaining connections.

### Examples of the Transport Layer

1. Transmission Control Protocol (TCP)
2. User Datagram Protocol (UDP)

### Applications of the Transport Layer

1. Email
2. File transfer
3. Web browsing
4. Video streaming
5. Online gaming