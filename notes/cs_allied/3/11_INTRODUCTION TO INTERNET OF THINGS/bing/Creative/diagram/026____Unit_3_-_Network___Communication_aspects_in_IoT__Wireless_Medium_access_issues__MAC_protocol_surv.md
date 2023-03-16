## Unit 3 - Network & Communication aspects in IoT: Wireless Medium access issues, MAC protocol survey, Survey routing protocols, Sensor deployment & Node discovery, Data aggregation & dissemination

- Wireless Medium access issues
  - Wireless medium access control (MAC) protocols are responsible for coordinating the access of multiple nodes to a shared wireless channel.
  - Wireless MAC protocols face several challenges, such as:
    - Hidden terminal problem: when two nodes that are out of range of each other transmit to a common receiver, causing collisions.
    - Exposed terminal problem: when a node is prevented from transmitting to its intended receiver because of a nearby transmission by another node to a different receiver.
    - Fading and interference: when the wireless signal quality varies due to environmental factors or co-channel interference from other sources.
    - Energy efficiency: when the nodes need to conserve battery power by minimizing idle listening, overhearing, and control overhead.
  - Wireless MAC protocols can be classified into two main categories: contention-based and contention-free.
    - Contention-based protocols: nodes compete for the channel access using random access techniques, such as carrier sense multiple access (CSMA), CSMA with collision avoidance (CSMA/CA), and CSMA with collision detection (CSMA/CD).
    - Contention-free protocols: nodes access the channel in a predetermined or negotiated manner, such as time division multiple access (TDMA), frequency division multiple access (FDMA), and code division multiple access (CDMA).
  - Wireless MAC protocols can also be designed for specific scenarios, such as:
    - Multihop networks: when the nodes are not within the direct transmission range of each other and need to rely on intermediate nodes to relay the packets, such as ad hoc networks and wireless sensor networks.
    - Multichannel networks: when the nodes can use multiple frequency channels to increase the network capacity and reduce the interference, such as cognitive radio networks and orthogonal frequency division multiplexing (OFDM) networks.
    - Multimedia networks: when the nodes need to support different types of traffic with different quality of service (QoS) requirements, such as voice, video, and data.

- MAC protocol survey
  - A MAC protocol survey is a systematic review of the existing wireless MAC protocols, their features, advantages, disadvantages, and performance metrics.
  - A MAC protocol survey can help to identify the gaps and challenges in the current state of the art, and to provide directions for future research and development.
  - A MAC protocol survey can cover different aspects of wireless MAC protocols, such as:
    - Classification: how the protocols are categorized based on their characteristics and objectives, such as contention-based, contention-free, multihop, multichannel, multimedia, etc.
    - Design principles: what are the main design goals and trade-offs of the protocols, such as throughput, delay, fairness, reliability, scalability, adaptability, etc.
    - Operation mechanisms: how the protocols work and coordinate the channel access among the nodes, such as carrier sensing, backoff, reservation, scheduling, handshaking, etc.
    - Performance evaluation: how the protocols are tested and compared in terms of their effectiveness and efficiency, such as analytical models, simulation tools, experimental platforms, etc.
    - Application scenarios: what are the typical use cases and environments where the protocols are applied or suitable, such as indoor, outdoor, urban, rural, etc.

- Survey routing protocols
  - Routing protocols are responsible for finding and maintaining the paths for data delivery among the nodes in a network.
  - Routing protocols face several challenges, such as:
    - Dynamic topology: when the network topology changes frequently due to node mobility, failure, or addition.
    - Limited resources: when the nodes have constraints on their battery power, memory, processing, and bandwidth.
    - Scalability: when the network size grows large and the routing overhead increases accordingly.
    - Heterogeneity: when the nodes have different capabilities and requirements, such as energy, QoS, security, etc.
  - Routing protocols can be classified into two main categories: proactive and reactive.
    - Proactive protocols: nodes maintain the routing information for all the destinations in the network, such as distance vector routing, link state routing, and hierarchical routing.
    - Reactive protocols: nodes discover the routing information on demand when there is a need to send data, such as ad hoc on-demand distance vector (AODV), dynamic source routing (DSR), and temporally ordered routing algorithm (TORA).
  - Routing protocols can also be designed for specific scenarios, such as:
    - Multihop networks: when the nodes need to forward the packets through multiple hops to reach the destination, such as ad hoc networks and wireless sensor networks.
    - Multicast networks: when the nodes need to