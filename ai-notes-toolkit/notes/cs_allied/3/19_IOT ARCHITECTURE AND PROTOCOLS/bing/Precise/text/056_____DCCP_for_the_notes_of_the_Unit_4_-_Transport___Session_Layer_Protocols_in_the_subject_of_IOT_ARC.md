### DCCP

- Datagram Congestion Control Protocol (DCCP) is a transport layer protocol that provides a way to send unreliable datagrams with congestion control.
- DCCP is designed for applications that require fast delivery of data but can tolerate some loss of data, such as multimedia streaming or online gaming.
- DCCP uses a combination of techniques from User Datagram Protocol (UDP) and Transmission Control Protocol (TCP) to provide congestion control while maintaining the benefits of datagram delivery.
- DCCP includes features such as:
  - Congestion control mechanisms to avoid network congestion and ensure fair sharing of network resources.
  - Capability negotiation to allow endpoints to negotiate and select the most appropriate congestion control mechanism for their needs.
  - Acknowledgments and retransmissions to provide reliability for control information and improve congestion control performance.
  - Explicit Congestion Notification (ECN) support to allow routers to signal congestion to endpoints and improve congestion control performance.
- DCCP is defined in RFC 4340 and has been extended by several other RFCs to add new features and improve performance.