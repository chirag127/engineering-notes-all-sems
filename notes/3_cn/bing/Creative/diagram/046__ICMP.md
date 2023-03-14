The Internet Control Message Protocol (ICMP) is a network layer protocol that is used for error reporting and diagnostic purposes. It is also used by some network utilities such as ping and traceroute. ICMP messages are encapsulated inside IP datagrams and have a specific format that includes a type, a code, a checksum and a data field. The type and code fields indicate the purpose and subtype of the ICMP message, such as destination unreachable, echo request, echo reply, time exceeded, etc. The checksum field is used to verify the integrity of the message. The data field may contain additional information depending on the type and code of the message, such as the original IP header and the first 8 bytes of the original datagram.

The following diagram illustrates the basic structure of an ICMP message:

```
+----------------+----------------+----------------+----------------+
|     Type       |      Code      |     Checksum   |                |
+----------------+----------------+----------------+                +
|                                                               Data
+----------------+----------------+----------------+----------------+
```

The following diagram illustrates an example of an ICMP echo request message, which is used by the ping utility to test the connectivity between two hosts. The type field is set to 8, the code field is set to 0, the checksum field is calculated based on the entire message, and the data field contains an identifier, a sequence number and a payload.

```
+----------------+----------------+----------------+----------------+
|       8        |       0        |     Checksum   |                |
+----------------+----------------+----------------+                +
|    Identifier  |   Sequence No. |                                |
+----------------+----------------+                                +
|                                                               Payload
+----------------+----------------+----------------+----------------+
```

The following diagram illustrates an example of an ICMP destination unreachable message, which is used by a router to inform the source host that the destination host or network is unreachable. The type field is set to 3, the code field is set to a value between 0 and 15 depending on the reason for the unreachability, the checksum field is calculated based on the entire message, and the data field contains the original IP header and the first 8 bytes of the original datagram that caused the error.

```
+----------------+----------------+----------------+----------------+
|       3        |       Code     |     Checksum   |                |
+----------------+----------------+----------------+                +
|                                                               Unused
+----------------+----------------+----------------+----------------+
|                                                               Original IP Header
+----------------+----------------+----------------+----------------+
|                                                               First 8 Bytes of Original Datagram
+----------------+----------------+----------------+----------------+
```