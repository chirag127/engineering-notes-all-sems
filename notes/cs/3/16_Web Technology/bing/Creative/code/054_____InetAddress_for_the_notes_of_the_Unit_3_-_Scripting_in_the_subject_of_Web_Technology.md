### InetAddress

- The `InetAddress` class in Java represents an Internet Protocol (IP) address, which is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP  .
- The `InetAddress` class is defined in the `java.net` package and can handle both IPv4 and IPv6 addresses   .
- The `InetAddress` class provides methods to get the IP address of any host name, such as www.google.com, www.facebook.com, etc., and vice versa     .
- The `InetAddress` class also provides methods to check if an IP address is a loopback address, a multicast address, a link-local address, a site-local address, etc  .
- The `InetAddress` class is an abstract class and has two subclasses: `Inet4Address` and `Inet6Address`, which represent IPv4 and IPv6 addresses respectively  .
- The `InetAddress` class has no public constructor and can only be instantiated by using static factory methods, such as `getByName`, `getByAddress`, `getAllByName`, `getLocalHost`, etc  .
- The `InetAddress` class implements the `Serializable` interface, which means it can be serialized and deserialized across different platforms  .
- The `InetAddress` class overrides the `equals`, `hashCode`, and `toString` methods from the `Object` class to provide meaningful comparison and representation of IP addresses  .
- The `InetAddress` class also implements the `Comparable` interface, which means it can be sorted according to the numerical value of the IP address.