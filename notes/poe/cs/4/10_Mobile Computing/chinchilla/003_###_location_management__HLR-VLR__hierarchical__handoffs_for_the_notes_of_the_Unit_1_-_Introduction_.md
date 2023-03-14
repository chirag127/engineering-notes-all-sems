### Location Management: HLR-VLR, Hierarchical, Handoffs

Location management is an essential aspect of mobile computing, which enables the network to locate mobile devices and route incoming calls and messages to the appropriate destinations. In this section, we'll explore the concepts of HLR-VLR, hierarchical, and handoffs in location management.

#### HLR-VLR

HLR (Home Location Register) and VLR (Visitor Location Register) are two components of the GSM (Global System for Mobile Communications) network that work together to manage the location of mobile devices. HLR maintains a centralized database of all the subscribers' information, including their phone numbers, current location, and service plan details. VLR, on the other hand, manages the information of the mobile devices that are currently in its coverage area. 

Whenever a mobile device moves from one VLR's coverage area to another, the VLR sends a location update request to the HLR, which updates the subscriber's location information in its database. When a call or message is sent to the subscriber, the network consults the HLR to determine the subscriber's current location and route the call or message to the appropriate VLR.

#### Hierarchical Location Management

Hierarchical location management is a technique used to manage the location information of mobile devices in large cellular networks. In a hierarchical structure, the network is divided into several levels, with each level having a different degree of granularity. The top level represents the entire network, while the lower levels represent smaller regions within the network.

The hierarchical structure makes it easier to manage the location information of mobile devices, as it reduces the number of location updates that need to be performed. For example, when a mobile device moves from one region to another, only the VLR at the lower level needs to be updated, and the higher levels can remain unchanged.

#### Handoffs

Handoffs are the process of transferring an ongoing call or data session from one base station to another as the mobile device moves from one cell to another. Handoffs are essential to maintain the quality of service and ensure that the call or session is not dropped during the transition.

Handoffs can be classified into two types: hard handoff and soft handoff. In a hard handoff, the connection to the old base station is severed before establishing a connection with the new base station. In contrast, in a soft handoff, the connection to the new base station is established before severing the connection to the old base station, ensuring that there is no interruption in the call or data session.

### Overview of Wireless Telephony: Cellular Concept, GSM

Wireless telephony refers to the use of wireless technology to make and receive phone calls. The cellular concept is a fundamental concept in wireless telephony, which divides the service area into smaller cells, each served by a base station. The cells are arranged in a honeycomb pattern, with each cell covering a specific area.

GSM (Global System for Mobile Communications) is a cellular network standard used in many countries worldwide. GSM uses digital modulation to transmit voice and data and provides better call quality and data transfer rates than its analog predecessors. The GSM network uses a combination of TDMA (Time Division Multiple Access) and FDMA (Frequency Division Multiple Access) to maximize the use of available bandwidth.

In conclusion, location management, hierarchical structures, and handoffs are crucial concepts in mobile computing that enable seamless connectivity for mobile devices. Understanding the cellular concept and GSM network standard is essential to comprehend the workings of wireless telephony.