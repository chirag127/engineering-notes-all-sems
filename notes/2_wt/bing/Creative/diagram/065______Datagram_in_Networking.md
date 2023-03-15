A datagram is a basic transfer unit associated with a packet-switched network. Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination. Datagrams provide a connectionless communication service across a packet-switched network.

#### Datagram in Networking

A datagram consists of two parts: a header and a payload. The header contains information such as the source and destination addresses, the protocol type, the length of the datagram, and other fields that help the network devices to process the datagram. The payload contains the actual data that is being transmitted.

A possible diagram of a datagram in networking is shown below:

```
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|    Source Address   |  Destination Address|    Protocol Type    |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|      Length         |      Checksum       |      Other Fields   |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     Payload (Data)       |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
|                     |                     |                     |
+---------------------+---------------------+---------------------+
```