 Here is the content in Markdown format for the given topic:

## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- Wireless LANs eliminate the need for physical cables between devices, allowing increased mobility. However, this introduces a number of new challenges at the MAC layer:
- Hidden terminal problem: Wireless stations cannot detect when other stations are transmitting, potentially leading to collisions. Solutions include RTS/CTS handshake and detecting signals from other stations.
- Exposed terminal problem: A station may unnecessarily defer its transmission even though the receiver is out of range of the other transmitting station. Solutions include adjusting the contention window size based on frame losses.
- Near-far effect: Stations close to the access point can overwhelm transmissions from farther stations. Solutions include power control and directional antennas.
- IEEE 802.11 is the most popular wireless LAN standard. Key features include:
- Carrier sense multiple access with collision avoidance (CSMA/CA) at the MAC layer.
- Multiple data rates (1-54 Mbps) and transmission ranges.
- Two modes: infrastructure (all communications via access point) and ad hoc (devices communicate directly).
- Security: WEP, WPA, WPA2.
- Bluetooth is a short-range wireless technology primarily designed for peripherals and accessories ( headphones, keyboards). Key features include:
- Frequency hopping spread spectrum technology to avoid interference.
- Master-slave relationships between devices.
- Limited data rates (1-3 Mbps) but low power consumption.
- Security built on device pairing and encryption.

Mnemonics and learning tricks:
- Think H-T-P for Hidden terminal, Exposed terminal, and Near-far problems.
- Remember the order of solutions: RTS/CTS, adjusting contention window, power control, directional antennas.
- For IEEE 802.11, remember "CSMA/CA" and the two modes: infrastructure and ad hoc.