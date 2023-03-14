#### Channel allocation in medium access control

- Channel allocation is the process of assigning a portion of the available bandwidth or frequency spectrum to different users or devices in a communication network.
- Channel allocation can be classified into three types: fixed, dynamic, and hybrid.
- Fixed channel allocation (FCA) assigns a fixed number of channels to each user or device, regardless of their traffic demand or activity. FCA is simple, fair, and efficient, but it may result in underutilization or wastage of channels when some users or devices are idle, and congestion or blocking when some users or devices have high traffic demand or activity.
- Dynamic channel allocation (DCA) assigns channels to users or devices on demand, based on their traffic demand or activity. DCA is flexible, adaptive, and responsive, but it may result in complexity, overhead, and delay in channel assignment and release. DCA can be further divided into two categories: centralized and distributed.
- Centralized DCA relies on a central controller or base station to monitor the traffic demand or activity of all users or devices, and to assign and release channels accordingly. Centralized DCA is easy to implement and manage, but it may result in a single point of failure, scalability issues, and interference from the central controller or base station.
- Distributed DCA relies on the users or devices to communicate with each other and to negotiate and agree on channel assignment and release. Distributed DCA is robust, scalable, and resilient, but it may result in coordination problems, collisions, and hidden terminal or exposed terminal issues.
- Hybrid channel allocation (HCA) combines the advantages of FCA and DCA, and tries to overcome their disadvantages. HCA assigns a fixed number of channels to each user or device, and allows them to dynamically borrow or lend channels from or to other users or devices, based on their traffic demand or activity. HCA is a compromise between simplicity and flexibility, efficiency and adaptability, and fairness and responsiveness.

- Some examples of channel allocation schemes are:

  - Frequency division multiple access (FDMA): divides the available bandwidth into equal-sized frequency bands, and assigns each band to a different user or device. FDMA is a type of FCA.
  - Time division multiple access (TDMA): divides the available bandwidth into equal-sized time slots, and assigns each slot to a different user or device. TDMA is a type of FCA.
  - Code division multiple access (CDMA): assigns a unique code to each user or device, and allows them to use the same bandwidth simultaneously. CDMA is a type of DCA.
  - Carrier sense multiple access (CSMA): allows users or devices to sense the channel before transmitting, and to defer or back off if the channel is busy. CSMA is a type of DCA.
  - Carrier sense multiple access with collision avoidance (CSMA/CA): allows users or devices to sense the channel before transmitting, and to send a request to send (RTS) and wait for a clear to send (CTS) before transmitting. CSMA/CA is a type of DCA.
  - Carrier sense multiple access with collision detection (CSMA/CD): allows users or devices to sense the channel before transmitting, and to abort or retransmit if a collision is detected. CSMA/CD is a type of DCA.
  - Token passing: passes a token or a permission to transmit among users or devices in a predefined order or sequence. Token passing is a type of DCA.
  - Reservation: allows users or devices to reserve a channel in advance for a certain duration or number of packets. Reservation is a type of DCA.
  - Polling: allows a central controller or base station to poll or query each user or device in turn, and to grant them a channel if they have data to transmit. Polling is a type of DCA.
  - Demand assigned multiple access (DAMA): allows users or devices to request a channel from a central controller or base station when they have data to transmit, and to release the channel when they are done. DAMA is a type of DCA.
  - Dynamic channel selection (DCS): allows users or devices to select a channel from a pool of available channels, based on the channel quality or interference level. DCS is a type of DCA.
  - Dynamic frequency selection (DFS): allows users or devices to switch to a different frequency band, based on the channel quality or interference level. DFS is a type of DCA.
  - Borrowed-channel multiple access (BCMA): allows users or devices to borrow a channel from another user or device, if their own channel is busy or unavailable. BCMA is a type of HCA.
  - Channelized multiple access (CMA): allows users or