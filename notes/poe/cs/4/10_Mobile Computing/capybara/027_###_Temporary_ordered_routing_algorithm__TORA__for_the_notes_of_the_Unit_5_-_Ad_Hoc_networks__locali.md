### Temporary Ordered Routing Algorithm (TORA) for Ad Hoc Networks

Temporary Ordered Routing Algorithm (TORA) is a distributed routing protocol that was developed for ad hoc networks. It is a reactive protocol that is designed to provide a quick response to changes in network topology. TORA is a multi-hop protocol that uses a link-state routing algorithm to determine the shortest path between source and destination nodes.

#### How TORA Works

The main idea behind TORA is to create a directed acyclic graph (DAG) of the network topology. Each node in the network maintains a set of links to its neighbors, and it uses this information to construct a local view of the network. Each node then computes its distance to the destination node using a set of metrics that take into account the number of hops, the link quality, and the relative position of the nodes.

The TORA protocol works in three phases:

1. Route Creation: When a source node wants to send a packet to a destination node, it broadcasts a query packet to all its neighbors. The query packet contains information about the source node, the destination node, and a sequence number that is used to identify the query.

2. Route Maintenance: When a node receives a query packet, it uses the information in the packet to update its local view of the network. If the node is not the destination node, it forwards the query packet to its neighbors. If the node is the destination node, it sends a reply packet back to the source node.

3. Route Deletion: When a node detects that a link has failed or that a node has moved out of range, it broadcasts a delete packet to all its neighbors. The delete packet contains information about the failed link or node, and it is used to update the local views of the network.

#### Advantages of TORA

- TORA is a highly scalable protocol that can handle large ad hoc networks.
- TORA is a reactive protocol that responds quickly to changes in network topology.
- TORA is a multi-hop protocol that can handle long-range communication.
- TORA is a distributed protocol that does not require centralized control.

#### Disadvantages of TORA

- TORA requires a lot of communication overhead due to the frequent updates of the local views of the network.
- TORA can suffer from routing loops if there are errors in the sequence numbers or the link metrics.
- TORA can be vulnerable to attacks such as blackhole attacks, grayhole attacks, and wormhole attacks.

#### Mnemonics and Learning Tricks

Unfortunately, there are no easy mnemonics or learning tricks for TORA. However, it is important to understand the basic principles of the protocol and to practice implementing it in simulation environments such as NS-3 or OMNET++. By doing so, students can gain a deeper understanding of the protocol and its strengths and weaknesses. Additionally, students can learn from real-world examples of TORA being used in ad hoc networks, such as military networks, disaster response networks, and emergency communication networks.