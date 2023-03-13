## Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- Wireless networking is the communication of data between devices without using wires or cables.
- Wireless LAN (WLAN) is a type of wireless network that connects devices within a local area, such as a home, office, or campus.
- WLANs use radio waves or infrared signals to transmit and receive data.
- WLANs have several advantages over wired LANs, such as mobility, scalability, ease of installation, and lower cost.
- WLANs also have some challenges, such as security, interference, limited range, and power consumption.

### MAC issues

- MAC (Medium Access Control) is the sublayer of the data link layer that controls how devices access the shared wireless medium.
- MAC issues are the problems that arise due to the characteristics of the wireless medium, such as noise, fading, multipath, and hidden and exposed terminals.
- Noise is the unwanted signal that interferes with the desired signal.
- Fading is the variation of signal strength due to the distance, obstacles, or movement of the transmitter or receiver.
- Multipath is the phenomenon of receiving multiple copies of the same signal with different delays, phases, and amplitudes, which can cause distortion or cancellation of the signal.
- Hidden terminal is the situation where two devices that are in the range of a common receiver, but not in the range of each other, may transmit simultaneously and cause a collision at the receiver.
- Exposed terminal is the situation where a device that is in the range of two receivers, but not in the range of the transmitter of one of them, may refrain from transmitting to avoid a collision, even though there is no collision at the intended receiver.

### IEEE 802.11

- IEEE 802.11 is the standard that defines the physical and MAC layers of WLANs.
- IEEE 802.11 specifies several physical layer technologies, such as frequency hopping spread spectrum (FHSS), direct sequence spread spectrum (DSSS), orthogonal frequency division multiplexing (OFDM), and multiple-input multiple-output (MIMO).
- IEEE 802.11 also specifies several MAC protocols, such as distributed coordination function (DCF), point coordination function (PCF), and hybrid coordination function (HCF).
- DCF is the basic MAC protocol that uses carrier sense multiple access with collision avoidance (CSMA/CA) to avoid collisions.
- CSMA/CA is a technique that requires a device to sense the medium before transmitting, and to wait for a random backoff time if the medium is busy.
- CSMA/CA also uses an optional handshake mechanism called request to send/clear to send (RTS/CTS) to solve the hidden terminal problem.
- PCF is an optional MAC protocol that uses a centralized controller called point coordinator (PC) to coordinate the access to the medium.
- PCF uses a polling mechanism to grant transmission opportunities to devices in a round-robin fashion.
- PCF also uses a contention-free period (CFP) to allow the PC to transmit without contention, followed by a contention period (CP) to allow the devices to transmit using DCF.
- HCF is an enhanced MAC protocol that combines the features of DCF and PCF, and introduces a new entity called hybrid coordinator (HC).
- HCF uses a contention-based channel access (EDCA) to allow devices to transmit using DCF with different priority levels, and a controlled channel access (HCCA) to allow the HC to transmit using PCF with guaranteed service quality.

### Blue Tooth

- Blue Tooth is a wireless technology that enables short-range communication between devices, such as phones, headsets, keyboards, mice, printers, and speakers.
- Blue Tooth uses a frequency band of 2.4 GHz, and can support data rates up to 3 Mbps.
- Blue Tooth uses a technique called adaptive frequency hopping (AFH) to avoid interference from other devices or sources in the same band.
- AFH is a technique that changes the frequency of transmission randomly and adaptively, based on the quality of the channels.
- Blue Tooth also uses a technique called spread spectrum to increase the robustness of the transmission.
- Spread spectrum is a technique that spreads the signal over a wider bandwidth than the original signal, using a code that is known to both the transmitter and the receiver.
- Blue Tooth devices form a network called a piconet, which consists of one master device and up to seven active slave devices.
- The master device controls the frequency hopping and the synchronization of the piconet.
- The slave devices follow the master's frequency hopping and transmit only when addressed by the master.
- Multiple piconets can form a larger network called a scatternet, which consists of