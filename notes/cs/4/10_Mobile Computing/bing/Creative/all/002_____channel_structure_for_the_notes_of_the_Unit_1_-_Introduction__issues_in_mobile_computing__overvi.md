# Channel Structure for Mobile Computing

- Mobile computing is the use of wireless devices and networks to access, process, and transmit data and services.
- Wireless telephony is the technology of providing voice and data communication over wireless channels, such as cellular networks, satellite networks, and radio networks.
- Cellular concept is the idea of dividing a large geographic area into smaller cells, each with its own base station and frequency allocation, to increase the capacity and coverage of wireless networks.
- GSM (Global System for Mobile Communications) is a standard for digital cellular networks that uses time division multiple access (TDMA) to divide each frequency channel into eight time slots, each carrying a burst of data or voice.
- Channel structure is the way of organizing the physical and logical channels in a wireless network to carry different types of information and signals.

## Physical Channels

- Physical channels are the basic units of transmission in a wireless network, defined by the frequency and the time slot used by a transmitter and a receiver.
- In GSM, each frequency channel has a bandwidth of 200 kHz and is divided into eight time slots, each lasting 0.577 ms. Each time slot can carry one burst of data or voice, which is 156.25 bits long.
- A physical channel can be either full-rate or half-rate, depending on the number of time slots used by a user. A full-rate channel uses one time slot per frame (4.615 ms), while a half-rate channel uses one time slot every two frames (9.23 ms).
- A physical channel can also be either uplink or downlink, depending on the direction of transmission. An uplink channel is used by a mobile station to transmit to a base station, while a downlink channel is used by a base station to transmit to a mobile station.

## Logical Channels

- Logical channels are the types of information and signals carried by the physical channels, such as traffic, control, and broadcast.
- In GSM, there are three types of logical channels: traffic channels (TCHs), control channels (CCHs), and the cell broadcast channel (CBCH) .
- Traffic channels are used to carry user data and voice between a mobile station and a base station. They can be either full-rate or half-rate, depending on the data rate and the codec used.
- Control channels are used to carry signaling and management information between a mobile station and a base station, such as synchronization, authentication, paging, location update, handover, and power control. They can be either common or dedicated, depending on the scope and the purpose of the information.
- The cell broadcast channel is used to transmit short messages to all mobile stations in a cell, such as emergency alerts, weather reports, or advertisements. It is a downlink-only channel that uses one time slot per frame.

## Channel Allocation

- Channel allocation is the process of assigning physical and logical channels to users and base stations in a wireless network, to optimize the performance and the quality of service.
- Channel allocation strategies can be classified into fixed, dynamic, hybrid, and borrowing, depending on the criteria and the flexibility of the allocation .
- Fixed channel allocation assigns a fixed number of channels to each cell, regardless of the traffic demand. It is simple and efficient, but it may cause channel wastage or congestion in some cells.
- Dynamic channel allocation assigns channels to cells on demand, based on the traffic load and the interference level. It is adaptive and flexible, but it may cause channel fragmentation or overhead in some cases.
- Hybrid channel allocation combines fixed and dynamic allocation, by reserving some channels for each cell and sharing the rest among neighboring cells. It is a compromise between simplicity and adaptability, but it may require complex coordination and signaling.
- Borrowing channel allocation allows a cell to borrow channels from neighboring cells when its own channels are not enough. It is a form of dynamic allocation, but it may cause interference or conflict with the original owners of the channels.