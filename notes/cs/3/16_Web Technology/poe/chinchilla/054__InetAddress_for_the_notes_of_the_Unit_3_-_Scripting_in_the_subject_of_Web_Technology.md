### InetAddress

InetAddress is a Java class that represents an IP address. It is used to identify the network address of a host or a computer on a network. Here are some of the important points to remember about InetAddress:

- InetAddress class provides two types of IP addresses: IPv4 and IPv6. IPv4 is a 32-bit IP address whereas IPv6 is a 128-bit IP address.
- The `static` method `getByName()` of the InetAddress class is used to get an instance of InetAddress from a hostname or an IP address string.
- The method `getLocalHost()` of the InetAddress class is used to get the local host address.
- The method `getHostName()` of the InetAddress class is used to get the host name of the InetAddress object.
- The method `getHostAddress()` of the InetAddress class is used to get the IP address string of the InetAddress object.
- The method `isReachable()` of the InetAddress class is used to check if a particular IP address is reachable on the network or not.
- The InetAddress class also provides methods to compare two IP addresses or host names for equality.
- It is important to handle exceptions when using the InetAddress class as it throws `UnknownHostException` when the host name or IP address is invalid or cannot be resolved.

In summary, InetAddress is a useful class for working with IP addresses and host names in Java. By using its methods, we can easily obtain information about the local host or remote hosts on a network.