 Here is the content in markdown format for the given topic:

### TCP over wireless for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

TCP over wireless networks faces several challenges due to the unreliable nature of the wireless medium:

- Higher bit error rates: The wireless medium is more prone to interference and noise, leading to higher bit error rates compared to wired networks. This can corrupt TCP segments, leading to reduced throughput.
- Variable latency: The wireless medium can exhibit variable latency due to factors like fading, interference, etc. This can affect TCP's timing estimates and congestion control.
- Limited bandwidth: The wireless medium typically has lower bandwidth than wired networks. This can impact TCP's congestion avoidance mechanisms.

To address these issues, the following TCP optimizations for wireless networks have been proposed:

- Selective acknowledgements (SACKs): SACKs can help recover from lost segments more efficiently in the face of higher bit error rates.
- Larger initial windows: Increasing the initial congestion window can help overcome the bandwidth limitations and achieve better utilization of the wireless link. However, this has to be done carefully to avoid congestion.
- Aggregation: Packet aggregation can help reduce protocol overhead and make better use of the limited bandwidth in wireless networks.
- Explicit congestion notification (ECN): ECN can help provide more timely congestion feedback to TCP and avoid unnecessary retransmissions in wireless networks with variable latency.

In addition, link layer techniques like forward error correction (FEC) and automatic repeat request (ARQ) can also help provide reliable delivery over the wireless link and complement the TCP optimizations.

Hope this helps! Let me know if you would like me to elaborate on any of the points or add additional details.