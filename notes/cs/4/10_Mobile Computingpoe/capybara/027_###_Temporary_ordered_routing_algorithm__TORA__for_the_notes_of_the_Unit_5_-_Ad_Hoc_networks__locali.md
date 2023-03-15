### Temporary Ordered Routing Algorithm (TORA)

Temporary Ordered Routing Algorithm (TORA) is a distributed routing protocol developed for ad-hoc networks. It is a reactive protocol that only establishes a route when it is needed. TORA is designed to be highly adaptive and scalable, making it suitable for use in large ad-hoc networks.

#### Advantages of TORA

- TORA is highly adaptive, making it suitable for use in dynamic ad-hoc networks.
- It is scalable and can be used in large networks.
- The protocol is distributed, making it easy to deploy without a central authority.
- TORA is designed to be fault-tolerant, ensuring that the network remains operational even in the presence of node failures.

#### Disadvantages of TORA

- The protocol requires a lot of overhead, which can result in high energy consumption.
- TORA is not suitable for use in networks with high mobility, as the frequent route changes can cause excessive overhead and delays.
- The protocol is not very secure, as it does not provide any mechanisms for authentication or encryption.

#### TORA Algorithm

- TORA is a distance-vector routing protocol that uses a three-phase process to establish routes.
- The first phase involves the creation of a directed acyclic graph (DAG) that represents the network topology.
- In the second phase, each node computes its distance to the destination node using the DAG.
- Finally, in the third phase, each node selects the shortest path to the destination node and forwards the data packet along that path.

#### Learning Tricks for TORA

Unfortunately, there are no easy-to-remember mnemonics or learning tricks for TORA, as the protocol is quite complex and requires a detailed understanding of the algorithm. However, to help with studying for exams, it is important to focus on understanding the three-phase process and the advantages and disadvantages of the protocol.

#### Applications of TORA

- TORA is used in ad-hoc networks, where nodes are mobile and the network topology is constantly changing.
- The protocol is also used in military and emergency communication networks, where a central authority may not be available to manage the network.