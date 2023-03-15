### InetAddress

- The `InetAddress` class in Java is defined in the `java.net` package and represents an Internet Protocol (IP) address.
- An IP address is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP to identify hosts on a network.
- The `InetAddress` class can handle both IPv4 and IPv6 addresses and provides methods to get the IP address of any host name, such as `www.google.com`, `www.facebook.com`, etc.
- The `InetAddress` class also provides methods to check if an IP address is a loopback address, a multicast address, a link-local address, or a site-local address.
- The `InetAddress` class is an abstract class and cannot be instantiated directly. Instead, it provides static factory methods to create `InetAddress` objects, such as `getByName(String host)`, `getByAddress(byte[] addr)`, `getAllByName(String host)`, and `getLocalHost()`.
- The `InetAddress` class has the following public methods:

  - `String getHostAddress()`: Returns the IP address string in textual presentation.
  - `String getHostName()`: Returns the host name for this IP address, or the IP address itself if the host name is unknown.
  - `String getCanonicalHostName()`: Returns the fully qualified domain name for this IP address, or the IP address itself if the domain name is unknown.
  - `byte[] getAddress()`: Returns the raw IP address of this `InetAddress` object as an array of bytes.
  - `boolean isAnyLocalAddress()`: Returns `true` if this IP address is a wildcard address, such as `0.0.0.0` or `::`.
  - `boolean isLoopbackAddress()`: Returns `true` if this IP address is a loopback address, such as `127.0.0.1` or `::1`.
  - `boolean isLinkLocalAddress()`: Returns `true` if this IP address is a link-local address, such as `169.254.0.0/16` or `fe80::/10`.
  - `boolean isSiteLocalAddress()`: Returns `true` if this IP address is a site-local address, such as `10.0.0.0/8`, `172.16.0.0/12`, or `fec0::/10`.
  - `boolean isMulticastAddress()`: Returns `true` if this IP address is a multicast address, such as `224.0.0.0/4` or `ff00::/8`.
  - `boolean isMCGlobal()`: Returns `true` if this IP address is a global multicast address, such as `224.0.1.0` to `238.255.255.255` or `ff0e::/16`.
  - `boolean isMCNodeLocal()`: Returns `true` if this IP address is a node-local multicast address, such as `ff01::/16`.
  - `boolean isMCLinkLocal()`: Returns `true` if this IP address is a link-local multicast address, such as `224.0.0.0/24` or `ff02::/16`.
  - `boolean isMCSiteLocal()`: Returns `true` if this IP address is a site-local multicast address, such as `239.255.0.0/16` or `ff05::/16`.
  - `boolean isMCOrgLocal()`: Returns `true` if this IP address is an organization-local multicast address, such as `239.192.0.0/14` or `ff08::/16`.
  - `boolean equals(Object obj)`: Compares this IP address to the specified object and returns `true` if they are equal.
  - `int hashCode()`: Returns a hash code for this IP address.
  - `String toString()`: Returns a string representation of this IP address, such as `/127.0.0.1` or `localhost/127.0.0.1`.