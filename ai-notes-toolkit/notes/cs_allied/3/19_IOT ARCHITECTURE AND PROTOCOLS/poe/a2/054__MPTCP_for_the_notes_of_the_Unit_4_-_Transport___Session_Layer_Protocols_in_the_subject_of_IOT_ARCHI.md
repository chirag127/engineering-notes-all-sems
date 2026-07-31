 Here is the formal content in Markdown format without any emojis or external links for the topic MPTCP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS:

### MPTCP

- MPTCP stands for Multipath TCP. It is an extension to the traditional TCP protocol.
- It enables a single TCP connection to use multiple paths to maximize resource usage and increase redundancy.
- This enables faster throughput, better bandwidth aggregation and higher tolerance for network interference.
- The data is split into multiple sub-flows across available paths and reassembled at the destination. This provides performance improvements and reliability.
- The MPTCP connection appears as a regular TCP connection to applications. The underlying paths may be wired, cellular or Wi-Fi networks.
- The IETF MPTCP working group standardized the MPTCP protocol in RFC 6824. There are open-source implementations in Linux and other OSs.
- MPTCP can benefit IOT use cases with heterogenous and multi-homed networks where multiple interfaces or paths are available and can be aggregated.
- However, MPTCP does introduce some complexity and processing/battery overhead and may not always be beneficial or compatible with firewalls/middleboxes.
- Hence, suitability of MPTCP needs to be evaluated for each specific use case. When available and compatible, it can improve performance and reliability.

Does this look okay? Let me know if you would like me to modify or expand the content in any way.