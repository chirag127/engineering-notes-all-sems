 Here is the content written in markdown format on the topic ### Static and dynamic routing in cn:

### Static Routing

- Routes are determined based on the network topology and assigned manually.
- Routing tables are static and do not change unless manually updated.
- Examples:
    - Small networks with a few routes.
    - Used when network traffic is predictable.

Advantages:

- Simple to configure.
- Resources required are less as routes are predefined.

Disadvantages:

- Cannot adapt to changes in topology or traffic patterns.
- Administrative overhead to update routes manually.

### Dynamic Routing

- Routes are determined automatically based on routing algorithms and topology changes.
- Routing tables are dynamically updated.
- Examples:
    - Large and complex networks.
    - Used when network traffic is unpredictable.

Advantages:

- Can adapt to changes in topology or traffic patterns.
- No administrative overhead to update routes manually.

Disadvantages:

- More complex to configure.
- Require more resources to calculate and update routes continuously.

Some common dynamic routing protocols are:

- RIP (Routing Information Protocol)
- OSPF (Open Shortest Path First)
- BGP (Border Gateway Protocol)

Applications:

- Dynamic routing is preferred for large and complex networks as it is more scalable and resilient to changes.
- Static routing can be used for small networks to avoid complexity. It can also be used as a fallback when dynamic routing fails.

[Detailed diagrams and examples can be added here to aid learning.]