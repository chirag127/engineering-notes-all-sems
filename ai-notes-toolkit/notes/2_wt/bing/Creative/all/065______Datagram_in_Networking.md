#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. This means that there is no need to establish or terminate a connection before or after sending data.
- In a datagram, data is frequently divided and transmitted from source to destination without a predefined route. The order of delivery to the receiver end is not guaranteed.
- Datagrams are suitable for applications that require fast and efficient data transmission, such as video streaming, voice over IP, or online gaming.
- Datagrams are also resilient to network failures, as they can be rerouted by different paths if some links or nodes are down.
- However, datagrams also have some disadvantages, such as:
  - They may incur high overhead due to the header information in each datagram.
  - They may suffer from congestion and packet loss in the network, as there is no flow control or error control mechanism.
  - They may not preserve the integrity or reliability of the data, as there is no acknowledgment or retransmission scheme.
  - They may not support quality of service or security features, as there is no negotiation or encryption process.

- A possible mnemonic to remember the characteristics of datagrams is:

  - **D**ivided data
  - **A**dequate header
  - **T**ransfer unit
  - **A**rrival not guaranteed
  - **G**o without connection
  - **R**outed individually
  - **A**pplications that need speed and efficiency
  - **M**ay have drawbacks

- A possible ASCII diagram to illustrate the structure of a datagram is:

```
  +-----------------+-----------------+-----------------+
  | Source Address  | Destination     | Data Length     |
  |                 | Address         |                 |
  +-----------------+-----------------+-----------------+
  | Data (Payload)                                              |
  |                                                             |
  +-------------------------------------------------------------+
```