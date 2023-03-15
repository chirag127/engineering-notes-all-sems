# InetAddress

- InetAddress is a class in the java.net package that represents an Internet Protocol (IP) address  .
- An IP address is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP  .
- InetAddress can handle both IPv4 and IPv6 addresses  .
- InetAddress consists of an IP address and possibly its corresponding host name.
- InetAddress provides methods to get the IP address of any host name, such as www.google.com, www.facebook.com, etc  .
- InetAddress also provides methods to check if an IP address is a loopback address, a multicast address, a link-local address, etc  .
- InetAddress is an abstract class, and it has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively  .
- InetAddress objects are immutable, meaning they cannot be modified once created  .
- InetAddress objects can be created by using the static methods of the InetAddress class, such as getByName, getByAddress, getAllByName, getLoopbackAddress, etc  .
- InetAddress objects can be compared for equality by using the equals method, or for ordering by using the isAnyLocalAddress, isLoopbackAddress, isLinkLocalAddress, etc methods  .