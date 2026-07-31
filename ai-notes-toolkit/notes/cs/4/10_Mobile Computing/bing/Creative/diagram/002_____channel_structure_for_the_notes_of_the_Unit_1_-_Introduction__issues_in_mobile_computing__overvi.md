Hello, I am Sydney, your AI assistant. I can help you with your study material for Mobile Computing. Here is the content for the topic of channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM:

### Channel Structure

- A channel is a medium or a path that carries information from one point to another in a communication system.
- In mobile computing, channels are used to transmit and receive data between mobile devices and base stations or between base stations and network controllers.
- Channels can be classified into two types: physical channels and logical channels.

#### Physical Channels

- Physical channels are the basic units of transmission in a mobile network. They are defined by the frequency, time slot, and code used to modulate the signal.
- Physical channels can be further divided into two types: frequency division multiple access (FDMA) channels and time division multiple access (TDMA) channels.
- FDMA channels are the frequency bands allocated to each user or cell in a network. They are separated by guard bands to avoid interference.
- TDMA channels are the time slots assigned to each user or cell in a network. They are separated by guard gaps to avoid interference.
- A combination of FDMA and TDMA channels is called a hybrid channel.

#### Logical Channels

- Logical channels are the information streams carried by the physical channels. They are defined by the type, format, and purpose of the data transmitted or received.
- Logical channels can be further divided into two types: traffic channels and control channels.
- Traffic channels are the logical channels that carry user data, such as voice, video, or text messages.
- Control channels are the logical channels that carry signaling and management data, such as call setup, handover, authentication, or synchronization.
- In GSM, there are three types of control channels: broadcast control channels (BCCHs), common control channels (CCCHs), and dedicated control channels (DCCHs).
- BCCHs are the control channels that broadcast information about the network and the cell, such as the frequency, the cell identity, or the network parameters.
- CCCHs are the control channels that handle the access and paging of the mobile devices, such as the random access channel (RACH), the paging channel (PCH), or the access grant channel (AGCH).
- DCCHs are the control channels that handle the communication between the mobile device and the base station, such as the stand-alone dedicated control channel (SDCCH), the slow associated control channel (SACCH), or the fast associated control channel (FACCH).

#### Channel Structure in GSM

- GSM is a cellular network that uses a combination of FDMA and TDMA channels to provide voice and data services to mobile users.
- GSM uses a 25 MHz frequency band in the 900 MHz range, which is divided into 124 FDMA channels, each with a bandwidth of 200 kHz.
- Each FDMA channel is further divided into eight TDMA channels, each with a duration of 0.577 ms. A group of eight TDMA channels is called a frame, which has a duration of 4.615 ms.
- A physical channel in GSM is defined by a pair of frequency and time slot, such as (f1, t1) or (f2, t2).
- A logical channel in GSM is defined by the information carried by the physical channel, such as TCH, BCCH, RACH, or SDCCH.
- The channel structure in GSM is shown in the following diagram:

![Channel structure in GSM](https://www.tutorialspoint.com/wireless_communication/images/gsm_channel_structure.jpg)

- Source: