Process-to-process delivery in transport layer is the delivery of a packet, part of a message, from one process to another. A process is an entity of the application layer that uses the services of the transport layer. Two processes can communicate using the client/server paradigm.

The transport layer is responsible for identifying the processes and creating a logical connection between them. The transport layer uses port numbers to identify the processes and segment numbers to identify the packets. The transport layer also provides reliable or unreliable delivery, flow control, error control, and congestion control  .

The following diagram shows an example of process-to-process delivery in transport layer:

### Process-to-process delivery in transport layer
```
+----------------+    +----------------+    +----------------+
| Application    |    | Application    |    | Application    |
| Layer          |    | Layer          |    | Layer          |
+----------------+    +----------------+    +----------------+
| Transport      |    | Transport      |    | Transport      |
| Layer          |    | Layer          |    | Layer          |
+----------------+    +----------------+    +----------------+
| Network        |    | Network        |    | Network        |
| Layer          |    | Layer          |    | Layer          |
+----------------+    +----------------+    +----------------+
| Data Link      |    | Data Link      |    | Data Link      |
| Layer          |    | Layer          |    | Layer          |
+----------------+    +----------------+    +----------------+
| Physical       |    | Physical       |    | Physical       |
| Layer          |    | Layer          |    | Layer          |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|     Host A     |    |     Router     |    |     Host B     |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Process A    |    |                |    |   Process B    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Port 80      |    |                |    |   Port 8080    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Segment 1    |    |   Segment 1    |    |   Segment 1    |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Datagram 1   |    |   Datagram 1   |    |   Datagram 1   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Frame 1      |    |   Frame 1      |    |   Frame 1      |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|   Bit Stream   |    |   Bit Stream   |    |   Bit Stream   |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```