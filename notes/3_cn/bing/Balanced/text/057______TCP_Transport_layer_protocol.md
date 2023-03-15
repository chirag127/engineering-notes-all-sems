#### TCP Transport layer protocol

- TCP stands for Transmission Control Protocol. It is a transport layer protocol that facilitates the transmission of packets from source to destination.
- TCP is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network.
- TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.
- TCP has three main steps to perform the data transmission: establish connection, send packets of data, and close the connection.
- TCP uses a four-way handshake to establish the connection between the sender and the receiver. The sender sends a SYN (synchronize) segment, the receiver replies with a SYN-ACK (synchronize-acknowledge) segment, the sender responds with an ACK (acknowledge) segment, and the connection is established.
- TCP uses a sliding window protocol to send packets of data. The sender can send multiple packets without waiting for the acknowledgment of each one, but it has a limit on how many packets it can send before receiving an acknowledgment. The receiver can send an acknowledgment for multiple packets at once, and also request the sender to retransmit any lost or corrupted packets.
- TCP uses a three-way handshake to close the connection between the sender and the receiver. The sender sends a FIN (finish) segment, the receiver replies with an ACK segment, the receiver sends a FIN segment, and the sender replies with an ACK segment. The connection is then terminated.
- TCP is a standard that defines how to establish and maintain a network conversation through which application programs can exchange data.
- TCP is used by many applications that require reliable and ordered delivery of data, such as web browsers, email clients, file transfer programs, etc.