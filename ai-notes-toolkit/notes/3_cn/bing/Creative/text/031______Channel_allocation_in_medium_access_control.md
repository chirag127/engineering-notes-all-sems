#### Channel allocation in medium access control

- Channel allocation is the process of assigning different frequency bands or time slots to different users or devices that want to communicate over a shared medium.
- Medium access control (MAC) is the protocol or mechanism that coordinates the access to the channel, while ensuring good throughput, fairness, low latency and low energy consumption.
- Channel allocation and medium access control are closely related, as the MAC protocol may depend on the channel allocation scheme, and vice versa.
- There are different types of channel allocation schemes, such as:
  - Fixed channel allocation: Each user or device is assigned a fixed channel or set of channels for the duration of the communication. This scheme is simple and avoids collisions, but may waste bandwidth if some channels are underutilized or some users have high demand.
  - Dynamic channel allocation: The channel or set of channels is assigned to each user or device on demand, based on some criteria such as traffic load, priority, channel availability, etc. This scheme is more flexible and efficient, but may incur higher overhead and complexity.
  - Hybrid channel allocation: A combination of fixed and dynamic channel allocation, where some channels are reserved for certain users or devices, and some channels are shared among others. This scheme can balance the trade-off between simplicity and flexibility, but may require coordination and synchronization among users or devices.
- There are different types of MAC protocols, such as:
  - Contention-based MAC: Each user or device competes for the channel access, using some random or deterministic algorithm to avoid or resolve collisions. Examples of contention-based MAC protocols are ALOHA, CSMA, CSMA/CD, CSMA/CA, etc.
  - Reservation-based MAC: Each user or device reserves the channel access in advance, using some signaling or negotiation mechanism. Examples of reservation-based MAC protocols are TDMA, FDMA, CDMA, OFDMA, etc.
  - Hybrid MAC: A combination of contention-based and reservation-based MAC, where some parts of the channel are accessed by contention, and some parts are accessed by reservation. Examples of hybrid MAC protocols are IEEE 802.11, IEEE 802.15.4, etc.