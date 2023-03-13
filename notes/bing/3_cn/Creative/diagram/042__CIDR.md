CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing. It replaces the previous classful network addressing architecture on the Internet, which was based on fixed-length network prefixes. CIDR allows variable-length network prefixes, which enables more efficient use of the IP address space and reduces the size of routing tables.

CIDR notation is a compact representation of an IP address and its associated network prefix. It consists of an IP address followed by a slash (/) and a number, which indicates the number of bits in the network prefix. For example, 192.168.1.0/24 represents the network prefix 192.168.1.0 with a 24-bit length, which covers the IP addresses from 192.168.1.0 to 192.168.1.255.

The following diagram illustrates the basic structure of a CIDR notation:

```
+-----------------+-----------------+-----------------+-----------------+
|   Network ID    |   Network ID    |   Network ID    |    Host ID      |
+-----------------+-----------------+-----------------+-----------------+
| 8 bits          | 8 bits          | 8 bits          | 8 bits          |
+-----------------+-----------------+-----------------+-----------------+
| 192             | 168             | 1               | 0               |
+-----------------+-----------------+-----------------+-----------------+
|<-------------------------- 24 bits -------------------------->|<----->|
|                           Network prefix                       | Host  |
|<---------------------------- 32 bits ------------------------------->|
|                           IP address                             |
+--------------------------------------------------------------------+
| 192.168.1.0/24                                                     |
+--------------------------------------------------------------------+
| CIDR notation                                                      |
+--------------------------------------------------------------------+
```