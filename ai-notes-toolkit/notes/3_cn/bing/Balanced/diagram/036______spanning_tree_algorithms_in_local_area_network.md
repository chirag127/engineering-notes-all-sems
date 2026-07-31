A spanning tree algorithm is a network protocol that builds a loop-free logical topology for any bridged Ethernet local area network. It prevents bridge loops and the broadcast radiation that results from them by disabling redundant links and selecting one preferred link between switches in the LAN. The preferred link is used for all Ethernet frames unless it fails, in which case a backup link is enabled. The algorithm also designates one layer-2 switch as the root bridge, which is the reference point for all other switches in the network .

A possible ASCII diagram for a spanning tree algorithm in a local area network with four switches (A, B, C, D) and six links (1, 2, 3, 4, 5, 6) is shown below. The diagram assumes that switch A is the root bridge and link 1 is the preferred link between A and B. The links that are disabled by the algorithm are marked with X.

#### Spanning Tree Algorithm in Local Area Network

```
    +---+  1  +---+  2  +---+
    | A |-----| B |-----| C |
    +---+     +---+     +---+
     | 3       | 4       | 5
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         |         |
     |         X         |
     |       +---+       |
     | 6     | D |       |
     +-------+---+-------+
```