# Medium Access Control Protocols for Broadcast Networks

- Medium access control (MAC) protocols coordinate access to a shared communications channel, such as a wireless broadcast network.
- Broadcast networks allow multiple nodes to transmit data to all other nodes in the network, which can be useful for real-time communication applications such as video conferencing, sensor networks, or vehicular networks.
- However, broadcast networks also face the challenge of avoiding or resolving collisions, which occur when two or more nodes transmit data at the same time, resulting in interference and data loss.
- MAC protocols can be classified according to the access strategy employed, such as probabilistic contention, deterministic scheduling, or hybrid protocols.
- Probabilistic contention protocols utilize direct, asynchronous competition between neighboring nodes to determine which node will transmit next. Examples include Aloha, CSMA, and IEEE 802.11.
- Deterministic scheduling protocols assign fixed or dynamic time slots to each node, ensuring collision-free transmission. Examples include TDMA, FDMA, and CDMA.
- Hybrid protocols combine elements of both contention and scheduling protocols, aiming to achieve high throughput, low delay, and adaptability. Examples include ABROAD, PRMA, and MACAW.
- The design and performance of MAC protocols depend on various factors, such as the network topology, the traffic pattern, the channel characteristics, the node capabilities, and the quality of service requirements.