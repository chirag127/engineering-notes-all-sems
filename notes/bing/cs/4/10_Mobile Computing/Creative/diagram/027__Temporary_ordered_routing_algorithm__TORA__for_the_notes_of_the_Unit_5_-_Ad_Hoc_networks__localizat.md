The Temporally Ordered Routing Algorithm (TORA) is a source-initiated on-demand routing protocol for wireless ad hoc networks. It is based on the link reversal algorithm and works in three main phases: route creation, route maintenance and route erasure. TORA attempts to build a separate directed acyclic graph (DAG) by each node to every destination, using a height metric that reflects the temporal order of link changes.

The following diagram illustrates the basic architecture of TORA:

```
    A
   / \
  B   C
 / \ / \
D   E   F
 \ / \ /
  G   H
   \ /
    I
```

Each node has a height value that consists of four components: a reference level, a delta value, an ID and a logical clock. The reference level is used to indicate the existence of a DAG. The delta value is used to break ties among nodes with the same reference level. The ID is the unique identifier of the node. The logical clock is incremented whenever a link change occurs.

The height values are used to determine the direction of the data packets. A node will forward a packet to a neighbor with a lower height value, thus creating a downward path to the destination. If a node has no lower neighbor, it is a local maximum and will initiate a route creation phase.

The route creation phase involves sending query (QRY) and update (UPD) packets to establish a DAG. A node that has no route to the destination will broadcast a QRY packet to its neighbors, requesting a route. A node that receives a QRY packet will either reply with an UPD packet if it has a route, or forward the QRY packet if it does not. An UPD packet contains the height value of the sender and is used to update the height value of the receiver. A node that receives an UPD packet will set its height value to one higher than the sender and forward the UPD packet to its other neighbors. This way, a DAG is formed from the source to the destination.

The route maintenance phase involves detecting and repairing link failures. A node that detects a link failure will increment its logical clock and set its reference level to the maximum of its neighbors' reference levels plus one. This creates a new DAG with the node as the local maximum. The node will then broadcast a clear (CLR) packet to its neighbors, informing them of the link failure and the new height value. A node that receives a CLR packet will update its height value and forward the CLR packet to its other neighbors. If a node has no lower neighbor after receiving a CLR packet, it will initiate a route creation phase.

The route erasure phase involves deleting invalid routes. A node that wants to erase a route will broadcast a flush (FLS) packet to its neighbors, indicating the destination and the last known height value for that destination. A node that receives a FLS packet will compare the destination and the height value with its own. If they match, the node will invalidate its route and forward the FLS packet to its other neighbors. If they do not match, the node will discard the FLS packet. This way, all the nodes that have an invalid route to the destination will erase it.