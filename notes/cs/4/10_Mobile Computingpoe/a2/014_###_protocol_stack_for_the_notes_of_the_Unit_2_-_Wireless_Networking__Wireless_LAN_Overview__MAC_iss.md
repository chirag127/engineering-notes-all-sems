 Here is the content in markdown format:

### Protocol stack for Wireless Networking

- Physical layer: Converts data into radio signals and vice versa. Examples: IEEE 802.11a/b/g PHY standards using different frequency bands.
- MAC layer: Handles access to shared wireless medium. Examples: IEEE 802.11 MAC using CSMA/CA. Handles acknowledgments, retries, etc.
- Link layer: Provides reliable data transmission over wireless links. Example: PPP handles point-to-point connections.
- Network layer: Same as in wired networks. Example: IP handles routing of data between wireless nodes.
- Transport layer: Same as in wired networks. Examples: TCP and UDP handle end-to-end connectivity and data delivery.
- Application layer: Same as in wired networks. Examples: HTTP, FTP, SMTP, etc.

Mnemonics: Please All, Come Eat Pizza (Physical, MAC, Link, Network, Transport, Application layers)

**Wireless LAN Overview: MAC issues**
- Hidden terminal problem: When node A sends to B and C wants to send to B but can't sense A's transmission. Solution: Use RTS/CTS.
- Exposed terminal problem: When A sends to B and C wants to send to D but defers because it senses A's transmission meant for B. Inefficient.
- MAC layer acknowledgements and retries handle lost/corrupted data.
- MAC protocols are designed for dynamically changing wireless medium properties.

**IEEE 802.11**
- Most popular WLAN standard.
- Defines 2.4/5 GHz bands with different PHY/MAC options (a/b/g/n/ac).
- Uses CSMA/CA: Listen before talk. Random backoff delays on collision.
- Supports different data rates and ranges. Higher frequencies have higher bandwidth but lower range.
- Security extensions: WEP, WPA, WPA2 (AES encryption).

**Bluetooth**
- Short-range (meters) wireless technology.
- Used for peripherals, headsets.
- Ad hoc network topology with master/slave relationships.
- Frequency hopping spread spectrum for interference avoidance.
- Supports voice and data with limited throughput (~1-3 Mbps).

**Wireless range/bandwidth tradeoff**
- Higher frequencies allow higher bandwidths but have lower range.
- Lower frequencies have higher range but lower bandwidth.
- Select technology based on application requirements.