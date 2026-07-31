### InetAddress

- InetAddress is a class in the java.net package that represents an Internet Protocol (IP) address  .
- An IP address is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP  .
- InetAddress can handle both IPv4 and IPv6 addresses  .
- InetAddress consists of an IP address and possibly its corresponding host name.
- InetAddress class provides methods to get the IP address of any host name, such as www.google.com, www.facebook.com, etc .
- InetAddress class also provides methods to check if an IP address is a loopback address, a multicast address, a link-local address, etc .
- InetAddress class is an abstract class and has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively .
- InetAddress class does not have a public constructor. Instead, it provides static factory methods to create instances of InetAddress, such as getByName, getByAddress, getAllByName, etc  .
- InetAddress class implements the Serializable interface, which means it can be serialized and deserialized .
- InetAddress class overrides the equals, hashCode, and toString methods from the Object class .