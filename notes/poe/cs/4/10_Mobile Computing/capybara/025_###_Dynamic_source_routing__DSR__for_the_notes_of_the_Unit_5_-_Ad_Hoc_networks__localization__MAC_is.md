### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing

Dynamic Source Routing (DSR) is a reactive routing protocol used in mobile ad hoc networks (MANETs). It is a type of on-demand routing protocol that allows nodes to dynamically discover routes to destinations within the network. In DSR, the source node determines the complete route to the destination node before sending the data packets.

#### Advantages of DSR
- DSR is a flexible and adaptable routing protocol that can handle frequent topology changes and node mobility in MANETs.
- It is a distributed routing protocol that does not require any centralized control or management.
- DSR is a loop-free routing protocol that avoids the formation of routing loops by maintaining a source route cache at each node.
- It provides efficient use of network resources by avoiding unnecessary broadcasts and reducing the overhead of maintaining routing tables.

#### Disadvantages of DSR
- DSR requires significant overhead due to the need to maintain source route caches at each node.
- The size of the source route cache can become very large in large-scale networks, which can lead to significant memory and processing overhead.
- DSR is vulnerable to attacks such as packet dropping, modification, and replay attacks due to the lack of authentication and verification mechanisms.

#### How DSR works
- When a source node wants to send a data packet to a destination node, it first checks its source route cache to see if it already has a route to the destination.
- If a route is not found in the source route cache, the source node initiates a route discovery process by broadcasting a route request packet (RREQ) to its neighbors.
- Each node that receives the RREQ packet either forwards it to its neighbors or responds with a route reply packet (RREP) if it already knows a route to the destination.
- The RREP packet contains the complete route from the source node to the destination node, which is then stored in the source route cache of each node along the path.
- Once the source node receives the RREP packet, it can send the data packet to the destination node using the route stored in its source route cache.

#### Mnemonic/Learning Trick
One possible mnemonic for remembering the working of DSR is "RREQ for route discovery, RREP for route reply, and SRC for source route cache."

#### Applications of DSR
- DSR is commonly used in military and emergency communication systems due to its ability to handle dynamic and unpredictable network topologies.
- It is also used in sensor networks and mobile robotic systems for efficient and flexible communication.

Overall, DSR is a robust and efficient routing protocol that is well-suited for mobile ad hoc networks. However, it has some limitations and vulnerabilities that must be addressed to ensure the security and reliability of the network.