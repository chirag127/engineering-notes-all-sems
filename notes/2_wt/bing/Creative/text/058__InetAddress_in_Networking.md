#### InetAddress in Networking

- The InetAddress class in Java represents an Internet Protocol (IP) address, which is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP .
- An IP address can be either IPv4 or IPv6, depending on the address architecture .
- An instance of InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution .
- The InetAddress class does not have public constructors, so it can only be created by using one of its factory methods    :
  - getByName(String host): creates an InetAddress object based on the provided hostname    .
  - getByAddress(byte[] addr): returns an InetAddress object from a byte array of the raw IP address    .
  - getAllByName(String host): returns an array of InetAddress objects from the specified hostname, as a hostname can be associated with several IP addresses    .
  - getLocalHost(): returns the address of the localhost    .
- To get the IP address or hostname from an InetAddress object, one can use the following methods    :
  - getHostAddress(): returns the IP address in text    .
  - getHostName(): gets the hostname    .
  - toString(): returns both hostname and IP address, e.g. www.codejava.net/198.57.151.22   .
- The InetAddress class also provides methods for checking the address type, such as isMulticastAddress(), isAnyLocalAddress(), isLoopbackAddress(), isLinkLocalAddress(), isSiteLocalAddress(), isMCGlobal(), isMCNodeLocal(), isMCLinkLocal(), isMCSiteLocal(), isMCOrgLocal(), isReachable(int), isReachable(NetworkInterface, int, int), etc   .
- The InetAddress class has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses, respectively    . However, most of the time, using InetAddress is enough as Java hides the details of the address types   .

: https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/net/InetAddress.html
: https://www.codejava.net/java-se/networking/java-inetaddress-examples
: https://www.javatpoint.com/InetAddress-class
: https://www.educba.com/java-inetaddress/
: https://docs.oracle.com/javase/7/docs/api/java/net/InetAddress.html