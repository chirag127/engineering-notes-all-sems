## Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR)

In this unit, we will cover various aspects of ad hoc networks, including localization, MAC issues, routing protocols, and global state routing (GSR). Ad hoc networks are wireless networks that are formed without any fixed infrastructure or centralized control, making them highly flexible and adaptable. Let's dive into the details:

### Ad Hoc Networks
- Ad hoc networks are wireless networks that are created on-the-fly, without any fixed infrastructure or centralized control.
- In ad hoc networks, nodes communicate with each other directly, forming a multi-hop network.
- Ad hoc networks are highly flexible and adaptable, making them suitable for use in situations where fixed infrastructure is not available or practical.
- Ad hoc networks can be used in a wide range of applications, including military and emergency response scenarios, sensor networks, and mobile computing.

### Localization
- Localization is the process of determining the physical location of nodes in an ad hoc network.
- Localization is important for many applications, including navigation, tracking, and monitoring.
- Various localization techniques can be used in ad hoc networks, including range-based and range-free techniques.
- Range-based techniques use measurements of signal strength or time of flight to estimate distances between nodes, while range-free techniques use other information, such as connectivity patterns, to estimate node locations.
- Localization accuracy can be affected by various factors, including signal propagation, interference, and node mobility.

### MAC Issues
- The medium access control (MAC) layer is responsible for coordinating access to the wireless medium in ad hoc networks.
- In ad hoc networks, the MAC layer faces various challenges, including hidden and exposed terminal problems, and the need to support multi-hop communication.
- Hidden terminal problems arise when a node cannot detect the presence of another node that is transmitting to a third node, leading to collisions.
- Exposed terminal problems arise when a node refrains from transmitting because it incorrectly detects the presence of another node that is not actually interfering with its transmission.
- Various MAC protocols have been developed to address these issues, including carrier sense multiple access (CSMA) and its variants, and contention-based protocols such as distributed coordination function (DCF) in IEEE 802.11.

### Routing Protocols
- Routing protocols are responsible for finding and maintaining routes between nodes in an ad hoc network.
- Routing protocols in ad hoc networks can be classified into two main categories: proactive and reactive.
- Proactive protocols maintain routes to all destinations in the network at all times, while reactive protocols only discover routes when needed.
- Proactive protocols are suitable for networks with low mobility and low traffic, while reactive protocols are more suitable for highly dynamic networks with high traffic.
- Examples of routing protocols include the proactive protocol optimized link state routing (OLSR) and the reactive protocol ad hoc on-demand distance vector (AODV).

### Global State Routing (GSR)
- Global state routing (GSR) is a routing protocol that is designed for large-scale ad hoc networks with high mobility and high traffic.
- GSR maintains a global view of the network state, allowing it to make optimal routing decisions.
- GSR uses a distributed algorithm to maintain a global view of the network state, with each node maintaining a partial view of the network and exchanging information with neighboring nodes.
- GSR has been shown to outperform other routing protocols in large-scale ad hoc networks with high mobility and high traffic. 

Mnemonics and Learning Tricks:

- To remember the types of routing protocols, think of "Proactive" as "Always prepared", while "Reactive" is "Just in time".
- For MAC issues, think of "hidden terminals" as "sneaky neighbors", while "exposed terminals" are "overly cautious".
- To remember the difference between range-based and range-free localization techniques, think of "range-based" as "measuring the distance", while "range-free" is "using other clues".