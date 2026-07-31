### Location Management: HLR-VLR, Hierarchical, Handoffs

- Location management is the process of tracking and updating the location of mobile devices in wireless cellular networks.
- Location management consists of three main tasks: location update, location lookup, and paging.
- Location update is the process of informing the network about the current location of a mobile device, usually initiated by the device itself.
- Location lookup is the process of finding the current location of a mobile device, usually initiated by the network or another device.
- Paging is the process of sending a message to a mobile device to notify it of an incoming call or data.
- Location management involves two types of databases: Home Location Register (HLR) and Visitor Location Register (VLR).
- HLR is a centralized database that stores the subscription information and some location information of all mobile devices in the network.
- VLR is a local database that stores the information of the mobile devices that are currently visiting a specific service area.
- HLR and VLR communicate with each other to update and query the location information of mobile devices.
- HLR-VLR scheme is a hierarchical location management scheme that divides the service coverage area into registration areas (RAs), each with a VLR.
- Each RA covers a group of base stations (cells) that provide wireless communication to the mobile devices.
- When a mobile device moves from one RA to another, it performs a location update to the new VLR, which then contacts the HLR to update the location information.
- When a call or data is destined to a mobile device, the network performs a location lookup by querying the HLR, which then returns the address of the VLR that serves the current RA of the device.
- The network then sends a paging message to the VLR, which broadcasts it to all the cells in the RA, until the device responds.
- Handoff is the process of transferring an ongoing call or data session from one base station to another, without interrupting the communication.
- Handoff is necessary when a mobile device moves out of the coverage area of one base station and into the coverage area of another.
- Handoff can be classified into two types: hard handoff and soft handoff.
- Hard handoff is the process of breaking the connection with the old base station before establishing a connection with the new base station.
- Soft handoff is the process of maintaining the connection with both the old and the new base stations until the connection with the old base station is dropped.
- Handoff can also be classified into two types: horizontal handoff and vertical handoff.
- Horizontal handoff is the process of transferring a call or data session from one base station to another within the same network or technology.
- Vertical handoff is the process of transferring a call or data session from one network or technology to another, such as from cellular to Wi-Fi.
- Handoff involves three main phases: initiation, decision, and execution.
- Initiation is the phase where the mobile device or the network detects the need for a handoff, based on some criteria such as signal strength, quality, or load.
- Decision is the phase where the network or the mobile device selects the best candidate base station for the handoff, based on some criteria such as availability, capacity, or cost.
- Execution is the phase where the network or the mobile device performs the necessary signaling and resource allocation to complete the handoff.
- Handoff performance can be measured by some metrics such as handoff delay, handoff failure rate, handoff dropping rate, or handoff overhead.
- Handoff delay is the time required to complete a handoff.
- Handoff failure rate is the probability that a handoff attempt fails.
- Handoff dropping rate is the probability that a call or data session is dropped due to a handoff failure.
- Handoff overhead is the amount of resources consumed by the handoff process.

: Location Management in Wireless Cellular Networks
: Location, Handoff Management and HLR-VLR Location and Handoff Management
: Visitor Location Register - an overview | ScienceDirect Topics
: Lecture 1: Mobility Management in Mobile Wireless