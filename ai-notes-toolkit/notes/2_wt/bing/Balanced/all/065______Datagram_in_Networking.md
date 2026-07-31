#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. This means that there is no need to establish or terminate a connection before or after sending data.
- In a datagram, data is frequently divided and transmitted from source to destination without a predefined route. The order of delivery to the receiver end is not guaranteed.
- Datagrams are typically structured in header and payload sections. The header contains information such as the source and destination addresses, the length of the datagram, and the protocol type. The payload contains the actual data to be transmitted.
- Datagrams are suitable for applications that require fast and efficient data transfer, such as video streaming, voice over IP, and online gaming.
- Datagrams have some disadvantages, such as:
  - They may be lost, duplicated, or corrupted during transmission due to network congestion, errors, or failures.
  - They may arrive out of order or with variable delays, which can affect the quality of service and the reliability of the communication.
  - They may not fit into the maximum transmission unit (MTU) of the underlying network, and thus need to be fragmented and reassembled at the endpoints.
- A possible mnemonic to remember the features of datagrams is: **D**ata **A**rrives **T**hrough **A**ny **G**ateway **R**egardless of **A**ny **M**ethod (DATAGRAM).