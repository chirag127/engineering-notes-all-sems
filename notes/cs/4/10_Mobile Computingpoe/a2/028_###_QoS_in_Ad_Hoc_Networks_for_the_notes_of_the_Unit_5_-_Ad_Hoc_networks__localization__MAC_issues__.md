 Here is the content in markdown format for the topic ### QoS in Ad Hoc Networks for the notes of the Unit 5 - Ad Hoc networks, localization, MAC issues, Routing protocols, global state routing (GSR), in the subject of Mobile Computing:

### QoS in Ad Hoc Networks

**QoS Issues:**
- Bandwidth constraints: Limited channel bandwidth in wireless ad hoc networks.
- Interference: Wireless transmission can interfere with other transmissions resulting in increased packet loss and latency.
- Hidden terminal problem: When a node is not in range of a transmitter but is in range of the receiver, it may transmit simultaneously resulting in packet collision at receiver.
- Limited battery power: Most ad hoc devices operate on batteries having limited energy. Hence, routing protocols must be energy efficient.

**QoS routing protocols:**
-AODV-QoS: Extension of AODV to find paths that meet QoS constraints such as bandwidth and delay.
-OARP: Finds highest throughput paths satisfying multiple QoS constraints.
-ZRP: Uses both proactive and reactive approaches for efficiently maintaining QoS routes.

**Resource reservation:**
-Receiver-initiated reservation: Receiver sends resource reservation message along path to reserve resources. Less overhead but may result in under-utilization of resources.
-Sender-initiated reservation: Sender sends resource reservation message to reserve resources along path before sending data. More overhead but resources are reserved only when needed.

**QoS MAC protocols:**
-IEEE 802.11e: Enhanced version of IEEE 802.11 to support QoS. Provides mechanisms for differentiated channel access based on QoS requirements.
-MMAC: A reservation-based TDMA MAC protocol designed for high-speed ad hoc networks satisfying QoS requirements. Slots are reserved based on QoS needs.

**Advantages:**
- Support real-time and multimedia applications having stringent QoS requirements.
- Provide differentiated services based on application needs.

**Disadvantages:**
- Additional overhead of maintaining QoS routes and resource reservations.
- Complexity of implementing QoS in ad hoc networks.