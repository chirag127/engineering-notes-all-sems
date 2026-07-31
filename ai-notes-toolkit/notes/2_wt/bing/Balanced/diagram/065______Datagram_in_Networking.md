A datagram is a basic transfer unit associated with a packet-switched network. Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination. A datagram is an independent, self-contained message sent over the network whose arrival, arrival time, and content are not guaranteed.

#### Datagram in Networking

A datagram can be represented as follows:

```
+----------------+----------------+----------------+----------------+
| Source Address | Dest. Address  | Data Length    | Other Info     |
+----------------+----------------+----------------+----------------+
| Data                                                               |
|                                                                    |
|                                                                    |
+--------------------------------------------------------------------+
```

The header of a datagram typically contains the following fields:

- Source Address: The address of the sender of the datagram.
- Destination Address: The address of the intended receiver of the datagram.
- Data Length: The size of the data payload in bytes.
- Other Info: Any additional information that may be required for routing or processing the datagram, such as checksum, sequence number, protocol type, etc.

The data payload of a datagram contains the actual information that is being transmitted, such as text, image, audio, video, etc. The data payload may be fragmented into smaller pieces if the datagram size exceeds the maximum transmission unit (MTU) of the network.