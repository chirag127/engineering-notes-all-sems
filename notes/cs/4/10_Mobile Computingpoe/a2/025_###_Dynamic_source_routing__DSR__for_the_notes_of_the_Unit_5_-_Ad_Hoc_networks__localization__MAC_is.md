 Here is the content in markdown format for the topic ### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### Dynamic Source Routing (DSR)

- DSR is a simple and efficient routing protocol for wireless mesh networks.
- Each packet contains the complete, ordered list of addresses of the nodes used to route the packet from the source to the destination.
- Nodes use the routing information in the packet headers of received packets to learn and maintain routes to other nodes in the network.
- Route discovery is used to detect new routes and route maintenance is used to detect and remove broken routes.
- The key goals of DSR are to reduce the number of required broadcasts and to be self-configuring while maintaining good performance in the common case where source routes are available.
- Advantages:
    - Minimal overhead (little to no periodic beaconing). Only packets that actually need routing contain routing information.
    - Flexible and adapts quickly to changes.
    - Does not require global periodic route advertisements, sequence numbers, or timers.
    - Supports multiple routes.
- Disadvantages:
    - The routing header can become large for long source routes.
    - The memory requirements to store all discovered routes can be significant if many routes are discovered.
    - Relies on promiscuous packet reception, which may not be supported on all hardware.
- Use cases: Mobile ad hoc networks, wireless mesh networks.

Mnemonics/Learning tricks:
- DSR: Dynamic Source Routing
- SouRCe Route: The complete route is contained in packet headers
- Route Discovery and Route Maintenance
- Minimal overhead but large routing headers and memory requirements can be disadvantages

Does this help? Let me know if you would like me to elaborate on any of the points or add/modify anything.