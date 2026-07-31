## Unit 4 - Medium Access Control and Local Area Networks

- Medium access control (MAC) is the sublayer of the data link layer that controls the hardware responsible for interaction with the transmission medium.
- MAC protocols enforce a methodology to allow multiple devices access to a shared media network.
- MAC protocols can be classified into two categories: contention-based and contention-free.
- Contention-based protocols allow devices to compete for the channel access, such as ALOHA, CSMA, CSMA/CD, and CSMA/CA.
- Contention-free protocols allocate the channel access to devices in a deterministic or centralized manner, such as TDMA, FDMA, CDMA, and polling.
- Local area networks (LANs) are networks that connect devices within a limited geographical area, such as a building or a campus.
- LANs can be wired or wireless, depending on the transmission medium used.
- Wired LANs use cables, such as coaxial, twisted pair, or optical fiber, to connect devices. Examples of wired LAN standards are Ethernet, Token Ring, and FDDI.
- Wireless LANs use radio waves, infrared, or microwave to connect devices. Examples of wireless LAN standards are IEEE 802.11, Bluetooth, and WiMAX.
- Wireless LANs have some challenges that wired LANs do not, such as interference, multipath fading, hidden terminal problem, and exposed terminal problem.
- IEEE 802.11 is the most widely used wireless LAN standard, which defines the MAC and physical layer (PHY) specifications for wireless connectivity   .
- IEEE 802.11 MAC sublayer has two modes of operation: distributed coordination function (DCF) and point coordination function (PCF).
- DCF is based on CSMA/CA protocol, which uses a random backoff mechanism and an optional acknowledgment scheme to avoid and recover from collisions.
- PCF is based on a polling mechanism, which uses a point coordinator (usually the access point) to grant the channel access to devices in a round-robin fashion.
- IEEE 802.11 PHY sublayer has several variants, such as 802.11a, 802.11b, 802.11g, 802.11n, 802.11ac, and 802.11ax, which differ in the modulation, coding, bandwidth, and data rate used.