### Temporary Ordered Routing Algorithm (TORA)

Temporary Ordered Routing Algorithm (TORA) is a distributed routing protocol that is used in Mobile Ad-hoc Networks (MANETs). It is a proactive protocol, which means that it constantly maintains the routing information even if there is no data to transmit. In this way, it is always ready to route data when necessary.

TORA is based on a concept of a directed acyclic graph (DAG) that is constructed dynamically. The nodes in the network maintain local information about the network topology, which is used to construct the DAG. The DAG is used to determine the shortest path between any two nodes in the network.

#### TORA Algorithm

The TORA algorithm can be divided into three main phases:

1. **Topology Setup**

In the first phase, each node in the network broadcasts a HELLO message to its neighbors, which contains information about the node's ID and its distance to its neighbors. Based on this information, each node constructs a local view of the network topology.

2. **Route Computation**

In the second phase, each node computes the shortest path to all other nodes in the network using the DAG. The DAG is constructed by using a set of rules that ensure that it is acyclic and that there are no loops.

3. **Route Maintenance**

In the third phase, each node monitors the network for changes in the topology. If there is a change, such as a node failure or a new node joining the network, the affected nodes will update their routing tables accordingly.

#### Advantages of TORA

- TORA is a proactive protocol, which means that it is always ready to route data.
- It is based on a directed acyclic graph, which ensures that there are no loops in the network.
- It is scalable and can handle large networks.
- It is efficient in terms of bandwidth and processing power.

#### Disadvantages of TORA

- TORA requires a lot of bandwidth for the HELLO messages that are broadcasted in the topology setup phase.
- It is not suitable for networks with a high degree of mobility, as it requires frequent updates to the DAG.

#### Mnemonic

One possible mnemonic for remembering the TORA algorithm is:

- Topology Setup
- Route Computation
- Route Maintenance

This can be remembered using the acronym TRM.

#### Example

Consider a simple network with three nodes A, B, and C. The network topology is shown in the figure below:

```
   A
  / \
 B---C
```

In the topology setup phase, each node broadcasts a HELLO message to its neighbors. Based on this information, each node constructs a local view of the network topology. The resulting topology is shown in the figure below:

```
   A
  / \
 B---C
```

In the route computation phase, each node computes the shortest path to all other nodes in the network using the DAG. The resulting DAG is shown in the figure below:

```
   A
  / \
 B---C
```

In the route maintenance phase, each node monitors the network for changes in the topology. If there is a change, such as a node failure or a new node joining the network, the affected nodes will update their routing tables accordingly.

#### Applications

TORA can be used in a variety of applications, including military networks, emergency response networks, and sensor networks. It is particularly useful in situations where the network topology is constantly changing, such as in disaster scenarios.