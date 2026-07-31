#### InetAddress in Networking

An InetAddress is a class in Java that represents an IP address, both IPv4 and IPv6. An IP address is a unique numerical label assigned to a machine in a network. An InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution.

There are two types of addresses: unicast and multicast. A unicast address identifies a single interface in a network. A packet sent to a unicast address is delivered to the interface identified by that address. A multicast address identifies a group of interfaces in a network. A packet sent to a multicast address is delivered to all the interfaces that belong to the group .

The following diagram shows the structure of an InetAddress object:

```
+-----------------+
| InetAddress     |
+-----------------+
| -hostName       |  // the host name of the IP address, may be null
| -address        |  // the 32-bit or 128-bit IP address in network byte order
| -family         |  // the address family, either IPv4 or IPv6
+-----------------+
| +getByName()    |  // returns an InetAddress object given the host name
| +getByAddress() |  // returns an InetAddress object given the raw IP address
| +getLocalHost() |  // returns the InetAddress object of the local host
| +getHostName()  |  // returns the host name of the IP address, or the IP address itself if the host name is unknown
| +getHostAddress()| // returns the IP address string in textual presentation
| +isAnyLocalAddress()| // returns true if the IP address is a wildcard address
| +isLoopbackAddress()| // returns true if the IP address is a loopback address
| +isLinkLocalAddress()| // returns true if the IP address is a link-local address
| +isSiteLocalAddress()| // returns true if the IP address is a site-local address
| +isMulticastAddress()| // returns true if the IP address is a multicast address
| +isMCGlobal()    |  // returns true if the IP address is a global multicast address
| +isMCNodeLocal() |  // returns true if the IP address is a node-local multicast address
| +isMCLinkLocal() |  // returns true if the IP address is a link-local multicast address
| +isMCSiteLocal() |  // returns true if the IP address is a site-local multicast address
| +isMCOrgLocal()  |  // returns true if the IP address is an organization-local multicast address
+-----------------+
```