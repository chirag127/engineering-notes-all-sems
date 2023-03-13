RARP stands for Reverse Address Resolution Protocol, which is a protocol that allows a device to request its IP address from a gateway server based on its MAC address. RARP operates on the network access layer of the TCP/IP protocol stack and uses a specialized RARP server that listens for RARP requests on the same LAN. RARP was used for address assignment in the early years of 1980, but was later replaced by BOOTP.

#### RARP

The following diagram illustrates the basic architecture of a RARP:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   RARP Client   |    |   RARP Server   |    |   Other Hosts   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   MAC Address   |    |   MAC to IP     |    |   MAC Address   |
|                 |    |   Mapping       |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   IP Address    |    |   IP Address    |    |   IP Address    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   RARP Module   |    |   RARP Module   |    |   RARP Module   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Ethernet      |    |   Ethernet      |    |   Ethernet      |
|   Interface     |    |   Interface     |    |   Interface     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Ethernet      |    |   Ethernet      |    |   Ethernet      |
|   Cable         |    |   Cable         |    |   Cable         |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

The RARP process involves the following steps:

1. The RARP client broadcasts a RARP request packet to the LAN, containing its MAC address and a request for its IP address.
2. The RARP server receives the RARP request packet and looks up its MAC to IP mapping table to find the corresponding IP address for the RARP client.
3. The RARP server sends a RARP reply packet to the RARP client, containing its MAC address and the IP address assigned to it.
4. The RARP client receives the RARP reply packet and configures its IP address accordingly.