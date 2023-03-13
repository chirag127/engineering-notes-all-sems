TCP Transport layer protocol
####

TCP Transport layer protocol is a standard that defines how to establish and maintain a network conversation through which application programs can exchange data. It is a connection-oriented protocol that means it establishes the connection prior to the communication that occurs between the computing devices in a network . TCP is a reliable protocol as it follows the flow and error control mechanism. It also supports the acknowledgment mechanism, which checks the state and sound arrival of the data.

The following diagram illustrates the basic architecture of a TCP Transport layer protocol using ASCII characters:

```
+-----------------+          +-----------------+
| Application     |          | Application     |
| Layer           |          | Layer           |
+-----------------+          +-----------------+
| TCP             |          | TCP             |
| Transport Layer |          | Transport Layer |
+-----------------+          +-----------------+
| IP              |          | IP              |
| Network Layer   |          | Network Layer   |
+-----------------+          +-----------------+
| Data Link Layer |          | Data Link Layer |
+-----------------+          +-----------------+
| Physical Layer  |          | Physical Layer  |
+-----------------+          +-----------------+
|                 |          |                 |
|      Host A     |          |      Host B     |
|                 |          |                 |
+-----------------+          +-----------------+
```

The TCP Transport layer protocol works as follows:

- Step 1: Establish connection
  - When two computers want to send data to each other over TCP, they first need to establish a connection using a three-way handshake.
  - The sender initiates the connection by sending a SYN (synchronize) segment to the receiver, which contains the initial sequence number and other parameters.
  - The receiver responds with a SYN-ACK (synchronize-acknowledge) segment, which contains the acknowledgment number (one more than the received sequence number) and its own initial sequence number and parameters.
  - The sender confirms the connection by sending an ACK (acknowledge) segment, which contains the acknowledgment number (one more than the received sequence number) and other parameters.
  - The connection is now established and ready for data transfer.

- Step 2: Send packets of data
  - When a packet of data is sent over TCP, the recipient must always acknowledge what they received by sending an ACK segment back to the sender.
  - The sender assigns a sequence number to each byte of data and sends it in a TCP segment, which also contains the source and destination port numbers, the checksum, and other flags and options.
  - The receiver checks the checksum and the sequence number of the received segment and sends an ACK segment back to the sender, which contains the acknowledgment number (one more than the last received sequence number) and other parameters.
  - The sender keeps track of the segments that have been sent but not acknowledged and retransmits them if they are lost or corrupted in the network.
  - The receiver also keeps track of the segments that have been received and reorders them if they are out of order.
  - The sender and the receiver use the sliding window mechanism to control the flow of data and avoid congestion in the network.

- Step 3: Close the connection
  - When the data transfer is complete, the sender and the receiver need to close the connection using a four-way handshake.
  - The sender initiates the connection termination by sending a FIN (finish) segment to the receiver, which indicates that it has no more data to send.
  - The receiver acknowledges the FIN segment by sending an ACK segment back to the sender, which indicates that it has received the FIN segment.
  - The receiver also sends a FIN segment to the sender, which indicates that it has no more data to receive.
  - The sender acknowledges the FIN segment by sending an ACK segment back to the receiver, which indicates that it has received the FIN segment.
  - The connection is now closed and the resources are freed.