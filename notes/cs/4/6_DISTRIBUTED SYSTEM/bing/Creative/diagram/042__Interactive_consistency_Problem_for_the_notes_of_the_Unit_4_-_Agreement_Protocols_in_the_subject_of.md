The interactive consistency problem is a problem in which n nodes, where up to t may be byzantine, each with its own private value, run an algorithm that allows all non-faulty nodes to infer the values of each other node.  This problem is relevant to critical applications that rely on the combination of the opinions of multiple peers to provide a service. 

The following diagram illustrates the basic architecture of a system with n nodes and t byzantine nodes, where each node sends its value to all other nodes and receives values from them. The non-faulty nodes then use a consensus algorithm to agree on a vector of values that represents the initial values of all nodes. The byzantine nodes may send different values to different nodes or no value at all.

```
+-----+     +-----+     +-----+     +-----+     +-----+
|  V1 |     |  V2 |     |  V3 |     |  V4 |     |  V5 |
+-----+     +-----+     +-----+     +-----+     +-----+
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   V           V           V           V           V
+-----+     +-----+     +-----+     +-----+     +-----+
|  V1 |     |  V2 |     |  V3 |     |  V4 |     |  V5 |
+-----+     +-----+     +-----+     +-----+     +-----+
|  V2 |     |  V1 |     |  V1 |     |  V1 |     |  V1 |
+-----+     +-----+     +-----+     +-----+     +-----+
|  V3 |     |  V3 |     |  V2 |     |  V2 |     |  V2 |
+-----+     +-----+     +-----+     +-----+     +-----+
|  V4 |     |  V4 |     |  V4 |     |  V3 |     |  V3 |
+-----+     +-----+     +-----+     +-----+     +-----+
|  V5 |     |  V5 |     |  V5 |     |  V5 |     |  V4 |
+-----+     +-----+     +-----+     +-----+     +-----+
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   |           |           |           |           |
   V           V           V           V           V
+-----+     +-----+     +-----+     +-----+     +-----+
| (V1 |     | (V1 |     | (V1 |     | (V1 |     | (V1 |
|  V2 |     |  V2 |     |  V2 |     |  V2 |     |  V2 |
|  V3 |     |  V3 |     |  V3 |     |  V3 |     |  V3 |
|  V4 |     |  V4 |     |  V4 |     |  V4 |     |  V4 |
|  V5)|     |  V5)|     |  V5)|     |  V5)|     |  V5)|
+-----+     +-----+     +-----+     +-----+     +-----+
```

In this diagram, the nodes are numbered from 1 to 5, and the values are represented by V1 to V5. The byzantine nodes are node 3 and node 5, and they send different values to different nodes. For example, node 3 sends V1 to node 1, V2 to node 2, V3 to itself, V4 to node 4, and V5 to node