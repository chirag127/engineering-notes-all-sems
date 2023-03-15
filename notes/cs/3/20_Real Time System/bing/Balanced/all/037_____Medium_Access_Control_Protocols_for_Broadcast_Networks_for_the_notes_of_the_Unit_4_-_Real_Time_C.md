# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast network.
- Broadcast networks are networks where a single transmission can reach all the nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks need to deal with the challenges of interference, collisions, hidden terminals, and fairness.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to decide which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but suffer from low efficiency and high collision probability.
- Deterministic contention protocols use a predefined order or priority to decide which node will transmit next, such as TDMA or token passing. These protocols are efficient and fair, but require synchronization and coordination among nodes, and are not adaptive to traffic changes or node failures.
- Reservation-based protocols use a combination of contention and reservation to allocate slots for transmission, such as ABROAD or PRMA. These protocols can provide performance guarantees and adaptivity, but require more overhead and complexity than pure contention protocols.