#### Multiple access protocols in medium access control

Medium Access Control (MAC) is an essential component of network protocol design. It is responsible for managing access to the shared communication medium in a network. Multiple Access Protocols (MAPs) are used in MAC to enable multiple nodes to access the medium simultaneously. Here are some common MAPs used in MAC:

1. Carrier Sense Multiple Access (CSMA): In this protocol, a node checks for the presence of signals on the medium before transmitting. If the medium is idle, the node transmits; otherwise, it waits until the medium is free. CSMA is further classified into three types: CSMA/CD (Collision Detection), CSMA/CA (Collision Avoidance), and 1-persistent CSMA.

2. Time Division Multiple Access (TDMA): In TDMA, the medium is divided into time slots, and each node is assigned a specific time slot for transmission. Only one node can transmit at a given time, and other nodes wait for their allocated time slot. TDMA is used in cellular networks.

3. Frequency Division Multiple Access (FDMA): In FDMA, the frequency band is divided into multiple channels, and each node is assigned a specific channel for transmission. The channels are separated by a guard band to minimize interference. FDMA is used in satellite communication systems.

4. Code Division Multiple Access (CDMA): In CDMA, each node is assigned a unique code that is used to encode the transmitted signal. All nodes transmit simultaneously, but only the receiver with the correct code can decode the signal. CDMA is used in wireless communication systems.

5. Slotted Aloha: In this protocol, each node transmits in a time slot, and the receiver acknowledges the successful reception. If the receiver does not receive the signal, the node retransmits in the next time slot. Slotted Aloha is used in satellite communication systems.

In conclusion, multiple access protocols are essential in medium access control to provide efficient and fair access to the shared communication medium. The choice of MAP depends on the application requirements and network characteristics. It is important to understand the advantages and disadvantages of each MAP to select the appropriate protocol for a given network design.