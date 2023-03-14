 Here is the content written in markdown format for the given topic:

#### UDP Transport layer protocol

- UDP stands for User Datagram Protocol. It is a connectionless and unreliable transport layer protocol.
- It is a simple protocol with minimal overhead. It provides fast delivery of messages without verification or sequencing.
- Some key points about UDP:

- No connection establishment process. Datagrams are sent directly to the recipient.
- Provides fast transport of messages since there is minimal connection overhead.
- Unreliable - there is no guarantee of delivery, ordering or duplicate protection of datagrams.
- Uses port numbers to identify sending and receiving applications.
- Header size is 8 bytes. Minimal overhead leading to fast speed.
- Often used for real-time applications where speed is priority and some data loss is acceptable like VoIP, online gaming, video streaming, etc.
- Can be used with multicast to send to multiple destinations efficiently.

- A mnemonic to remember features of UDP is:
**U**nreliable and **U**nconnected but **U**ltra fast and small **P**rotocol with port addressing.

- Some advantages and disadvantages:

Advantages:
- Fast: Minimal connection establishment and teardown overhead.
- Efficient: Small header size leading to less bandwidth usage.
- Suitable for real-time applications where speed is priority.

Disadvantages:
- Unreliable: No guarantee of delivery or ordering of datagrams. Can lead to data loss.
- Vulnerable: Since there is no connection establishment, UDP is vulnerable to attacks like spoofing, hijacking, etc.
- Not suitable for applications requiring high reliability.

- Here is a simple ASCII diagram showing UDP packet format:

  UDP Header (8 bytes)
  __________________
  | Source Port |
  | Destination Port |
  | Length |
  | Checksum |
  |        Data        |
  |__________________|

- Some example applications of UDP: DNS, SNMP, DHCP, VoIP, Video streaming, Online gaming, etc.