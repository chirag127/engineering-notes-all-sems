Static and dynamic routing are two methods used to determine how to send a packet toward its destination. Static routes are configured in advance of any network communication by a network administrator. Dynamic routes are learned by routers using routing protocols that exchange information with other routers.

The following diagram illustrates the basic architecture of a static and dynamic routing in cn using ASCII characters:

```
+-----+     +-----+     +-----+     +-----+
| R1  |     | R2  |     | R3  |     | R4  |
+-----+     +-----+     +-----+     +-----+
|     |     |     |     |     |     |     |
|     |     |     |     |     |     |     |
+-----+     +-----+     +-----+     +-----+
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
   |           |           |           |
+-----+     +-----+     +-----+     +-----+
| PC1 |     | PC2 |     | PC3 |     | PC4 |
+-----+     +-----+     +-----+     +-----+

Static routing:

R1 has a static route to PC4 via R2 and R4
R2 has a static route to PC3 via R3
R3 has a static route to PC1 via R2 and R1
R4 has a static route to PC2 via R3 and R2

Dynamic routing:

R1, R2, R3 and R4 are running a dynamic routing protocol such as OSPF or EIGRP
They exchange routing information with each other and learn the best paths to all destinations
They update their routing tables accordingly and forward packets based on the dynamic routes
```