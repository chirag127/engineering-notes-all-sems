#### InetAddress in Networking

- InetAddress is a class in Java that represents an IP address, both IPv4 and IPv6.
- An IP address is a unique numerical label assigned to a machine in a network.
- An instance of InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution.
- There are two types of addresses: unicast and multicast.
  - Unicast addresses identify a single interface in a network. A packet sent to a unicast address is delivered to the interface identified by that address.
  - Multicast addresses identify a group of interfaces in a network. A packet sent to a multicast address is delivered to all the interfaces that belong to the group.
- There are also different scopes of addresses, such as link-local, site-local, global, etc. The scope determines the reachability of the address in a network.
- InetAddress provides methods to create, manipulate, and query IP addresses and host names.
  - To create an InetAddress object, you can use the static methods getByName, getByAddress, getAllByName, or getLoopbackAddress.
  - To manipulate an InetAddress object, you can use the methods isAnyLocalAddress, isLoopbackAddress, isLinkLocalAddress, isSiteLocalAddress, isMulticastAddress, isMCGlobal, isMCNodeLocal, isMCLinkLocal, isMCSiteLocal, isMCOrgLocal, isReachable, etc.
  - To query an InetAddress object, you can use the methods getHostAddress, getHostName, getCanonicalHostName, getAddress, etc.
- InetAddress is an abstract class, and it has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively.
- InetAddress is immutable, meaning that its state cannot be changed after creation.
- InetAddress does not have a public constructor, meaning that you cannot create an instance of it using the new keyword. You have to use the static methods mentioned above to obtain an instance of it.

Some examples of using InetAddress are:

- To get the IP address of a host name:

```java
InetAddress address = InetAddress.getByName("www.google.com");
System.out.println(address.getHostAddress()); // prints 142.250.74.196
```

- To get the host name of an IP address:

```java
InetAddress address = InetAddress.getByAddress(new byte[]{(byte)142, (byte)250, (byte)74, (byte)196});
System.out.println(address.getHostName()); // prints www.google.com
```

- To get all the IP addresses of a host name:

```java
InetAddress[] addresses = InetAddress.getAllByName("www.google.com");
for (InetAddress address : addresses) {
  System.out.println(address.getHostAddress()); // prints 142.250.74.196, 2404:6800:4006:80a::2004, etc.
}
```

- To check if an IP address is reachable:

```java
InetAddress address = InetAddress.getByName("www.google.com");
System.out.println(address.isReachable(1000)); // prints true if reachable within 1000 milliseconds, false otherwise
```

- To get the loopback address of the local machine:

```java
InetAddress address = InetAddress.getLoopbackAddress();
System.out.println(address.getHostAddress()); // prints 127.0.0.1
```

Some mnemonics and learning tricks for InetAddress are:

- Remember that InetAddress is an abstract class, and you cannot create an instance of it using the new keyword. You have to use the static methods that start with get to obtain an instance of it.
- Remember that InetAddress is immutable, meaning that its state cannot be changed after creation. You cannot modify its IP address or host name.
- Remember that there are two types of addresses: unicast and multicast. Unicast addresses identify a single interface, while multicast addresses identify a group of interfaces. You can use the methods that start with is to check the type of an address.
- Remember that there are different scopes of addresses, such as link-local, site-local, global, etc. The scope determines the reachability of the address in a network. You can use the methods that start with is to check the scope of an address.
- Remember that InetAddress provides methods to create, manipulate, and query IP addresses and host names. You can use the methods that start with get to obtain information about an address, such as its host address, host name, canonical host name, address bytes, etc. You can also use the