 Here is the content in markdown format without any emojis or external links:

## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR),

Ad Hoc networks:

- Self organizing network without any infrastructure
- Nodes are mobile and can join/leave the network dynamically
- Nodes act as routers and forward packets for other nodes
- Challenges: Dynamic topology, limited bandwidth, energy constraint

Localization:

- Determining the position of nodes in an ad hoc network
- Required for routing, tracking mobile nodes and other location based services
- Methods: Range based (using connectivity/RSSI), Range free (using hop count), Hybrid

MAC issues:

- Hidden terminal problem: When a node is visible to the receiver but not the sender
- Exposed terminal problem: When a node refrains from sending due to an ongoing transmission that it cannot sense
- deafness: When a node cannot sense an ongoing transmission
- Capture effect: When a stronger signal overrides a weak ongoing transmission

Routing protocols:

- Table driven: Maintain consistent routing tables, low latency but high overhead
- On demand: Create routes only when needed, low overhead but high latency
- Hierarchical: Cluster formation to create a hierarchy, efficient for large networks
- Geography based: Use location info to route packets

Global state routing (GSR):

- Maintains global view of the network to provide optimized routes
- Difficult to implement due to scale and dynamics of ad hoc networks
- Approaches: Hierarchical, distributed

Does this look okay? Let me know if you would like me to modify or add anything.