 Here is the content in markdown format for the topic -

### Basic internetworking in network layer

1. Internetworking is the concept of connecting multiple individual networks to form an internetwork using devices called routers.
2. Routers have two or more network interfaces, each connected to a different network. The router forwards packets between networks based on network layer addressing information.
3. For two hosts on different networks to communicate, they must have IP addresses on the same subnet. The router maintains a routing table that contains the subnet numbers and interfaces to reach them. When a packet is received, the router examines the destination IP address and forwards the packet out the appropriate interface towards the destination network.
4. For example, Host A on Network 1 sends a packet to Host B on Network 2. The router receives the packet on its Network 1 interface and checks the routing table. It sees the packet is destined for Network 2 and forwards the packet out its Network 2 interface. Host B then receives the packet. This process works in reverse for packets sent from Host B to Host A.
5. Advantages of internetworking -
    - Resource sharing - Resources such as servers and printers can be shared across networks.
    - Scalability - The network can be easily expanded by adding more networks and routers.
    - Reliability - If one network goes down, traffic can be routed around it to the destination.
    - Economy of scale - It is cheaper to connect existing LANs into a larger internetwork than to replace everything with a single large network.

[Diagrams and examples can be added here to aid learning]

The content covers the key points around internetworking at the network layer with routers, routing tables, forwarding packets between networks, advantages, etc. Let me know if you would like me to elaborate on any part or add more details.