#### InetAddress in Networking

- The InetAddress class is used to encapsulate both the numerical IP address and the domain name for that address     .
- An IP address is a unique numerical label assigned to a machine in a network. It can be either 32-bit (IPv4) or 128-bit (IPv6)  .
- An instance of InetAddress represents an IP address with its corresponding host name, which is more convenient and understandable than its IP address     .
- The InetAddress class can handle both IPv4 and IPv6 addresses   .
- There are two types of addresses: Unicast and Multicast .
  - Unicast addresses are used to identify a single host in a network.
  - Multicast addresses are used to identify a group of hosts that can receive the same message.
- The InetAddress class provides methods to create, compare, and resolve IP addresses and host names  .
  - To create an InetAddress object, you can use the static methods getByName, getByAddress, getAllByName, or getLoopbackAddress of the InetAddress class  .
  - To compare two InetAddress objects, you can use the equals, isAnyLocalAddress, isLoopbackAddress, isLinkLocalAddress, isSiteLocalAddress, isMulticastAddress, or isReachable methods of the InetAddress class  .
  - To resolve an IP address to a host name or vice versa, you can use the getHostName, getHostAddress, or getCanonicalHostName methods of the InetAddress class  .
- The InetAddress class is an abstract class that has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively .
- The InetAddress class is immutable, meaning that its state cannot be changed after it is created .