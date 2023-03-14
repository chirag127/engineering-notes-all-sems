The link layer in the Internet protocol suite is the lowest layer that operates on the local network segment (link) that a host is physically connected to. It is responsible for transferring data frames between nodes on the same link, and may also provide error detection and correction. The link layer can be divided into two sublayers: the media access control (MAC) sublayer and the logical link control (LLC) sublayer. The MAC sublayer handles the access to the shared medium, such as Ethernet or Wi-Fi, and the LLC sublayer provides flow control and multiplexing for different network protocols.  

The following diagram illustrates the basic architecture of a link layer in a computer network:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Application   |    |   Application   |    |   Application   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Transport    |    |    Transport    |    |    Transport    |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Network     |    |     Network     |    |     Network     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Logical Link    |    | Logical Link    |    | Logical Link    |
|   Control (LLC) |    |   Control (LLC) |    |   Control (LLC) |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| Media Access    |    | Media Access    |    | Media Access    |
|  Control (MAC)  |    |  Control (MAC)  |    |  Control (MAC)  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|    Physical     |    |    Physical     |    |    Physical     |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       | | | |          | | | | | | | | |          | | | |
       | | | +----------+ | | | | | | +----------+ | | |
       | | +--------------+ | | | | +--------------+ | |
       | +------------------+ | | +------------------+ |
       +----------------------+ +----------------------+
```