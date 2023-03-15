
#### Learning Bridge Algorithms in Local Area Network

* Learning bridge algorithms are used in local area networks to switch data frames between different LAN segments.
* These algorithms enable communication between different LAN segments by learning MAC addresses and creating a forwarding table.
* The most commonly used learning bridge algorithms are the Spanning Tree Protocol (STP) and the Rapid Spanning Tree Protocol (RSTP).
* Spanning Tree Protocol (STP) is a Layer 2 protocol used to create a loop-free topology in a LAN. It works by creating a tree-like structure with a root bridge, designated bridges and blocked ports.
* It uses the concept of port states (blocking, listening, learning and forwarding).
* Rapid Spanning Tree Protocol (RSTP) is an evolution of STP. RSTP works faster than STP and has fewer port states (discarding, learning and forwarding).
* RSTP also has the concept of edge ports, which are ports that are directly connected to end devices and do not need to participate in the spanning tree process.
* Both STP and RSTP use the BPDU (Bridge Protocol Data Unit) to exchange information between bridges.
* A good mnemonic for remembering the port states of STP is "B-L-L-F" for Blocking, Listening, Learning, and Forwarding.