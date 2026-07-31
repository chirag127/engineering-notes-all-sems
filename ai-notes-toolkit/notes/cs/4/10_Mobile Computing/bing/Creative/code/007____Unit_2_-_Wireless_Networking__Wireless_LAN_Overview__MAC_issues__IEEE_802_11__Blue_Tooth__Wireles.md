# Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Bluetooth, Wireless

## Wireless Networking
- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless networking can provide mobility, flexibility, scalability, and cost-effectiveness for various applications and scenarios.
- Wireless networking can be classified into different types based on the coverage area, such as wireless personal area networks (WPANs), wireless local area networks (WLANs), wireless metropolitan area networks (WMANs), and wireless wide area networks (WWANs).

## Wireless LAN Overview
- A wireless LAN (WLAN) is a type of wireless networking that connects devices within a limited area, such as a home, office, campus, or hotspot.
- A WLAN typically uses radio waves or infrared signals to transmit and receive data over the air.
- A WLAN consists of wireless stations (such as laptops, smartphones, tablets, etc.) and wireless access points (APs) that provide wireless connectivity to a wired network or the Internet.
- A WLAN can operate in two modes: infrastructure mode and ad hoc mode. In infrastructure mode, the wireless stations communicate through the APs, which act as bridges between the wireless and wired networks. In ad hoc mode, the wireless stations communicate directly with each other without using any APs.

## MAC Issues
- The medium access control (MAC) layer is responsible for coordinating the access of multiple wireless stations to the shared wireless medium.
- The MAC layer faces several challenges and issues in wireless networking, such as:
  - Hidden terminal problem: when two wireless stations are within the range of an AP but not within the range of each other, they may not sense each other's transmissions and cause collisions.
  - Exposed terminal problem: when a wireless station is within the range of two APs but not within the range of the intended receiver, it may unnecessarily defer its transmission to avoid collisions with the other AP.
  - Fading and interference: the wireless signals may vary in strength and quality due to obstacles, reflections, multipath, noise, etc., which may affect the reliability and performance of the wireless communication.
  - Mobility and power management: the wireless stations may move across different APs or switch between different power states, which may require the MAC layer to handle the handoff and sleep/wake-up procedures.

## IEEE 802.11
- IEEE 802.11 is the most widely used standard for WLANs, developed by the IEEE 802.11 working group.
- IEEE 802.11 defines the MAC and physical (PHY) layer specifications for WLANs, as well as several amendments and extensions to enhance the functionality and performance of WLANs.
- IEEE 802.11 supports various frequency bands, modulation schemes, data rates, and channel widths, such as:
  - 2.4 GHz band: used by 802.11b, 802.11g, and 802.11n, with data rates up to 11 Mbps, 54 Mbps, and 600 Mbps, respectively, and channel widths of 20 MHz or 40 MHz.
  - 5 GHz band: used by 802.11a, 802.11n, 802.11ac, and 802.11ax, with data rates up to 54 Mbps, 600 Mbps, 6.9 Gbps, and 9.6 Gbps, respectively, and channel widths of 20 MHz, 40 MHz, 80 MHz, 160 MHz, or 320 MHz.
  - 6 GHz band: used by 802.11ax and 802.11be, with data rates up to 9.6 Gbps and 46 Gbps, respectively, and channel widths of 20 MHz, 40 MHz, 80 MHz, 160 MHz, or 320 MHz.
- IEEE 802.11 uses the Ethernet protocol and CSMA/CA (carrier sense multiple access with collision avoidance) as the basic MAC scheme, which requires the wireless stations to sense the medium before transmitting and to wait for an acknowledgment from the receiver after transmitting.
- IEEE 802.11 also supports various MAC enhancements and features, such as:
  - RTS/CTS (request to send/clear to send): a mechanism to solve the hidden terminal problem by exchanging control frames before data frames.
  - NAV (network allocation vector): a mechanism to inform the wireless stations about the duration of the ongoing transmissions and to reserve the medium for future transmissions.
  - DCF (distributed coordination function): a contention-based MAC scheme that uses CSMA/CA and binary