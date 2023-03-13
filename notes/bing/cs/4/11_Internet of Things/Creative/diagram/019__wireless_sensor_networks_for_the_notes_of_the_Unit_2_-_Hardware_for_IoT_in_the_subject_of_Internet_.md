A wireless sensor network (WSN) is a network of distributed devices that can sense and communicate data about the physical environment. A WSN typically consists of sensor nodes, a base station, and optional relay nodes. The sensor nodes are small, low-power, and wireless devices that can collect and transmit data to the base station or other sensor nodes. The base station is a central node that can communicate with the sensor nodes and the external network. The relay nodes are intermediate nodes that can forward data from the sensor nodes to the base station or other relay nodes.

The following diagram illustrates the basic architecture of a wireless sensor network using ASCII art:

```
    +-----------------+        +-----------------+
    | External Network|        | External Network|
    +-----------------+        +-----------------+
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
            |                           |
+-----------------+        +-----------------+
|    Base Station |        |    Base Station |
+-----------------+        +-----------------+
    /       |       \          /       |       \
   /        |        \        /        |        \
  /         |         \      /         |         \
 /          |          \    /          |          \
+---+    +---+      +---+  +---+    +---+      +---+
| R |    | R |      | R |  | R |    | R |      | R |
+---+    +---+      +---+  +---+    +---+      +---+
 /|\      /|\        /|\    /|\      /|\        /|\
  |        |          |      |        |          |
  |        |          |      |        |          |
  |        |          |      |        |          |
+---+    +---+      +---+  +---+    +---+      +---+
| S |    | S |      | S |  | S |    | S |      | S |
+---+    +---+      +---+  +---+    +---+      +---+

S: Sensor Node
R: Relay Node
```