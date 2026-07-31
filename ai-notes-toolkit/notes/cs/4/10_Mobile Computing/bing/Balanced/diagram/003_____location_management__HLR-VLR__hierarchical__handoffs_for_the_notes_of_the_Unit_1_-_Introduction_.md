### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile users in a wireless cellular network.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of notifying the network about the current location of a mobile user, usually initiated by the mobile user when it moves across a predefined boundary (such as a cell or a registration area).
- Location lookup is the process of finding the current location of a mobile user, usually initiated by the network when it needs to deliver a call or a message to the mobile user.
- Paging is the process of broadcasting a message to a set of cells where the mobile user is expected to be, usually initiated by the network after performing a location lookup, to alert the mobile user about an incoming call or message.
- Location management involves two types of databases: Home Location Register (HLR) and Visitor Location Register (VLR).
- HLR is a centralized database that stores the permanent information of all mobile users in the network, such as their phone numbers, service profiles, and current location areas.
- VLR is a local database that stores the temporary information of mobile users who are currently visiting a specific service area, such as their phone numbers, service profiles, and current cells.
- HLR and VLR communicate with each other to update and query the location information of mobile users.
- HLR-VLR scheme is a hierarchical location management scheme that divides the service coverage area into registration areas (RAs), each with a VLR. Each RA covers a group of base stations (cells).
- In HLR-VLR scheme, a mobile user performs a location update when it moves from one RA to another, and informs both the HLR and the VLR about its new location.
- In HLR-VLR scheme, a location lookup is performed by querying the HLR to find the current RA of the mobile user, and then querying the VLR of that RA to find the current cell of the mobile user.
- In HLR-VLR scheme, a paging is performed by broadcasting a message to the current cell of the mobile user, as obtained from the location lookup.
- Handoff is the process of transferring an ongoing call or data session from one base station to another, without interrupting the communication, when a mobile user moves across the cell boundaries.
- Handoff can be classified into two types: hard handoff and soft handoff.
- Hard handoff is the process of breaking the connection with the old base station before establishing a connection with the new base station. Hard handoff causes a brief interruption in the communication.
- Soft handoff is the process of establishing a connection with the new base station before breaking the connection with the old base station. Soft handoff allows a smooth transition in the communication.