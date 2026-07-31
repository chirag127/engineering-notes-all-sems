# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless network or a broadcast channel.
- Broadcast networks are networks where a single transmission can be received by all nodes in the network, such as radio or satellite networks.
- MAC protocols for broadcast networks need to deal with the challenges of interference, collisions, hidden terminals, and exposed terminals, which can affect the reliability and efficiency of data transmission.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic contention, or reservation-based protocols.
- Probabilistic contention protocols use randomization to determine which node will transmit next, such as Aloha or CSMA. These protocols are simple and adaptive, but can suffer from high collision rates and unbounded access delays.
- Deterministic contention protocols use a predefined order or priority to determine which node will transmit next, such as TDMA or token passing. These protocols can provide bounded access delays and guaranteed throughput, but can be inefficient and inflexible under dynamic traffic and network conditions.
- Reservation-based protocols use a combination of contention and reservation phases to allocate slots for data transmission, such as PRMA or ABROAD. These protocols can achieve high channel utilization and reliability, but can incur overhead and complexity in the reservation process.