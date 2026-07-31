# Unit 6 - Transport Layer: UDP and TCP

The transport layer of the OSI model is responsible for providing end-to-end communication services for applications. Two of the main protocols used at this layer are the User Datagram Protocol (UDP) and the Transmission Control Protocol (TCP).

## UDP
- UDP is a connectionless protocol that provides a simple and unreliable message service for transaction-oriented services.
- It is used when the amount of data to be transferred is small and speed is more important than reliability.
- UDP does not provide any error checking or flow control mechanisms, so it is up to the application to handle these issues.
- Some common uses of UDP include Domain Name System (DNS) queries, online gaming, and Voice over IP (VoIP) applications.

## TCP
- TCP is a connection-oriented protocol that provides a reliable, stream-oriented service.
- It is used when the amount of data to be transferred is large and reliability is more important than speed.
- TCP provides error checking, flow control, and congestion control mechanisms to ensure that data is transmitted reliably and efficiently.
- Some common uses of TCP include file transfers, email, and web browsing.

In summary, UDP and TCP are two transport layer protocols that provide different levels of service depending on the needs of the application. UDP is best suited for applications that require speed and can tolerate some data loss, while TCP is best suited for applications that require reliability and can tolerate some delay.