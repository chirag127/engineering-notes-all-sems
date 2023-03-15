#### ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol that is used by network devices to communicate problems with data transmission  .
- It is mainly used to determine whether data is reaching its intended destination in a timely manner .
- It also performs network diagnostics and reports errors in IP operations .
- ICMP messages are encapsulated in IP datagrams and have a specific format that includes a type, a code, a checksum, and optional data fields.
- Some common ICMP message types are:
  - Echo request and echo reply: used to test the reachability and round-trip time of a destination .
  - Destination unreachable: used to indicate that a destination or a service is unreachable for some reason .
  - Time exceeded: used to indicate that a datagram has expired in transit or in a reassembly queue .
  - Parameter problem: used to indicate that a datagram has an invalid or missing option or header field.
  - Redirect: used to inform a source host of a better route to a destination.
  - Router advertisement and router solicitation: used to discover and advertise routers on a network.
- ICMP is part of the Internet protocol suite as defined in RFC 792.