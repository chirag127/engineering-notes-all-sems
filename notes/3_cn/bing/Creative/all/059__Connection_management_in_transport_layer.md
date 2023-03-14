### Connection management in transport layer

- Connection management is the process of establishing, maintaining, and terminating a logical connection between two end hosts in a network.
- Connection management is performed by the transport layer protocols, such as TCP and UDP, that provide end-to-end communication services to the applications.
- Connection management involves three phases: connection establishment, data transfer, and connection termination.
- Connection establishment is the phase where the two end hosts agree on the parameters and state of the connection, such as the port numbers, sequence numbers, window sizes, and options.
- Connection establishment is usually done by a handshake protocol, such as the three-way handshake in TCP, that involves the exchange of control messages (SYN, SYN-ACK, ACK) between the end hosts.
- Connection establishment can be active or passive, depending on whether the end host initiates or waits for a connection request. The end host that initiates the connection is called the client, and the end host that accepts the connection is called the server.
- Connection establishment can also be symmetric or asymmetric, depending on whether the end hosts have equal or different roles and responsibilities in the connection. TCP provides a symmetric connection management service, where both end hosts can send and receive data and control messages. UDP provides an asymmetric connection management service, where one end host is the sender and the other is the receiver, and no control messages are exchanged.
- Data transfer is the phase where the end hosts exchange data and control messages over the established connection, according to the agreed parameters and state of the connection.
- Data transfer is usually done by a sliding window protocol, such as the go-back-N or selective repeat protocol, that involves the use of sequence numbers, acknowledgments, timers, and retransmissions to ensure reliable and orderly delivery of data.
- Data transfer can also be reliable or unreliable, depending on whether the transport layer protocol guarantees or not the delivery of data. TCP provides a reliable data transfer service, where every data segment is acknowledged and retransmitted if lost or corrupted. UDP provides an unreliable data transfer service, where data segments are sent without acknowledgments or retransmissions, and may be lost, corrupted, duplicated, or reordered.
- Connection termination is the phase where the end hosts agree to close the connection and release the resources associated with it, such as the port numbers, sequence numbers, window sizes, and buffers.
- Connection termination is usually done by a handshake protocol, such as the four-way handshake in TCP, that involves the exchange of control messages (FIN, FIN-ACK, ACK) between the end hosts.
- Connection termination can be graceful or abrupt, depending on whether the end hosts wait or not for the completion of data transfer before closing the connection. TCP provides a graceful connection termination service, where both end hosts can initiate or accept the connection closure, and wait for the acknowledgment of all the data segments before sending or receiving the FIN message. UDP provides an abrupt connection termination service, where either end host can close the connection at any time, without waiting for the acknowledgment of any data segment.

#### Mnemonics and learning tricks for connection management in transport layer

- To remember the three phases of connection management, use the acronym EDT: Establishment, Data transfer, Termination.
- To remember the three control messages used in TCP connection establishment, use the acronym SAS: SYN, SYN-ACK, ACK.
- To remember the four control messages used in TCP connection termination, use the acronym FFA: FIN, FIN-ACK, ACK.
- To remember the difference between TCP and UDP in connection management, use the following table:

| TCP | UDP |
| --- | --- |
| Symmetric | Asymmetric |
| Reliable | Unreliable |
| Handshake | No handshake |
| Graceful | Abrupt |