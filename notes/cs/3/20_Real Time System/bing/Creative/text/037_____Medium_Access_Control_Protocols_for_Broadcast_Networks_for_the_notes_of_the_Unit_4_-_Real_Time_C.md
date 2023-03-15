### Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks are networks where a single transmission from one node can be received by all other nodes within the transmission range.
- Broadcast networks can be used for applications such as emergency alert systems, vehicular networks, sensor networks, etc.
- MAC protocols for broadcast networks can be classified according to the access strategy employed, such as probabilistic contention, deterministic scheduling, or hybrid approaches.
- Probabilistic contention protocols use randomization to resolve collisions among competing nodes. Examples are Aloha, CSMA, and IEEE 802.11.
- Deterministic scheduling protocols use a predefined or dynamically allocated transmission schedule to avoid collisions. Examples are TDMA, CDMA, and OFDMA.
- Hybrid protocols combine both contention and scheduling to achieve a trade-off between performance and adaptability. Examples are ABROAD, DRAND, and B-MAC.
- MAC protocols for broadcast networks need to address several challenges, such as hidden terminal problem, exposed terminal problem, fairness, scalability, reliability, and energy efficiency.
- Hidden terminal problem occurs when two nodes that are out of range of each other transmit to a common receiver, causing a collision at the receiver.
- Exposed terminal problem occurs when a node is prevented from transmitting to another node because of a neighboring transmission, even though the transmission would not cause a collision at the intended receiver.
- Fairness refers to the equal or proportional allocation of channel resources among competing nodes, which may have different traffic demands, transmission ranges, and channel conditions.
- Scalability refers to the ability of the MAC protocol to accommodate a large number of nodes without degrading the performance or increasing the overhead.
- Reliability refers to the ability of the MAC protocol to deliver packets successfully to the intended receivers, which may require mechanisms such as acknowledgments, retransmissions, or error correction.
- Energy efficiency refers to the ability of the MAC protocol to minimize the energy consumption of the nodes, which may require mechanisms such as duty cycling, power control, or sleep scheduling.