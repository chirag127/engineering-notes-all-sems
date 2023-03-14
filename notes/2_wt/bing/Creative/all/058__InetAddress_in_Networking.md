#### InetAddress in Networking

- InetAddress is a class in Java Network API that represents an Internet Protocol (IP) address, either a 32-bit or 128-bit unsigned number used by lower-level protocols like UDP and TCP.
- An instance of InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution.
- There are two types of addresses: unicast and multicast.
  - A unicast address is an identifier for a single interface. A packet sent to a unicast address is delivered to the interface identified by that address.
  - A multicast address is an identifier for a set of interfaces (typically belonging to different nodes). A packet sent to a multicast address is delivered to all interfaces identified by that address.
- There are also different scopes of IP addresses, such as link-local, site-local, and global.
  - Link-local addresses are designed to be used for addressing on a single link for purposes such as auto-address configuration, neighbor discovery, or when no routers are present.
  - Site-local addresses are designed to be used for addressing inside of a site without the need for a global prefix.
  - Global addresses are unique across the internet.
- The textual representation of an IP address is address family specific. For IPv4 address format, please refer to Inet4Address#format; For IPv6 address format, please refer to Inet6Address#format.
- The InetAddress class does not have public constructors, so you create a new instance by using one of its factory methods:
  - getByName(String host): creates an InetAddress object based on the provided hostname.
  - getByAddress(byte[] addr): returns an InetAddress object from a byte array of the raw IP address.
  - getAllByName(String host): returns an array of InetAddress objects from the specified hostname, as a hostname can be associated with several IP addresses.
  - getLocalHost(): returns the address of the localhost.
- To get the IP address or hostname, you can use a couple of methods below:
  - getHostAddress(): returns the IP address in text.
  - getHostName(): gets the hostname.
- The InetAddress class also provides several methods for checking the address type, such as isAnyLocalAddress(), isLoopbackAddress(), isMulticastAddress(), etc.
- The InetAddress class's toString() method returns both hostname and IP address, e.g. www.codejava.net/198.57.151.22.
- Inet4Address and Inet6Address are subclasses of the InetAddress class that represent IPv4 and IPv6 addresses, respectively. However, when writing network applications, you don't have to concern about IPv4 or IPv6 as Java hides all the details. The InetAddress can refer to either Inet4Address or Inet6Address so most of the time, using InetAddress is enough.

Here is an example of using the InetAddress class to get the IP address of a given hostname:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {

    public static void main(String[] args) {
        try {
            // create an InetAddress object from a hostname
            InetAddress address = InetAddress.getByName("www.codejava.net");
            // print the IP address
            System.out.println(address.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
```

Output:

```
198.57.151.22
```

Here is a possible mnemonic to remember the factory methods of the InetAddress class:

- getByName: get the address by the name of the host
- getByAddress: get the address by the bytes of the address
- getAllByName: get all the addresses by the name of the host
- getLocalHost: get the address of the local host