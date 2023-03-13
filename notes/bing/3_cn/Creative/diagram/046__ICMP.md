ICMP stands for Internet Control Message Protocol. It is a network layer protocol used for error handling and diagnostic purposes. ICMP messages are encapsulated inside IP datagrams and have a specific format that includes a type, a code, a checksum, and optional data fields. The type and code fields indicate the purpose and the nature of the ICMP message, such as echo request, echo reply, destination unreachable, time exceeded, etc. The checksum field is used to verify the integrity of the ICMP message. The data field may contain additional information relevant to the ICMP message, such as the original IP header, the timestamp, the identifier, etc.

#### ICMP

```
+-----------------+-----------------+-----------------+-----------------+
|     Type (8)    |     Code (8)    |   Checksum (16) |      Data       |
+-----------------+-----------------+-----------------+-----------------+
|                                                               |
|                            Data (variable)                    |
|                                                               |
+---------------------------------------------------------------+
```