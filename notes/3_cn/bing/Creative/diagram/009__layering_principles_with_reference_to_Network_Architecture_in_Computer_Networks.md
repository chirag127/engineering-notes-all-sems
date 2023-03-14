The layering principles with reference to network architecture in computer networks are based on the idea of dividing the communication process into smaller and simpler components, each performing a specific function and interacting with each other through well-defined interfaces. The layering principles allow for modularity, interoperability, scalability, and flexibility of network design and implementation. The most widely used network architecture models are the OSI model and the TCP/IP model, which have different numbers and names of layers, but share some common concepts and functions.

The following ASCII diagram illustrates the basic architecture of a network using the OSI model, which has seven layers: physical, data link, network, transport, session, presentation, and application. Each layer is represented by a box with its name and function, and the arrows indicate the direction of data flow between the layers.

```
+-----------------+    +-----------------+
| Application     |    | Application     |
| (User services) |    | (User services) |
+-----------------+    +-----------------+
| Presentation    |    | Presentation    |
| (Data format)   |    | (Data format)   |
+-----------------+    +-----------------+
| Session         |    | Session         |
| (Dialog control)|    | (Dialog control)|
+-----------------+    +-----------------+
| Transport       |    | Transport       |
| (Reliable data) |    | (Reliable data) |
+-----------------+    +-----------------+
| Network         |    | Network         |
| (Routing)       |    | (Routing)       |
+-----------------+    +-----------------+
| Data link       |    | Data link       |
| (Framing)       |    | (Framing)       |
+-----------------+    +-----------------+
| Physical        |    | Physical        |
| (Signal)        |    | (Signal)        |
+-----------------+    +-----------------+
|                 |    |                 |
|      Node A     |----|      Node B     |
|                 |    |                 |
+-----------------+    +-----------------+
```