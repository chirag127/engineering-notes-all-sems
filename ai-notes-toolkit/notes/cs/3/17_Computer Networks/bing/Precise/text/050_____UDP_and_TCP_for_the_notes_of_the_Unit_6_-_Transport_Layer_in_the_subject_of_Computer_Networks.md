### UDP and TCP for the notes of the Unit 6 - Transport Layer in the subject of Computer Networks

- **UDP (User Datagram Protocol)** and **TCP (Transmission Control Protocol)** are two of the main protocols in the transport layer of the TCP/IP model.
- **UDP** is a connectionless protocol that provides a simple and unreliable message service for transaction-oriented services.
    - It is useful for applications that require fast, efficient transmission, such as games or voice and video communication.
    - It does not provide error checking, flow control, or retransmission of lost packets.
- **TCP** is a connection-oriented protocol that provides a reliable, stream-oriented service.
    - It is used by applications that require guaranteed delivery, such as web browsing, email, and file transfer.
    - It provides error checking, flow control, and retransmission of lost packets.
    - It establishes a virtual connection between the sender and receiver before transmitting data.
- Both protocols use port numbers to identify the specific process running on the host computer that the data is intended for.
- The main difference between the two protocols is the level of reliability and the way they handle data transmission.