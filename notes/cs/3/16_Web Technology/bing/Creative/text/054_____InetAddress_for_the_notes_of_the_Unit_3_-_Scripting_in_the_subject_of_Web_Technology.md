### InetAddress

- InetAddress is a class in the java.net package that represents an Internet Protocol (IP) address  .
- An IP address is a 32-bit or 128-bit unsigned number that identifies a host on a network  .
- InetAddress can handle both IPv4 and IPv6 addresses .
- InetAddress provides methods to get the IP address of any host name, such as www.google.com, www.facebook.com, etc .
- InetAddress also provides methods to check if an IP address is a loopback address, a multicast address, a link-local address, etc .
- InetAddress is an abstract class, and it has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively .
- InetAddress objects are immutable, meaning they cannot be modified once created .
- Some of the commonly used methods of InetAddress are:

  - static InetAddress getByName(String host): returns an InetAddress object for the given host name or IP address     .
  - static InetAddress[] getAllByName(String host): returns an array of InetAddress objects for all the IP addresses of the given host name     .
  - static InetAddress getLocalHost(): returns an InetAddress object for the local host     .
  - String getHostName(): returns the host name of the IP address, or the IP address itself if the host name is unknown     .
  - String getHostAddress(): returns the IP address in string format     .
  - boolean isLoopbackAddress(): returns true if the IP address is a loopback address, such as 127.0.0.1 or ::1 .
  - boolean isMulticastAddress(): returns true if the IP address is a multicast address, such as 224.0.0.1 or ff02::1 .
  - boolean isLinkLocalAddress(): returns true if the IP address is a link-local address, such as 169.254.0.1 or fe80::1 .