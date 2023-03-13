
### Temporary Ordered Routing Algorithm (TORA)

TORA is a distributed routing algorithm used in Ad Hoc networks that is based on the concept of link reversal. It is an extension of the [Distance Vector Routing Protocol (DVRP)](https://en.wikipedia.org/wiki/Distance-vector_routing_protocol). It is used to provide efficient routing in networks with highly dynamic topologies and is particularly useful in networks with mobile nodes.

#### Overview of TORA

TORA is a source-initiated, link-state routing protocol. It is a distributed routing algorithm that uses a hierarchical structure to enable nodes to quickly respond to changes in the network topology. TORA is designed to be robust in the face of link failures and to provide efficient routing in networks with highly dynamic topologies.

TORA works by maintaining a directed acyclic graph (DAG) of the network topology. Each node in the network maintains a local view of the DAG and uses it to determine the best route to any given destination. When a link fails, the nodes in the network update their local views of the DAG to reflect the new topology. This enables them to quickly respond to changes in the network topology and find an alternate route to the destination.

#### Advantages of TORA

- TORA is a distributed routing algorithm, which means that it does not require a centralized controller. This makes it well-suited for networks with mobile nodes.
- TORA is a source-initiated protocol, which means that it is not reliant on periodic updates from a centralized controller. This makes it more efficient and reliable in networks with highly dynamic topologies.
- TORA is designed to be robust in the face of link failures. It is able to quickly respond to changes in the network topology and find an alternate route to the destination.
- TORA is able to maintain a consistent view of the network topology, even in the presence of link failures. This makes it more reliable than other routing protocols, such as DVRP.

#### Disadvantages of TORA

- TORA is a complex routing algorithm, which makes it more difficult to implement and debug than simpler algorithms.
- TORA is not well-suited for networks with a large number of nodes, as it can become inefficient in such networks.
- TORA is not well-suited for networks with a high degree of mobility, as it can become inefficient in such networks.
- TORA is not well-suited for networks with a high degree of latency, as it can become inefficient in such networks.

#### Mnemonics and Learning Tricks

- **T**emporary **O**rdered **R**outing **A**lgorithm
- **T**opology **O**bservation **R**outing **A**lgorithm
- **T**opology **O**bservation **R**outing **A**rchitecture