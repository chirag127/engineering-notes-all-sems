#### Medium Access Control and Local Area Networks

- Medium Access Control (MAC) is a sublayer of the data link layer that regulates the access of multiple devices to a shared medium, such as a wireless channel or a wired network.
- MAC protocols are designed to avoid or resolve collisions, which occur when two or more devices transmit data at the same time on the same medium.
- There are two main approaches to MAC in Local Area Networks (LANs): contention and token-passing.
  - Contention is a first-come, first-serve approach, where devices compete for the medium and back off if they detect a collision. An example of a contention-based MAC protocol is Carrier Sense Multiple Access with Collision Detection (CSMA/CD), which is used in Ethernet networks.
  - Token-passing is a cooperative approach, where devices take turns to access the medium by passing a token among themselves. An example of a token-passing MAC protocol is Token Ring, which is used in some LANs.
- MAC protocols can also be classified as centralized or distributed, depending on whether there is a central controller or not that coordinates the access to the medium.
  - Centralized MAC protocols rely on a master device or an access point that grants or denies the requests of other devices to access the medium. An example of a centralized MAC protocol is Polling, which is used in some wireless LANs.
  - Distributed MAC protocols rely on local decisions of each device based on the state of the medium or the messages from other devices. An example of a distributed MAC protocol is CSMA/CA, which is used in IEEE 802.11 wireless LANs.
- MAC protocols can also be adaptive or non-adaptive, depending on whether they adjust their parameters or behavior according to the network conditions or not.
  - Adaptive MAC protocols can change their transmission rate, power, channel, or backoff time based on the network load, interference, or quality of service requirements. An example of an adaptive MAC protocol is IEEE 802.11e, which is an amendment to IEEE 802.11 that defines MAC procedures to support LAN applications with quality of service requirements.
  - Non-adaptive MAC protocols use fixed parameters or behavior regardless of the network conditions. An example of a non-adaptive MAC protocol is IEEE 802.11b, which is a standard for wireless LANs that operates at a fixed rate of 11 Mbps.