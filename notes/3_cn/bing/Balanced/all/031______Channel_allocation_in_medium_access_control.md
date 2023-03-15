#### Channel allocation in medium access control

- Channel allocation is the process of assigning channels (frequency bands, time slots, code sequences, etc.) to different users or nodes in a communication network.
- Medium access control (MAC) is the protocol or mechanism that coordinates the access to a shared channel by multiple users or nodes, while ensuring good performance, fairness, low latency and low energy consumption.
- Channel allocation and medium access control are closely related, as the MAC protocol may depend on the channel allocation scheme, and vice versa.
- There are three main types of channel allocation schemes: fixed, dynamic and hybrid.

  - Fixed channel allocation (FCA) assigns a fixed number of channels to each user or node, regardless of the traffic demand or channel conditions. FCA is simple and efficient, but may suffer from underutilization or congestion of channels.
  - Dynamic channel allocation (DCA) assigns channels to users or nodes on demand, based on the traffic load, channel quality, priority, etc. DCA is flexible and adaptive, but may incur higher overhead and complexity.
  - Hybrid channel allocation (HCA) combines the advantages of FCA and DCA, by dividing the channels into two groups: one for fixed allocation and one for dynamic allocation. HCA can balance the trade-off between efficiency and flexibility, but may require more coordination and synchronization.

- There are two main types of MAC protocols: contention-based and contention-free.

  - Contention-based MAC protocols allow users or nodes to compete for the channel access, using random or deterministic methods. Contention-based MAC protocols are simple and decentralized, but may suffer from collisions, delays and unfairness.
  - Contention-free MAC protocols allocate the channel access to users or nodes in a predetermined or negotiated manner, using polling, reservation, token passing, etc. Contention-free MAC protocols are collision-free and predictable, but may incur higher overhead and complexity.

- A mnemonic to remember the types of channel allocation schemes and MAC protocols is:

  - FCA: Fixed Channel Allocation
  - DCA: Dynamic Channel Allocation
  - HCA: Hybrid Channel Allocation
  - CBM: Contention-Based MAC
  - CFM: Contention-Free MAC

- A learning trick to understand the difference between channel allocation and medium access control is:

  - Channel allocation is like assigning seats to passengers in a plane, while medium access control is like managing the boarding process.