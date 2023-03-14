 Here is the content on ### Static and dynamic routing in cn in markdown format:

### Static and dynamic routing in cn

Static routing:
- Predefined routes are configured manually.
- Routes do not change unless manually reconfigured.
- Good for small networks with predictable traffic patterns.

Mnemonic: Think of static as fixed, unchanged.

Dynamic routing:
- Routes are automatically updated based on network changes.
- Routers exchange routing information with other routers using routing protocols.
- Good for large, complex networks with unpredictable traffic patterns.
- Examples: RIP, OSPF, BGP.

Advantages of dynamic routing:
- Auto adjustment to topology changes like link failures or new connections.
- Utilization of multiple paths to destination.
- Optimal path selection based on various path attributes.

Disadvantages of dynamic routing:
- Additional overhead on routers to maintain and exchange routing information.
- Complexity in configuring and debugging routing protocols.
- Vulnerable to routing loops and other issues if not configured properly.

When to use static vs dynamic routing:
- For small networks with simple topology and static traffic patterns, use static routing.
- For large networks with complex topology and dynamic traffic patterns, use dynamic routing.
- Can also use hybrid approach with static default route and dynamic routing for the rest of the network.

[Include diagrams and examples here if helpful for learning]

Applications: Both static and dynamic routing are commonly used in networking for efficient forwarding of packets between networks based on logical addressing.