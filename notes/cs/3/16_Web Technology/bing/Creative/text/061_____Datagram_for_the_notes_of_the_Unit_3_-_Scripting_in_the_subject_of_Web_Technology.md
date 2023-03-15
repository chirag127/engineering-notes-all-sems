### Datagram

- A datagram is a unit of data that is sent from one location to another over a network.
- A datagram is similar to a packet, but does not require confirmation that it has been received.
- A datagram has a header and a payload section.
- The header contains information such as the source and destination addresses, the protocol type, and the length of the datagram.
- The payload contains the actual data that is being transmitted.
- A datagram is self-contained and independent, meaning that it can be routed without relying on previous or future exchanges between the source and destination.
- A datagram provides a connectionless communication service, meaning that there is no established connection or session between the sender and receiver.
- A datagram can be divided into smaller pieces and transmitted without a defined route or guaranteed order of delivery.
- A datagram can be lost, duplicated, corrupted, or delivered out of order due to network congestion, errors, or failures.
- A datagram is suitable for applications that can tolerate some degree of unreliability, such as voice or video streaming, or that require low latency, such as online gaming.
- A datagram is not suitable for applications that require reliable and ordered delivery of data, such as file transfer or email.
- A datagram is used by protocols such as UDP, IP, and ICMP.