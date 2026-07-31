#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a transport layer protocol that is part of the Internet Protocol suite, also known as UDP/IP suite.
- UDP is a simple, unreliable and connectionless protocol. It does not establish a connection before sending data, nor does it guarantee that the data will be delivered or received in order  .
- UDP adds a 16-byte header to the data from the upper layer. The header contains four fields: source port, destination port, length and checksum. The source and destination ports identify the endpoints of the communication. The length field specifies the total length of the UDP datagram, including the header and the data. The checksum field provides error detection for the header and the data  .

| Source Port | Destination Port |
| ----------- | ---------------- |
| 16 bits     | 16 bits          |

| Length      | Checksum         |
| ----------- | ---------------- |
| 16 bits     | 16 bits          |

- UDP is suitable for applications that require fast, low-overhead and one-way communication, such as streaming audio and video, online gaming, DNS queries and SNMP messages  .
- UDP has some advantages and disadvantages over TCP, the other major transport layer protocol. Some of the advantages are:
  - UDP is simpler and more efficient than TCP, as it does not involve connection setup, acknowledgment, retransmission, congestion control or flow control .
  - UDP allows multicast and broadcast communication, as it can send data to multiple destinations with a single send operation .
  - UDP gives more control to the application layer, as it can decide how to handle the reliability, ordering and congestion issues .
- Some of the disadvantages are:
  - UDP does not provide reliability, ordering or congestion control, which may result in data loss, duplication, delay or jitter .
  - UDP does not provide any mechanism for flow control, which may cause the sender to overwhelm the receiver or the network .
  - UDP is vulnerable to spoofing attacks, as it does not verify the source of the datagrams.

- A possible mnemonic to remember the four fields of the UDP header is: **S**ome **D**ogs **L**ove **C**heese, which stands for **S**ource port, **D**estination port, **L**ength and **C**hecksum. Alternatively, one can use the acronym **SDL**C and associate it with something memorable, such as **S**uper **D**uper **L**ovely **C**at.