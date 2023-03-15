### Datagram

- A datagram is a unit of data that is sent from one location to another over a network .
- A datagram is composed of a header and a payload. The header contains information such as the source and destination addresses, the length of the datagram, and the protocol type. The payload contains the actual data to be transmitted.
- A datagram is a self-contained and independent entity of data, meaning that it does not depend on any previous or subsequent datagrams for its delivery or interpretation.
- A datagram is a connectionless service, meaning that it does not require any prior establishment or termination of a connection between the sender and the receiver. Each datagram is treated as a separate and independent transmission .
- A datagram is an unreliable service, meaning that it does not guarantee the delivery, order, or integrity of the datagrams. Datagrams may be lost, duplicated, corrupted, or delivered out of order by the network .
- A datagram is a best-effort service, meaning that it tries to deliver the datagrams as fast and as accurately as possible, but does not provide any feedback or error correction mechanisms .
- A datagram is suitable for applications that can tolerate some loss or delay of data, such as voice or video streaming, or that can implement their own error control mechanisms, such as TCP .