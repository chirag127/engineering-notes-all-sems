# Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

## Wireless Networking
- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless networking can provide mobility, convenience, scalability, and cost-effectiveness for users and network administrators.
- Wireless networking can also pose challenges such as security, interference, reliability, and compatibility.

## Wireless LAN Overview
- A wireless LAN (WLAN) is a local area network (LAN) that uses wireless media to connect devices.
- A WLAN typically consists of one or more access points (APs) that provide wireless coverage to a certain area, and one or more wireless stations (STAs) that communicate with the APs.
- A WLAN can operate in two modes: infrastructure mode and ad hoc mode.
  - In infrastructure mode, the STAs associate with an AP and use it as a relay to communicate with other STAs or the wired network.
  - In ad hoc mode, the STAs form a peer-to-peer network without an AP and communicate directly with each other.

## MAC Issues
- The medium access control (MAC) layer is responsible for coordinating the access of multiple STAs to the shared wireless medium.
- The MAC layer faces several issues in wireless networking, such as:
  - Hidden terminal problem: when two STAs are within the range of an AP but not within the range of each other, they may not sense each other's transmissions and cause collisions at the AP.
  - Exposed terminal problem: when a STA is within the range of two APs but not within the range of the intended receiver, it may unnecessarily defer its transmission to avoid interfering with another transmission that does not affect the receiver.
  - Fading and multipath: when the wireless signal is attenuated or distorted by obstacles, reflections, or interference, resulting in reduced signal quality and increased bit error rate.
  - Mobility: when the STAs move within or across the coverage areas of different APs, requiring handoff and reassociation procedures to maintain connectivity.

## IEEE 802.11
- IEEE 802.11 is a family of standards that define the MAC and physical layer (PHY) specifications for WLANs.
- IEEE 802.11 defines several PHY technologies that operate in different frequency bands and offer different data rates, such as:
  - 802.11a: 5 GHz band, up to 54 Mbps
  - 802.11b: 2.4 GHz band, up to 11 Mbps
  - 802.11g: 2.4 GHz band, up to 54 Mbps
  - 802.11n: 2.4 GHz and/or 5 GHz band, up to 600 Mbps
  - 802.11ac: 5 GHz band, up to 6.9 Gbps
  - 802.11ax: 2.4 GHz and/or 5 GHz band, up to 9.6 Gbps
- IEEE 802.11 also defines several MAC features and enhancements, such as:
  - Distributed coordination function (DCF): a basic MAC scheme that uses carrier sense multiple access with collision avoidance (CSMA/CA) and binary exponential backoff to access the medium.
  - Point coordination function (PCF): an optional MAC scheme that uses a centralized controller (point coordinator) to poll the STAs and grant them access to the medium.
  - Quality of service (QoS): a set of MAC mechanisms that provide differentiated services for different traffic classes, such as voice, video, and data.
  - Security: a set of MAC protocols that provide authentication, encryption, and integrity protection for wireless communications, such as wired equivalent privacy (WEP), Wi-Fi protected access (WPA), and WPA2.

## Bluetooth
- Bluetooth is a wireless technology that enables short-range communication between devices, such as phones, headsets, keyboards, mice, printers, etc.
- Bluetooth uses a frequency-hopping spread spectrum (FHSS) technique to hop among 79 channels in the 2.4 GHz band, each with a bandwidth of 1 MHz.
- Bluetooth devices form a piconet, which is a network of up to eight devices, one of which acts as a master and the others as slaves.
- Multiple piconets can be interconnected to form a scatternet, which is a network of multiple masters and slaves.

## Wireless
- Wireless is a broad term that encompasses any communication that does not use wires or cables, such as radio, infrared, microwave, satellite, cellular, etc.