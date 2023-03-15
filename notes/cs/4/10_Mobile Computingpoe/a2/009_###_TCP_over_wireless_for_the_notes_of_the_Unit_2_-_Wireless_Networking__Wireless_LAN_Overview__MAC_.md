 Here is the content in markdown format for the given topic:

### TCP over wireless for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

TCP over wireless networks face several challenges compared to TCP over wired networks:

- Higher error rates: Wireless channels are more prone to errors due to interference, fading, etc. This can lead to more frequent packet loss and corruption which can impact TCP performance.
- Variability in bandwidth: Wireless channels can experience variability in bandwidth due to mobility, interference, etc. This can impact TCP's congestion control mechanisms.
- Packet reordering: Packets can get reordered more frequently in wireless networks, which can trigger unnecessary retransmissions and congestion control in TCP.
- Handoffs: When a mobile device moves from one base station to another, it experiences a handoff. This can lead to temporary packet loss and delays, impacting TCP.

To handle these challenges and improve TCP performance over wireless, the following techniques are used:

- Error recovery techniques like selective acknowledgements (SACKs) and forward error correction (FEC) codes to recover from packet loss and corruption.
- Rate adaptation techniques to adapt to variability in bandwidth.
- Reorder buffering and duplication avoidance to handle packet reordering.
- Handoff buffering and seamless ROHC to handle the delays and packet loss during handoffs.

By employing these techniques, TCP performance over wireless networks can be significantly improved. However, TCP over wireless is still an active area of research to make it more robust to the unique challenges of the wireless medium.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.