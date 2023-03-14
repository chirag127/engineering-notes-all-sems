### Channel structure for the notes of the Unit 1 - Introduction, issues in mobile computing, overview of wireless telephony: cellular concept, GSM: in the subject of Mobile Computing

- GSM (Global System for Mobile Communications) is a second-generation digital cellular radio access technology that uses Time Division Multiple Access (TDMA) and Frequency Division Duplex (FDD) to provide voice and data services.
- GSM divides the available frequency band into channels of 200 kHz width, and each channel is further divided into eight time slots of 0.577 ms duration  . Each time slot can carry one burst of data or voice, and each user is assigned a specific time slot on a specific channel.
- The channel structure of GSM can be classified into two types: physical channels and logical channels.
- Physical channels are the combination of a frequency and a time slot, and they are used to carry the information between the mobile station and the base station. There are two types of physical channels: traffic channels (TCH) and control channels (CCH).
- Traffic channels are used to carry user data, such as voice or SMS. There are different types of traffic channels, depending on the data rate and the coding scheme. For example, a full rate TCH can carry 22.8 kbps of data, while a half rate TCH can carry 11.4 kbps of data.
- Control channels are used to carry signaling and control information, such as synchronization, authentication, paging, and handover. There are different types of control channels, depending on their function and direction. For example, a broadcast control channel (BCCH) is used to broadcast system information to all mobile stations, while a random access channel (RACH) is used by mobile stations to request access to the network.
- Logical channels are the abstraction of the information carried by the physical channels, and they are defined by the type and the format of the information. There are two types of logical channels: traffic channels and control channels.
- Traffic channels are used to carry user data, such as voice or SMS. There are different types of traffic channels, depending on the type of service and the quality of service. For example, a speech traffic channel (TCH/FS) is used to carry voice with full rate coding, while a data traffic channel (TCH/F9.6) is used to carry data with 9.6 kbps rate.
- Control channels are used to carry signaling and control information, such as synchronization, authentication, paging, and handover. There are different types of control channels, depending on their function and direction. For example, a frequency correction channel (FCCH) is used to provide frequency reference to mobile stations, while a common control channel (CCCH) is used to carry paging and access grant messages.

- A possible mnemonic to remember the types of control channels is: **F**or **S**yncing **F**requency, **S**end **F**CCH and **S**CH; **B**roadcast **B**CCH and **C**CCH; **R**equest **R**ACH and **A**nswer **A**GCH; **P**age **P**CH and **S**end **S**DCCH.

- A possible ascii diagram to illustrate the channel structure of GSM is:

```
|<----------------- 200 kHz ----------------->|
|<---- 0.577 ms ---->|<---- 0.577 ms ---->|...
|                    |                    |
|     Time slot 0    |     Time slot 1    |...
|                    |                    |
|                    |                    |
|<----------------- Physical channel ----------------->|
|                    |                    |
|                    |                    |
|     TCH or CCH    |     TCH or CCH    |...
|                    |                    |
|                    |                    |
|<----------------- Logical channel ------------------>|
```