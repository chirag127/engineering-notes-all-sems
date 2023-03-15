## Unit 4 - Transport Layer in Computer Networks

The transport layer is a conceptual division of methods in the layered architecture of protocols in the network stack in the Internet protocol suite and the OSI model. The protocols of this layer provide end-to-end communication services for applications.

The transport layer takes data from the application layer and divides it into smaller units called segments, numbers each byte, and hands over to the network layer for delivery. The transport layer also provides error-checking mechanisms and data flow controls to ensure the reliable arrival of messages across a network.

The transport layer interacts with the functions of the session layer and provides the user address which is specified as a station or port. The port variable represents a specific process or service running on the host machine. The transport layer protocols need to know the network layer address of the destination host to deliver the segments.

The transport layer can use either connection-oriented or connectionless protocols, depending on the requirements of the application. Connection-oriented protocols establish a logical connection between the source and destination hosts before transferring data, while connectionless protocols do not require any prior setup and send data as independent packets.

Some of the common transport layer protocols are:

- Transmission Control Protocol (TCP): A connection-oriented, reliable, byte-stream protocol that provides error detection, retransmission, flow control, and congestion control.
- User Datagram Protocol (UDP): A connectionless, unreliable, datagram protocol that provides minimal overhead and is suitable for real-time applications that can tolerate some packet loss.
- Stream Control Transmission Protocol (SCTP): A connection-oriented, reliable, message-oriented protocol that provides multiple streams of data within a single connection and supports multihoming.

A possible ASCII diagram for the transport layer in computer networks is:

```
+----------------+      +----------------+      +----------------+
| Application    |      | Application    |      | Application    |
+----------------+      +----------------+      +----------------+
| Presentation   |      | Presentation   |      | Presentation   |
+----------------+      +----------------+      +----------------+
| Session        |      | Session        |      | Session        |
+----------------+      +----------------+      +----------------+
| Transport      |      | Transport      |      | Transport      |
+----------------+      +----------------+      +----------------+
| Network        |      | Network        |      | Network        |
+----------------+      +----------------+      +----------------+
| Data Link      |      | Data Link      |      | Data Link      |
+----------------+      +----------------+      +----------------+
| Physical       |      | Physical       |      | Physical       |
+----------------+      +----------------+      +----------------+
    Host A               Router                  Host B

    +----------------+      +----------------+      +----------------+
    | TCP/UDP/SCTP  |      | TCP/UDP/SCTP  |      | TCP/UDP/SCTP  |
    +----------------+      +----------------+      +----------------+
    | IP            |      | IP            |      | IP            |
    +----------------+      +----------------+      +----------------+
    | Ethernet      |      | Ethernet      |      | Ethernet      |
    +----------------+      +----------------+      +----------------+
    | Cable         |      | Cable         |      | Cable         |
    +----------------+      +----------------+      +----------------+
```