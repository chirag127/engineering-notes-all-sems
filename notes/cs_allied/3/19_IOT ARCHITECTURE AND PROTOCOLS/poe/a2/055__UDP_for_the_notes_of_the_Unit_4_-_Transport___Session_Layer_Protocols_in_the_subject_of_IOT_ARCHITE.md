 Here is the formal content in Markdown format without any emojis or external links for the given topic:

### UDP for the notes of the Unit 4 - Transport & Session Layer Protocols in the subject of IOT ARCHITECTURE AND PROTOCOLS

1. UDP stands for User Datagram Protocol. It is a connectionless and unreliable transport layer protocol.
2. It is faster than TCP as it does not establish a dedicated end-to-end connection between the client and the server. It just attaches source and destination port numbers to the datagrams and sends them.
3. Due to no connection establishment, there is no connection termination phase in UDP. This makes it faster and more efficient for small packets transmission.
4. As there is no connection, UDP does not guarantee delivery of datagrams or preserves their order. It is an unreliable protocol.
5. UDP is typically used for applications that require fast transmission of data and do not require high reliability. Examples are streaming media, DNS, DHCP, etc.
6. The UDP header size is 8 bytes, comprising of source port, destination port, length and checksum field. The checksum is optional and can be disabled.
7. UDP does not provide any congestion control mechanisms. The applications built on top of UDP must implement congestion control in order to avoid network congestion.

The above points cover the key highlights of UDP protocol for the given topic. Please let me know if you would like me to elaborate on any of the points or add/modify any points.