RARP stands for Reverse Address Resolution Protocol, which is a protocol used by a client computer to request its IP address from a gateway server's Address Resolution Protocol table or cache . The client sends its physical or MAC address to the RARP server, which then returns the IP address assigned to that MAC address  .

#### RARP

The following diagram illustrates the basic architecture of a RARP:

```
+-----------------+     +-----------------+     +-----------------+
| RARP client     |     | RARP server     |     | Other device    |
| MAC: AA:BB:CC   |     | MAC: DD:EE:FF   |     | MAC: GG:HH:II   |
| IP: ?           |     | IP: 192.168.1.1 |     | IP: 192.168.1.2 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+------+---------------------+---------------------+------+
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
|      |                     |                     |      |
+---------------------------------------------------------+
|                                                         |
|                      Ethernet network                   |
|                                                         |
+---------------------------------------------------------+

```

The RARP process is as follows  :

1. The RARP client broadcasts a RARP request with its MAC address and requests an IP address it can use.
2. The RARP server receives the RARP request and looks up its RARP table to find the IP address associated with the MAC address of the client.
3. The RARP server sends a RARP reply with the IP address of the client to the client.
4. The RARP client receives the RARP reply and configures its IP address accordingly.