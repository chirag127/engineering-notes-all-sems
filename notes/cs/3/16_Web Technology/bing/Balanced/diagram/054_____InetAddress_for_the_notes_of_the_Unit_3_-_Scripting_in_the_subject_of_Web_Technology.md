Hello, I am Sydney, your AI assistant. I can help you with your study material for Web Technology. Here is some information about InetAddress for the notes of Unit 3 - Scripting.

### InetAddress
- InetAddress is a class in Java that represents an IP address.
- It can be used to get information about a host, such as its name, address, or reachability.
- It can also be used to create sockets for network communication.
- InetAddress has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively.
- InetAddress provides static methods to create instances of InetAddress, such as:
  - `getByName(String host)`: returns an InetAddress object for the given host name or IP address.
  - `getByAddress(byte[] addr)`: returns an InetAddress object for the given raw IP address in a byte array.
  - `getAllByName(String host)`: returns an array of InetAddress objects for all the IP addresses of the given host name.
  - `getLocalHost()`: returns an InetAddress object for the local host.
- InetAddress also provides instance methods to get information about the InetAddress object, such as:
  - `getHostName()`: returns the host name of the IP address, or the IP address itself if the host name is unknown.
  - `getHostAddress()`: returns the string representation of the IP address in the format x.x.x.x for IPv4 or x:x:x:x:x:x:x:x for IPv6.
  - `getAddress()`: returns the raw IP address in a byte array.
  - `isReachable(int timeout)`: tests if the host is reachable within the given timeout in milliseconds.
  - `isAnyLocalAddress()`: returns true if the IP address is a wildcard address, such as 0.0.0.0 or ::.
  - `isLoopbackAddress()`: returns true if the IP address is a loopback address, such as 127.0.0.1 or ::1.
  - `isLinkLocalAddress()`: returns true if the IP address is a link-local address, such as 169.254.x.x or fe80::x.
  - `isSiteLocalAddress()`: returns true if the IP address is a site-local address, such as 10.x.x.x or fec0::x.
  - `isMulticastAddress()`: returns true if the IP address is a multicast address, such as 224.0.0.0 to 239.255.255.255 or ff00:: to ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff.
- InetAddress is an immutable class, which means that its state cannot be changed once it is created.