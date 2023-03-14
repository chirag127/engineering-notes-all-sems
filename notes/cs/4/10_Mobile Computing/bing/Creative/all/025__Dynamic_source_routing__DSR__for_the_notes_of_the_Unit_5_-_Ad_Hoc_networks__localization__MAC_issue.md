### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

- Dynamic source routing (DSR) is a simple and efficient routing protocol designed specifically for use in multi-hop wireless ad hoc networks of mobile nodes  .
- DSR allows the network to be completely self-organizing and self-configuring, without the need for any existing network infrastructure or administration  .
- DSR is composed of two mechanisms: Route Discovery and Route Maintenance, which work together to allow nodes to discover and maintain source routes to arbitrary destinations in the ad hoc network .
- DSR uses source routing, which means that each data packet carries in its header the complete, ordered list of nodes through which the packet must pass  .
- Source routing allows packet routing to be trivially loop-free, avoids the need for up-to-date routing information in the intermediate nodes, and allows nodes forwarding or overhearing packets to cache the routing information for their own future use  .
- DSR operates entirely on-demand, which means that the routing packet overhead of DSR scales automatically to only that needed to react to changes in the routes currently in use .

#### Route Discovery
- Route Discovery is the mechanism by which a node S wishing to send a packet to a destination D obtains a source route to D .
- Route Discovery is used only when S attempts to send a packet to D and does not already know a route to D .
- Route Discovery works as follows  :
  - S initiates Route Discovery by broadcasting a Route Request packet, which contains the address of D, a unique identification number, and a record of the address of each node through which this packet is forwarded.
  - Each node receiving the Route Request checks whether it knows of a route to D. If not, it appends its own address to the route record of the packet and forwards the packet along its outgoing links.
  - A Route Reply is generated when either D or a node that knows a route to D receives the Route Request. The Route Reply contains a copy of the route record from the Route Request, which is a source route from S to D.
  - The Route Reply is sent back to S along the reverse of the route record. Alternatively, if the node generating the Route Reply knows a source route to S, it may use that route instead of reversing the route record.
  - As the Route Reply is forwarded back to S, each node along the way caches the source route to D for its own future use.
  - S can send its data packets to D once it receives the Route Reply. S also caches the source route to D for its own future use.

#### Route Maintenance
- Route Maintenance is the mechanism by which a node S detects if the network topology has changed such that it can no longer use its source route to D because a link along the route no longer works .
- Route Maintenance is used only when S is actually sending packets to D .
- Route Maintenance works as follows  :
  - When a node encounters a fatal transmission problem at its data link layer along the source route, it removes the link from its cache and generates a Route Error packet, which contains the addresses of the two nodes at the endpoints of the broken link.
  - The Route Error is sent back to S along the reverse of the source route, and each node forwarding the Route Error also removes the link from its cache.
  - When S receives the Route Error, it also removes the link from its cache and initiates Route Discovery again if it still needs a route to D.

#### Advantages of DSR
- DSR has the following advantages   :
  - It eliminates the need for periodic route advertisements, which reduces the network bandwidth overhead and conserves the battery power of the nodes.
  - It allows multiple routes to any destination, which increases the robustness and load balancing of the network.
  - It supports