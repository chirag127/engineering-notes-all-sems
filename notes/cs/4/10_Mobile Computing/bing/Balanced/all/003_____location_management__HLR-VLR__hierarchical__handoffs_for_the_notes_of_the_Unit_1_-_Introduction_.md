# Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is a fundamental problem in personal communication services network (PCSN) that allows the network to locate and track the mobile users and deliver calls to them  .
- Location management consists of three main tasks: location update, location lookup, and paging  .
- Location update is the process of informing the network about the current location of the mobile user, which is recorded in the home location register (HLR) and the visitor location register (VLR) databases  .
- HLR is a centralized database that stores the permanent information of all the subscribers in the network, such as their phone numbers, service profiles, and current locations .
- VLR is a local database that stores the temporary information of the subscribers who are currently visiting a certain registration area (RA) in the network, such as their authentication data, temporary phone numbers, and location areas (LAs) .
- RA is a logical area that covers a group of base stations (cells) and is served by a VLR .
- LA is a logical area that covers a group of cells and is served by a mobile switching center (MSC) .
- Location lookup is the process of finding the current location of the mobile user when a call arrives for them, which involves querying the HLR and the VLR databases  .
- Paging is the process of sending a broadcast message to the mobile user in their current LA to alert them about the incoming call and establish a connection  .
- Handoff is the process of transferring the ongoing call from one cell to another as the mobile user moves across the network, which involves updating the routing information and allocating the radio resources  .
- Handoff can be classified into two types: hard handoff and soft handoff  .
- Hard handoff is the process of breaking the connection with the old cell before establishing a connection with the new cell, which results in a brief interruption of the call  .
- Soft handoff is the process of maintaining the connection with both the old and the new cells until the call is transferred to the new cell, which results in a seamless transition of the call  .
- Location management and handoff management are interrelated, as the location update and lookup affect the handoff performance and vice versa  .
- Location management and handoff management face several challenges and trade-offs, such as minimizing the signaling overhead, reducing the latency, balancing the load, preserving the quality of service, and ensuring the security and privacy of the users    .
- Location management and handoff management can be improved by using various techniques, such as hierarchical, distributed, or hybrid architectures, location caching, location prediction, mobility modeling, adaptive algorithms, and cooperative strategies    .