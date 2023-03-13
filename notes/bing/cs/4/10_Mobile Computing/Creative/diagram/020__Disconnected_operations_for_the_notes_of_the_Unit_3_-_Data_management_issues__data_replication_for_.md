Disconnected operations for mobile computing are a technique that allows users to access and modify data stored on remote servers even when the network connection is unavailable or unreliable. This is achieved by using a local cache on the mobile device that stores a subset of the data and synchronizes it with the server when the connection is restored. The main challenges of this technique are how to handle conflicts, how to ensure consistency, and how to optimize the use of network bandwidth and battery power.

A possible diagram for disconnected operations for mobile computing is shown below, using ASCII characters. The diagram assumes a client-server architecture, where the mobile device is the client and the remote server is the server. The diagram also shows the components of the Coda file system, which is an example of a system that supports disconnected operations for mobile computing .

### Disconnected operations for mobile computing

```
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Mobile device   |        |  Wireless network|        |  Remote server   |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  +------------+  |        |                  |        |  +------------+  |
|  |            |  |        |                  |        |  |            |  |
|  |  Coda      |  |        |                  |        |  |  Coda      |  |
|  |  Venus     |  |        |                  |        |  |  Vice      |  |
|  |  (client)  |  |        |                  |        |  |  (server)  |  |
|  |            |  |        |                  |        |  |            |  |
|  +------------+  |        |                  |        |  +------------+  |
|  |            |  |        |                  |        |  |            |  |
|  |  Local     |  |        |                  |        |  |  Remote    |  |
|  |  cache     |  |        |                  |        |  |  data      |  |
|  |            |  |        |                  |        |  |            |  |
|  +------------+  |        |                  |        |  +------------+  |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Disconnected   |        |  Connected       |        |  Connected       |
|  operation      |<------>|  operation       |<------>|  operation      |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
```