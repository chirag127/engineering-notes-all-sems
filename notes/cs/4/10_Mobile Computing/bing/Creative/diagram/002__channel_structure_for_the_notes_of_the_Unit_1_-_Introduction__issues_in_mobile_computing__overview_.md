The channel structure in GSM is based on the division of the frequency band into 124 channels, each with a bandwidth of 200 kHz, and the division of each channel into eight time slots. Each time slot is called a physical channel and can carry different types of logical channels, which are used for different purposes, such as traffic, control, or broadcast.

The logical channels in GSM can be classified into two main types: traffic channels (TCHs) and control channels (CCHs). Traffic channels carry digitally encoded user voice or user data and have identical formats on both forward and reverse links. Control channels carry signaling and synchronization commands between the base station and mobile station.

The control channels can be further divided into three subtypes: broadcast channels (BCHs), common control channels (CCCHs), and dedicated control channels (DCCHs). Broadcast channels are used to transmit system information and cell parameters to all mobile stations in the cell. Common control channels are used to establish and maintain communication between a mobile station and the network. Dedicated control channels are used to exchange signaling information during a call.

The following diagram illustrates the basic architecture of a GSM channel structure, using ASCII characters to represent the different types of channels. The diagram shows a 51-frame multiframe structure, which is used for most of the control channels. Each frame consists of eight time slots, and each time slot can carry one physical channel. The diagram also shows the mapping of the logical channels to the physical channels, using the following abbreviations:

- FCCH: Frequency Correction Channel
- SCH: Synchronization Channel
- BCCH: Broadcast Control Channel
- RACH: Random Access Channel
- AGCH: Access Grant Channel
- PCH: Paging Channel
- SDCCH: Standalone Dedicated Control Channel
- SACCH: Slow Associated Control Channel
- FACCH: Fast Associated Control Channel

```
+-----------------------------------------------------------------+
| Frame 0 | Frame 1 | Frame 2 | Frame 3 | ... | Frame 49 | Frame 50|
+-----------------------------------------------------------------+
| FCCH    | SDCCH   | SDCCH   | SDCCH   | ... | SDCCH    | SDCCH   |
| SCH     | SACCH   | SDCCH   | SDCCH   | ... | SDCCH    | SACCH   |
| BCCH    | SDCCH   | SDCCH   | SDCCH   | ... | SDCCH    | SDCCH   |
| BCCH    | SACCH   | SDCCH   | SDCCH   | ... | SDCCH    | SACCH   |
| BCCH    | SDCCH   | SDCCH   | SDCCH   | ... | SDCCH    | SDCCH   |
| BCCH    | SACCH   | SDCCH   | SDCCH   | ... | SDCCH    | SACCH   |
| BCCH    | SDCCH   | SDCCH   | SDCCH   | ... | SDCCH    | SDCCH   |
| BCCH    | RACH    | AGCH    | PCH     | ... | AGCH     | PCH     |
+-----------------------------------------------------------------+
```