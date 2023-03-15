# ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol that is used by network devices to communicate problems with data transmission  .
- It is mainly used to determine whether data is reaching its intended destination in a timely manner .
- It is also used for reporting errors and performing network diagnostics .
- ICMP messages are typically generated in response to errors in IP operations, such as unreachable hosts, network congestion, or time exceeded.
- ICMP messages are encapsulated within IP datagrams, and have a specific format that consists of a type, a code, a checksum, and a data field.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the connectivity between two hosts using the ping command .
  - Destination unreachable: used to inform the sender that the destination host or network is unreachable for some reason .
  - Time exceeded: used to inform the sender that the datagram has expired in transit due to a hop limit or a timeout .
  - Parameter problem: used to inform the sender that the datagram has an invalid or missing field in the IP header.
  - Source quench: used to inform the sender that the receiver or a router is experiencing congestion and requests the sender to reduce the sending rate.
  - Redirect: used to inform the sender that there is a better route to the destination and to update its routing table accordingly.
  - Router advertisement and router solicitation: used to discover and advertise the presence of routers on a network.