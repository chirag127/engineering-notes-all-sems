Static and dynamic routing are two methods of determining how to send packets toward their destinations in a computer network. Static routing is manually configured by a network administrator, while dynamic routing is automatically learned and updated by routers using routing protocols.

The following diagram illustrates the basic architecture of a static and dynamic routing network:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Router A      |     |  Router B      |     |  Router C      |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Static route  |     |  Dynamic route |     |  Static route  |
|  to network X  |     |  to network X  |     |  to network X  |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Network Y     |     |  Network Z     |     |  Network X     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

In this diagram, Router A and Router C have static routes configured to reach network X, which is connected to Router C. Router B has a dynamic route to network X, which it learned from Router C using a routing protocol. Router B can also advertise network X to Router A using the same protocol, so Router A can have an alternative path to network X in case of a link failure. Router B can also learn about network Y and network Z from Router A and Router C, respectively, and update its routing table accordingly.