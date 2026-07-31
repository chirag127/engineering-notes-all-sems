# Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated on-demand routing protocol that was proposed by Park and Corson in 1997 .
- TORA is designed for wireless mobile ad hoc networks that are highly dynamic and have frequent topology changes .
- TORA is based on the concept of link reversal, which is a technique to re-establish routes after link failures without global network information .
- TORA consists of three main phases: route creation, route maintenance, and route erasure  .
  - Route creation: When a source node wants to send data to a destination node, it broadcasts a query packet containing the destination ID. The query packet propagates through the network until it reaches the destination or a node that has a route to the destination. The nodes that receive the query packet assign themselves a height metric based on their distance from the destination. The height metric is used to create a directed acyclic graph (DAG) rooted at the destination. The nodes that have a lower height than their neighbors are downstream nodes, and the nodes that have a higher height than their neighbors are upstream nodes. The upstream nodes send update packets to their downstream nodes to inform them of their height and establish routes. The source node receives an update packet from one of its downstream nodes and selects it as the next hop to the destination.
  - Route maintenance: When a link failure occurs, the nodes that are affected by the link failure adjust their height metrics to reflect the new topology. The nodes that lose all their downstream neighbors increase their height to a value higher than their highest neighbor and broadcast a clear packet to invalidate the routes that use the failed link. The clear packet triggers a new route creation phase to re-establish the routes.
  - Route erasure: When a source node no longer needs a route to a destination node, it broadcasts a clear packet containing the destination ID. The clear packet propagates through the network and erases all the routes to the destination. The nodes that receive the clear packet reset their height metrics to null.
- TORA has some advantages and disadvantages as a routing protocol for ad hoc networks  .
  - Advantages:
    - TORA is highly adaptive and scalable to large and dense networks.
    - TORA minimizes the control overhead by using local information and avoiding global network updates.
    - TORA avoids routing loops by using the height metric and the DAG structure.
    - TORA supports multiple routes to the same destination, which increases the reliability and load balancing of the network.
  - Disadvantages:
    - TORA may create long and suboptimal routes due to the link reversal technique and the propagation delay of the control packets.
    - TORA may generate a large number of control packets in the presence of frequent link failures, which consumes bandwidth and energy.
    - TORA does not consider the quality of service (QoS) parameters such as delay, bandwidth, and reliability in the route selection process.
    - TORA does not provide security mechanisms to prevent malicious attacks on the routing protocol.