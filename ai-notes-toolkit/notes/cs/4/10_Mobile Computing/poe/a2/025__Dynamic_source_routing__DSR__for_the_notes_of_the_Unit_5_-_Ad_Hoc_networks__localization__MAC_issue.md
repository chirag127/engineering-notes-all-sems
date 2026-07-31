 Here is the content in Markdown format without any feelings or friendliness, being formal and without any emojis or external links:

### Dynamic source routing (DSR) for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

- DSR is an on-demand routing protocol for mobile ad hoc networks.
- It allows nodes to dynamically discover a source route across multiple network hops to any destination in the network.
- Route discovery is performed when a node needs a route to a destination and does not already have one in its route cache.
- Route request (RREQ) packets are broadcast by the source to find the route.
- Route reply (RREP) packets are unicast in the reverse direction to establish the route.
- The discovered routes are cached by nodes for future use until they expire or are invalidated.
- DSR allows multiple routes to any destination to exist simultaneously, so that if a route breaks, other routes can be tried.
- The key advantage of DSR is that the route discovery process is on-demand, so that routes are only determined when needed. This leads to a reduction in network bandwidth usage and reduced latency.
- Some additional features of DSR include:
-- Use of source routing
-- Route caching
-- Route maintenance
-- Optional route shortening
-- Multiple route reply options
-- Flow id inclusion to differentiate datagram streams
- DSR is suited for use in multi-hop wireless ad hoc networks with rapidly changing network topology.