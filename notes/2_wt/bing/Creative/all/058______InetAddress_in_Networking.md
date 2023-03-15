#### InetAddress in Networking

- An InetAddress is a Java class that represents an IP address, both IPv4 and IPv6  .
- An IP address is a unique numerical label assigned to a machine in a network  .
- An IP address is either 32-bit (IPv4) or 128-bit (IPv6) long    .
- An InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution .
- Reverse host name resolution is the process of finding the host name associated with an IP address .
- An InetAddress can be either unicast or multicast  .
- A unicast address identifies a single interface in a network. A packet sent to a unicast address is delivered to the interface identified by that address .
- A multicast address identifies a group of interfaces in a network. A packet sent to a multicast address is delivered to all the interfaces that belong to the group .
- An InetAddress can also have a scope, which defines the range of the network where the address is valid.
- The scope can be link-local, site-local, global, or loopback.
- A link-local address is valid only on the same link (network segment) as the interface.
- A site-local address is valid only on the same site (network domain) as the interface.
- A global address is valid on any network in the Internet.
- A loopback address is used to refer to the local host (the same machine as the interface).
- The loopback address is 127.0.0.1 for IPv4 and ::1 for IPv6.
- An InetAddress can be created by using the static methods of the InetAddress class, such as getByName, getByAddress, getAllByName, getLoopbackAddress, etc    .
- An InetAddress can be used with other classes in the Java Network API, such as Socket, ServerSocket, DatagramPacket, and DatagramSocket, to establish network connections and exchange data    .