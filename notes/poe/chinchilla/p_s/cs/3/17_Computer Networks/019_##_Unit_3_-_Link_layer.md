## Unit 3 - Link layer

The Link layer is the second layer in the OSI model and is responsible for the reliable transmission of data between two nodes connected by a physical communication link. This layer provides services to the Network layer and is responsible for error detection and correction, flow control, and medium access control.

### Functions of the Link layer

The Link layer performs the following functions:

1. **Framing**: The Link layer divides the data received from the Network layer into frames and adds a header and a trailer to each frame. The header contains information about the source and destination nodes, while the trailer contains error detection and correction codes.

2. **Error detection and correction**: The Link layer uses error detection and correction codes to ensure that the data transmitted over the link is error-free. The most common error detection and correction codes used in the Link layer are CRC (Cyclic Redundancy Check) and Hamming code.

3. **Flow control**: The Link layer manages the flow of data between two nodes to prevent buffer overflow or underflow. The two most common flow control techniques used in the Link layer are Stop-and-Wait and Sliding Window.

4. **Medium access control**: The Link layer determines which node has access to the communication medium at any given time. The most common medium access control techniques used in the Link layer are CSMA/CD (Carrier Sense Multiple Access with Collision Detection) and Token Passing.

### Protocols in the Link layer

The Link layer uses several protocols to provide its services. Some of the most common protocols used in the Link layer are:

1. **Ethernet**: Ethernet is a widely used protocol in the Link layer that provides reliable and efficient communication over a local area network (LAN). It uses CSMA/CD for medium access control and supports data rates of up to 100 Gbps.

2. **PPP (Point-to-Point Protocol)**: PPP is a protocol used to establish a point-to-point connection between two nodes over a serial link. It provides error detection and correction, flow control, and authentication services.

3. **HDLC (High-Level Data Link Control)**: HDLC is a protocol used for synchronous communication between two nodes over a point-to-point link. It provides error detection and correction, flow control, and sequencing services.

### Advantages and disadvantages of the Link layer

Advantages:

- The Link layer provides reliable and efficient communication between two nodes connected by a physical link.
- The Link layer uses error detection and correction codes to ensure that the data transmitted over the link is error-free.
- The Link layer manages the flow of data between two nodes to prevent buffer overflow or underflow.
- The Link layer determines which node has access to the communication medium at any given time.

Disadvantages:

- The Link layer is limited to providing services between two nodes connected by a physical link and does not provide end-to-end communication between two nodes.
- The Link layer can only provide communication within a local area network and cannot be used for wide area network communication.

### Applications of the Link layer

The Link layer is used in several applications, some of which are:

- Local area network (LAN) communication
- Point-to-point communication over a serial link
- Communication between a computer and a peripheral device, such as a printer or a scanner.

### Conclusion

The Link layer is an important layer in the OSI model that provides reliable and efficient communication between two nodes connected by a physical link. It performs several functions such as framing, error detection and correction, flow control, and medium access control. The Link layer uses several protocols such as Ethernet, PPP, and HDLC to provide its services.