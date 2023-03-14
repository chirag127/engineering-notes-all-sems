### etransmission in transport layer

- The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. 
- The transport layer provides end-to-end communication services for applications, such as connection-oriented communication, reliability, flow control, and multiplexing. 
- The transport layer protocols in the Internet protocol suite are the Transmission Control Protocol (TCP), the User Datagram Protocol (UDP), the Datagram Congestion Control Protocol (DCCP), and the Stream Control Transmission Protocol (SCTP). 
- TCP is the most widely used transport protocol, as it provides reliable, ordered, and error-checked delivery of data. TCP uses a connection-oriented approach, which means that it establishes a connection with the destination before sending any data. TCP also uses mechanisms such as sequence numbers, acknowledgements, retransmission, and congestion control to ensure the quality of service.  
- UDP is a simpler transport protocol, as it provides connectionless and unreliable delivery of data. UDP does not guarantee that the data will arrive in order, without errors, or at all. UDP is useful for applications that require speed and efficiency, such as streaming media, online gaming, and voice over IP. UDP also has a smaller header size than TCP, which reduces the overhead. 
- DCCP is a transport protocol that provides congestion control for unreliable datagrams. DCCP is designed for applications that can tolerate some packet loss, but need to avoid congestion collapse. DCCP also supports features such as multipath, encryption, and authentication. 
- SCTP is a transport protocol that provides reliable, ordered, and unordered delivery of data. SCTP is designed for applications that require multiple streams of data within a single connection, such as telephony and web browsing. SCTP also supports features such as multihoming, partial reliability, and message-oriented communication. 

#### Mnemonics and learning tricks

- To remember the four transport layer protocols in the Internet protocol suite, you can use the acronym **TUDS** (TCP, UDP, DCCP, SCTP).
- To remember the main differences between TCP and UDP, you can use the following table:

| TCP | UDP |
| --- | --- |
| Connection-oriented | Connectionless |
| Reliable | Unreliable |
| Ordered | Unordered |
| Error-checked | No error-checking |
| Congestion-controlled | No congestion control |
| Larger header | Smaller header |

- To remember the main features of DCCP and SCTP, you can use the following sentences:

  - **D**CCP **c**ontrols **c**ongestion for unreliable datagrams.
  - **S**CTP **s**upports multiple **s**treams within a connection.