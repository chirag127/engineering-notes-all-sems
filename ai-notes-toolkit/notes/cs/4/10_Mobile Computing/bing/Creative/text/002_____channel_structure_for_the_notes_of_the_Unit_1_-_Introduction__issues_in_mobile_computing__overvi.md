### Channel Structure

- Channel structure is the way of organizing the communication channels in a mobile network.
- A channel is a logical or physical path for transmitting data between a mobile device and a base station.
- Channel structure affects the performance, efficiency, and reliability of the mobile network.

#### Physical Channels and Logical Channels

- Physical channels are the radio frequency (RF) carriers that are divided into time slots. Each time slot can carry one or more bits of data.
- Logical channels are the information streams that are carried within the physical channels. Logical channels can be classified into traffic channels and control channels.
- Traffic channels (TCHs) are used to carry voice or data between the mobile device and the base station.
- Control channels (CCHs) are used to carry signaling and management information between the mobile device and the base station. Control channels can be further divided into broadcast channels, common control channels, and dedicated control channels.

#### Broadcast Channels

- Broadcast channels are used to transmit information from the base station to all mobile devices in the cell. Broadcast channels include:
  - Frequency correction channel (FCCH): used to synchronize the frequency of the mobile device with the base station.
  - Synchronization channel (SCH): used to synchronize the time slot and frame number of the mobile device with the base station.
  - Broadcast control channel (BCCH): used to broadcast information about the cell identity, frequency allocation, and network parameters.
  - Cell broadcast channel (CBCH): used to broadcast short messages to all mobile devices in the cell.

#### Common Control Channels

- Common control channels are used to establish and maintain the connection between the mobile device and the base station. Common control channels include:
  - Random access channel (RACH): used by the mobile device to request access to the network.
  - Paging channel (PCH): used by the base station to page the mobile device for an incoming call or data.
  - Access grant channel (AGCH): used by the base station to assign a traffic channel or a dedicated control channel to the mobile device.
  - Stand-alone dedicated control channel (SDCCH): used to exchange authentication, encryption, and location update information between the mobile device and the base station.

#### Dedicated Control Channels

- Dedicated control channels are used to carry signaling and management information between the mobile device and the base station during an active call or data session. Dedicated control channels include:
  - Slow associated control channel (SACCH): used to exchange power control, timing advance, and quality measurement information between the mobile device and the base station.
  - Fast associated control channel (FACCH): used to exchange handover, call setup, and call release information between the mobile device and the base station.
  - Enhanced full rate (EFR) SACCH: used to exchange enhanced power control, timing advance, and quality measurement information between the mobile device and the base station.