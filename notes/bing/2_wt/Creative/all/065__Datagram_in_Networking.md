#### Datagram in Networking

- A datagram is a basic transfer unit associated with a packet-switched network.
- Datagrams are data packets which contain adequate header information so that they can be individually routed by all intermediate network switching devices to the destination.
- Datagrams provide a connectionless communication service across a packet-switched network. This means that there is no need to establish or terminate a connection before or after sending data.
- In a datagram, data is frequently divided and transmitted from source to destination without a predefined route. The network layer is responsible for datagram switching and routing.
- Datagrams are not guaranteed to arrive, arrive in order, or arrive without errors. The transport layer may provide reliability and error correction mechanisms on top of datagrams, such as TCP.
- Datagrams are suitable for applications that require fast and efficient data transfer, such as video streaming, voice over IP, or online gaming.
- Datagrams have some advantages and disadvantages compared to connection-oriented services, such as:

| Advantages | Disadvantages |
|------------|---------------|
| No connection setup or teardown overhead | No guarantee of delivery, order, or error-free transmission |
| More efficient use of network resources | More complex transport layer protocols to ensure reliability |
| More robust to network failures or congestion | More difficult to implement flow and congestion control |
| More flexible and scalable to support dynamic and heterogeneous networks | More vulnerable to security attacks or spoofing |

- A possible mnemonic to remember the characteristics of datagrams is:

**D**ata packets with **A**dequate header information that are **T**ransmitted without a predefined route and provide a **A**connectionless service across a **G**packet-switched network, but are not **R**eliable, **A**rrival-ordered, or **M**error-free.

- A possible ascii diagram to illustrate the structure of a datagram is:

```
+-----------------+-----------------+-----------------+-----------------+
| Source Address  | Destination     | Protocol        | Other Header    |
|                 | Address         |                 | Information     |
+-----------------+-----------------+-----------------+-----------------+
|                                                                     |
|                             Payload/Data                            |
|                                                                     |
+---------------------------------------------------------------------+
```