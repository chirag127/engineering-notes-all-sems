The following is a detailed ASCII diagram for Dynamic Source Routing (DSR) protocol for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing.

```
DSR is an on-demand protocol that uses source routing to discover and maintain routes in ad hoc wireless networks.

Source routing means that the sender of a packet determines the complete sequence of nodes through which the packet has to pass. The sender explicitly lists this route in the packet's header, identifying each forwarding hop by the address of the next node to which to transmit the packet on its way to the destination host.

DSR consists of two main mechanisms: Route Discovery and Route Maintenance.

Route Discovery is the process by which a node S wishing to send a packet to a destination node D obtains a source route to D. Route Discovery is used only when S attempts to send a packet to D and does not already know a route to D.

Route Maintenance is the process by which node S is able to detect, while using a source route to D, if the network topology has changed such that it can no longer use its route to D because a link along the route no longer works. When Route Maintenance indicates a source route is broken, S can attempt to use any other route it happens to know to D, or can invoke Route Discovery again to find a new route for subsequent packets to D. Route Maintenance is used only when S is actually sending packets to D.

The following diagram illustrates the basic architecture of DSR:

+-----+     +-----+     +-----+     +-----+     +-----+
|  S  |-----|  A  |-----|  B  |-----|  C  |-----|  D  |
+-----+     +-----+     +-----+     +-----+     +-----+

S: Source node
D: Destination node
A, B, C: Intermediate nodes

When S wants to send a packet to D, it first checks its route cache for a source route to D. If it finds one, it uses it to send the packet. If it does not find one, it initiates Route Discovery by broadcasting a Route Request packet. The Route Request contains the address of the destination (D), the address of the source (S), and a unique identification number.

Each node that receives the Route Request checks to see if it knows of a route to the destination. If it does not, it appends its own address to the route record of the packet and then forwards the packet along its outgoing links. If it does know of a route to the destination, it returns a Route Reply to the source node using the route record in the Route Request. The Route Reply contains the copy of the route record from the Route Request, along with any additional route information known by the node generating the Route Reply.

For example, suppose node A receives the Route Request from S. Node A does not know of a route to D, so it appends its address to the route record and forwards the packet to B. Node B also does not know of a route to D, so it appends its address to the route record and forwards the packet to C. Node C knows of a route to D, so it returns a Route Reply to S using the route record [S,A,B,C] and appending the address of D. The Route Reply contains the route [S,A,B,C,D] which S can use to send packets to D.

When S receives the Route Reply, it caches the route in its route cache for future use. It also reverses the route and caches it for sending packets to C or any intermediate nodes along the route.

If a link in the source route breaks, the node upstream of the break can send a Route Error message to the source node, indicating the link that failed. The source node can then remove the link from its cache and try another route or initiate Route Discovery again.

For example, suppose the link between B and C breaks while S is sending packets to D using the route [S,A,B,C,D]. Node B detects the link failure and sends a Route Error to S, indicating that the link (B,C) is broken. Node S removes the link (B,C) from its cache and checks for another route to D. If it does not find one, it initiates Route Discovery again.
```