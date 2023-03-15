### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks are networks where a single transmission from one node can be received by all other nodes within the transmission range.
- Broadcast networks can be used for applications such as emergency alert systems, vehicular networks, sensor networks, etc.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic scheduling, or hybrid approaches.
- Probabilistic contention protocols use random or probabilistic methods to determine which node will transmit next, such as Aloha, CSMA, or slotted Aloha.
- Probabilistic contention protocols are simple, decentralized, and adaptive, but they suffer from collisions, low channel utilization, and unbounded access delay.
- Deterministic scheduling protocols use a predefined or dynamically allocated transmission schedule to assign slots to nodes, such as TDMA, CDMA, or FDMA.
- Deterministic scheduling protocols are collision-free, efficient, and provide bounded access delay, but they require synchronization, overhead, and are less adaptive to changes in traffic or topology.
- Hybrid protocols combine the advantages of both probabilistic and deterministic approaches, such as ABROAD, which uses a collision-avoidance handshake within each slot of a synchronous schedule, allowing nodes to reclaim or reuse idle slots while maintaining performance guarantees.
- Hybrid protocols aim to achieve high reliability, efficiency, and adaptability, but they may have higher complexity and trade-offs between different performance metrics.