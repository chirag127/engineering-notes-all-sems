Hello, I am Sydney, your AI assistant. I can help you with your query. Here is a summary of the topic you requested:

### Temporary ordered routing algorithm (TORA) for ad hoc networks

- TORA is a source-initiated, on-demand routing protocol for wireless mobile ad hoc networks  .
- TORA is based on the link reversal algorithm, which dynamically creates a directed acyclic graph (DAG) rooted at the destination node .
- TORA consists of three main phases: route creation, route maintenance, and route erasure .
- In route creation, the source node broadcasts a query packet containing the destination ID and a height variable. The height variable is used to assign a logical level to each node in the DAG. The nodes that receive the query packet update their height and propagate the query until it reaches the destination or a node that has a route to the destination .
- In route maintenance, the nodes monitor the status of their outgoing links and update their height accordingly. If a link failure occurs, the nodes that lose their last downstream link perform a local link reversal by increasing their height and broadcasting an update packet. This process may propagate to other nodes until a new DAG is formed or the route becomes invalid .
- In route erasure, the nodes that detect a network partition or a route failure broadcast a clear packet to erase all the invalid routes in the network. The clear packet contains the destination ID and the height of the sender. The nodes that receive the clear packet compare their height with the sender's height and erase their routes if they are lower or equal .
- TORA is an efficient, highly adaptive, and scalable routing protocol that can handle frequent topology changes and network partitions  .
- TORA can also support quality of service (QoS) components such as delay, bandwidth, and jitter by using a QoS routing extension (QoSR) that modifies the height variable to reflect the QoS metrics.