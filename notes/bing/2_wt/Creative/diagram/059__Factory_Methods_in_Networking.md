Factory Methods in Networking are a design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. This pattern is useful when the type of objects to be created depends on the network environment, such as the protocol, the topology, or the device level.

#### Factory Methods in Networking

```
+-----------------+      +-----------------+      +-----------------+
| Enterprise      |      | Control         |      | Device          |
| Level           |      | Level           |      | Level           |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | Application | |      | | Application | |      | | Application | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|       |         |      |       |         |      |       |         |
|       |         |      |       |         |      |       |         |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | HTTP, FTP, | |      | | TCP, UDP    | |      | | IP          | |
| | SNMP       | |      | +-------------+ |      | +-------------+ |
| +-------------+ |      |       |         |      |       |         |
|       |         |      |       |         |      |       |         |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | TCP, UDP    | |      | | Ethernet    | |      | | Ethernet    | |
| +-------------+ |      | +-------------+ |      | +-------------+ |
|       |         |      |       |         |      |       |         |
| +-------------+ |      | +-------------+ |      | +-------------+ |
| | IP          | |      | | Physical    | |      | | Physical    | |
| +-------------+ |      | | Transmission| |      | | Transmission| |
|       |         |      | | Technology  | |      | | Technology  | |
+-------|---------+      +-------|---------+      +-------|---------+
        |                      |                      |
        |                      |                      |
        +----------------------+----------------------+
                               |
                               |
                               |
                           +---|---+
                           |       |
                           |  WAN  |
                           |       |
                           +-------+
```