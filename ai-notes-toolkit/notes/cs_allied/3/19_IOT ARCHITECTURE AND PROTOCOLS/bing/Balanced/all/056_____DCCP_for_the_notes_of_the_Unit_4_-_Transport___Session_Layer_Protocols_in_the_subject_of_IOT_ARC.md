# DCCP

DCCP stands for Datagram Congestion Control Protocol. It is a message-oriented transport layer protocol that provides bidirectional unicast connections of congestion-controlled unreliable datagrams . DCCP is suitable for applications that transfer fairly large amounts of data, but can benefit from control over the tradeoff between timeliness and reliability. Some examples of such applications are streaming media, online games, and voice over IP.

Some of the main features of DCCP are:

- It implements reliable connection setup and teardown, using a three-way handshake and a four-way handshake respectively .
- It supports Explicit Congestion Notification (ECN), which allows routers to mark packets as experiencing congestion instead of dropping them .
- It allows the sender and the receiver to negotiate and select a specific congestion control mechanism, such as TCP-like, TCP-friendly, or TCP-low priority .
- It provides a feature negotiation mechanism, which allows the endpoints to enable or disable optional features, such as acknowledgments, checksums, or encryption .
- It uses a 48-bit sequence number and a 24-bit acknowledgment number to identify and acknowledge packets, which reduces the risk of sequence number wraparound and duplicate packets .
- It uses a generic header and a variable-length options field to encode different types of packets, such as data, acknowledgment, request, response, close, or reset .
- It supports half-closed connections, which allow one endpoint to stop sending data while the other endpoint can continue to send data .

DCCP is designed to be a flexible and extensible protocol that can accommodate different application requirements and network conditions. It is also intended to be compatible with existing network infrastructure and protocols, such as IP, UDP, and ICMP . DCCP is defined in RFC 4340, which was published by the IETF as a proposed standard in March 2006.