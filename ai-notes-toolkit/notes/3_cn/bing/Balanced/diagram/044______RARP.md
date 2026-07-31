RARP stands for Reverse Address Resolution Protocol. It is a protocol that allows a client computer to request its IP address from a gateway server's ARP table or cache. The client computer sends its MAC address to the server, and the server responds with the corresponding IP address. RARP is useful for devices that do not have a permanent IP address, such as diskless workstations.

#### RARP

```
+-----------------+     +-----------------+     +-----------------+
| Client computer |     | Gateway server  |     | RARP server     |
| MAC: 00-11-22   |     | MAC: 33-44-55   |     | MAC: 66-77-88   |
| IP: unknown     |     | IP: 192.168.1.1 |     | IP: 192.168.1.2 |
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
       | RARP request        |                      |
       | MAC: 00-11-22       |                      |
       | IP: unknown         |                      |
       +--------------------->|                      |
       |                      | RARP request        |
       |                      | MAC: 00-11-22       |
       |                      | IP: unknown         |
       |                      +--------------------->|
       |                      |                      | Lookup MAC in ARP table
       |                      |                      | MAC: 00-11-22
       |                      |                      | IP: 192.168.1.100
       |                      |                      |
       |                      | RARP reply          |
       |                      | MAC: 00-11-22       |
       |                      | IP: 192.168.1.100   |
       |                      |<---------------------+
       | RARP reply          |                      |
       | MAC: 00-11-22       |                      |
       | IP: 192.168.1.100   |                      |
       |<---------------------+                      |
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
+-----------------+     +-----------------+     +-----------------+
| Client computer |     | Gateway server  |     | RARP server     |
| MAC: 00-11-22   |     | MAC: 33-44-55   |     | MAC: 66-77-88   |
| IP: 192.168.1.100|     | IP: 192.168.1.1 |     | IP: 192.168.1.2 |
+-----------------+     +-----------------+     +-----------------+
```