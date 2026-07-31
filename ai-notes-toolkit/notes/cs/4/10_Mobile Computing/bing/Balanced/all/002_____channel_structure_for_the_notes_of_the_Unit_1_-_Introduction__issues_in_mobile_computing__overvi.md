# Channel Structure

- Channel structure is the way of organizing the communication channels in a mobile network.
- A channel is a logical or physical path for transmitting data between a mobile device and a base station.
- Channel structure affects the performance, efficiency, and reliability of the mobile network.

## Physical and Logical Channels

- Physical channels are defined by the frequency and time slot used for transmission.
- Logical channels are defined by the type and purpose of the data carried by the physical channel.
- There are two types of logical channels: traffic channels and control channels.
- Traffic channels (TCHs) are used to carry voice or data between the mobile device and the base station.
- Control channels (CCHs) are used to carry signaling and management information between the mobile device and the base station.
- Control channels can be further classified into broadcast channels, common control channels, and dedicated control channels.

## Channel Structure in GSM

- GSM is a widely used standard for cellular communication that uses a combination of frequency division multiple access (FDMA) and time division multiple access (TDMA) to allocate channels.
- GSM divides the frequency spectrum into 124 carrier frequencies, each with a bandwidth of 200 kHz.
- Each carrier frequency is divided into eight time slots, each with a duration of 0.577 ms.
- Each time slot can carry one physical channel, which can be assigned to one logical channel.
- GSM uses different logical channels for different purposes, such as:

  - Broadcast Control Channel (BCCH): used to broadcast system information and cell parameters to all mobile devices in the cell.
  - Frequency Correction Channel (FCCH): used to synchronize the frequency of the mobile devices with the base station.
  - Synchronization Channel (SCH): used to synchronize the time slot of the mobile devices with the base station.
  - Paging Channel (PCH): used to alert the mobile devices of incoming calls or messages.
  - Random Access Channel (RACH): used by the mobile devices to request access to the network or to respond to paging messages.
  - Access Grant Channel (AGCH): used by the base station to assign a traffic channel or a dedicated control channel to a mobile device.
  - Standalone Dedicated Control Channel (SDCCH): used to exchange authentication, encryption, and location update information between the mobile device and the base station.
  - Slow Associated Control Channel (SACCH): used to carry measurement reports and power control commands between the mobile device and the base station.
  - Fast Associated Control Channel (FACCH): used to carry urgent signaling information, such as handover commands, by stealing a traffic channel time slot.
  - Cell Broadcast Channel (CBCH): used to broadcast short messages to all mobile devices in the cell.