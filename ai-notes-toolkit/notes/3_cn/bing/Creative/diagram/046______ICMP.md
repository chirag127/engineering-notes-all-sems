#### ICMP
ICMP stands for Internet Control Message Protocol. It is a network layer protocol that is used for error handling and diagnostic purposes. ICMP messages are transmitted as datagrams that are encapsulated inside IP packets. ICMP messages have a header that appears after the IP header and contains the following fields:

- Type: 8 bits, specifies the type of ICMP message
- Code: 8 bits, specifies the subtype of ICMP message
- Checksum: 16 bits, used for error detection
- Data: variable length, contains additional information depending on the type and code of ICMP message

The following diagram shows the format of an ICMP header and an example of an ICMP echo request message:

```
+-----------------+-----------------+-----------------+-----------------+
|   IP Header     |   IP Header     |   IP Header     |   IP Header     |
+-----------------+-----------------+-----------------+-----------------+
| Type (8 bits)   | Code (8 bits)   | Checksum (16 bits)                |
+-----------------+-----------------+-----------------+-----------------+
| Identifier (16 bits)              | Sequence Number (16 bits)         |
+-----------------+-----------------+-----------------+-----------------+
| Data (variable length)                                            |
+-------------------------------------------------------------------+

Example: ICMP echo request

+-----------------+-----------------+-----------------+-----------------+
|   IP Header     |   IP Header     |   IP Header     |   IP Header     |
+-----------------+-----------------+-----------------+-----------------+
| Type = 8        | Code = 0        | Checksum                            |
+-----------------+-----------------+-----------------+-----------------+
| Identifier                          | Sequence Number                     |
+-----------------+-----------------+-----------------+-----------------+
| Data (optional)                                                    |
+-------------------------------------------------------------------+
```