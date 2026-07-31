# Network Protocol- Data Dissemination

- Data dissemination is the process of delivering data that matches the interest of the querying nodes in a network.
- Data dissemination is essential for IoT applications that generate massive amounts of data from various sensors and devices.
- Data dissemination protocols aim to provide efficient, reliable, secure and scalable data delivery in IoT networks.
- Data dissemination protocols can be classified into two categories: broadcast and query-based.

## Broadcast Protocols

- Broadcast protocols disseminate data to all nodes in the network without requiring any query from the nodes.
- Broadcast protocols can be further divided into deterministic and probabilistic protocols.
- Deterministic protocols use fixed rules to determine which nodes should forward the data packets to their neighbors, such as flooding, gossiping, or geographic routing.
- Probabilistic protocols use random decisions to select the forwarding nodes, such as random walk, epidemic routing, or neighbor-based routing.
- Broadcast protocols have the advantages of simplicity, robustness, and low latency, but they also have the drawbacks of high overhead, redundancy, and low reliability.

## Query-based Protocols

- Query-based protocols disseminate data to the nodes that express their interest in a given data type by specifying a query message, which then propagates through the network.
- Query-based protocols can be further divided into pull and push protocols.
- Pull protocols allow the nodes to request the data they need from the data sources or the intermediate nodes, such as directed diffusion, SPIN, or COUGAR.
- Push protocols allow the data sources or the intermediate nodes to proactively send the data to the interested nodes, such as TAG, TinyDB, or DSWare.
- Query-based protocols have the advantages of low overhead, high reliability, and high accuracy, but they also have the drawbacks of high latency, complexity, and scalability issues.