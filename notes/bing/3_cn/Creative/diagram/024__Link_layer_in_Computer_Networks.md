The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer or layer 2 in the OSI model of computer networking. The link layer is responsible for transferring data between nodes on a network segment across the physical layer, and for providing error control and addressing functions.

The link layer can be divided into two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer. The LLC sublayer provides services such as flow control, error detection and correction, and multiplexing to the upper layers. The MAC sublayer handles the access to the shared medium, such as Ethernet, Wi-Fi, or Bluetooth.

The following diagram illustrates the basic architecture of the link layer in computer networks:

```
+-----------------+    +-----------------+    +-----------------+
|   Application   |    |   Application   |    |   Application   |
+-----------------+    +-----------------+    +-----------------+
|    Transport    |    |    Transport    |    |    Transport    |
+-----------------+    +-----------------+    +-----------------+
|    Network      |    |    Network      |    |    Network      |
+-----------------+    +-----------------+    +-----------------+
| Logical Link    |    | Logical Link    |    | Logical Link    |
| Control (LLC)   |    | Control (LLC)   |    | Control (LLC)   |
+-----------------+    +-----------------+    +-----------------+
| Media Access    |    | Media Access    |    | Media Access    |
| Control (MAC)   |    | Control (MAC)   |    | Control (MAC)   |
+-----------------+    +-----------------+    +-----------------+
|    Physical     |    |    Physical     |    |    Physical     |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Node A      |    |     Node B      |    |     Node C      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|     Link 1      |----|     Link 2      |----|     Link 3      |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```