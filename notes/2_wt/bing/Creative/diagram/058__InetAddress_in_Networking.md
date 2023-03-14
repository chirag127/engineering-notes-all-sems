#### InetAddress in Networking

InetAddress is a class in Java that represents an Internet Protocol (IP) address, which is either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP. An instance of InetAddress consists of an IP address and possibly its corresponding host name, depending on how it is constructed or whether it has done reverse host name resolution. There are two types of addresses: unicast and multicast. A unicast address identifies a single interface, while a multicast address identifies a set of interfaces. IP addresses also have different scopes, such as link-local, site-local, and global.

The following diagram illustrates the basic architecture of a InetAddress:

```
+-----------------+     +-----------------+
| InetAddress     |     | InetAddress     |
+-----------------+     +-----------------+
| -hostName       |     | -hostName       |
| -address        |     | -address        |
| -family         |     | -family         |
+-----------------+     +-----------------+
| +getByName()    |     | +getByAddress() |
| +getHostAddress()|    | +getHostName()  |
| +getLocalHost() |     | +getAllByName() |
| +isMulticastAddress()| | +isAnyLocalAddress()|
| +isLoopbackAddress() | | +isLinkLocalAddress()|
| +isSiteLocalAddress()| | +isMCGlobal()   |
| +isMCLinkLocal() |     | +isMCNodeLocal()|
| +isMCSiteLocal() |     | +isMCOrgLocal() |
+-----------------+     +-----------------+
        ^                       ^
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
| Inet4Address    |     | Inet6Address    |
+-----------------+     +-----------------+
|                 |     | -ipaddress      |
|                 |     | -scope_id       |
|                 |     | -scope_id_set   |
|                 |     | -scope_ifname   |
|                 |     | -scope_ifname_set|
+-----------------+     +-----------------+
|                 |     | +getByAddress() |
|                 |     | +getHostAddress()|
|                 |     | +isIPv4CompatibleAddress()|
|                 |     | +isAnyLocalAddress()|
|                 |     | +isLinkLocalAddress()|
|                 |     | +isSiteLocalAddress()|
|                 |     | +isMCGlobal()   |
|                 |     | +isMCLinkLocal()|
|                 |     | +isMCNodeLocal()|
|                 |     | +isMCSiteLocal()|
|                 |     | +isMCOrgLocal() |
+-----------------+     +-----------------+
```

The diagram shows that InetAddress is an abstract class that has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses, respectively. The InetAddress class has several fields and methods that are common to both types of addresses, such as hostName, address, family, getByName, getHostAddress, getLocalHost, getAllByName, and various methods to check the address type and scope. The Inet6Address class has some additional fields and methods that are specific to IPv6 addresses, such as ipaddress, scope_id, scope_ifname, and methods to check the IPv4 compatibility and the multicast scope. The Inet4Address class does not have any additional fields or methods. The diagram also shows that the InetAddress class and its subclasses do not have public constructors, so they can only be created by using the factory methods provided by the class.