 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Temporary ordered routing algorithm (TORA)

- TORA is a link-state routing protocol designed for ad-hoc networks.
- It is an on-demand routing protocol which establishes routes only when needed.
- TORA maintains multiple routes to each destination to provide robustness and fast convergence in the face of topological changes.
- TORA organizes nodes into directed acyclic graph (DAG) rooted at the destination.
- The DAG is created and maintained through the periodic transmission of query packets from nodes to their downstream neighbors.
- When a node has data to send, it retrieves the DAG information for the destination and uses it to determine and select the most appropriate next hop.
- The key features of TORA are its localized route creation and maintenance.
- Only nodes in the vicinity of a topological change need to react to the change. This results in significantly reduced routing overhead.
- However, TORA may suffer from oscillation in some scenarios and can result in high latency before new routes are found.

The above content summarizes the key points about Temporary ordered routing algorithm (TORA) for ad-hoc networks. The points are written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.