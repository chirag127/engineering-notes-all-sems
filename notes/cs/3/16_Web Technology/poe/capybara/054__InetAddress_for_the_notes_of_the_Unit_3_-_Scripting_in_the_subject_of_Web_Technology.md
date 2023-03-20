### InetAddress

InetAddress is a class in Java that represents an Internet Protocol (IP) address. It is used to encapsulate both the numerical IP address and the hostname. Here are some important points to note about InetAddress:

- InetAddress is a part of the java.net package, so it must be imported to be used in a Java program.
- There are two types of InetAddress: IPv4 and IPv6. IPv4 is the older version and uses a 32-bit address, while IPv6 is the newer version and uses a 128-bit address.
- The InetAddress class provides methods to get the hostname, IP address, and canonical hostname for a given InetAddress object.
- To create an InetAddress object, you can use the following static methods provided by the InetAddress class:

  - `getByName(String host)`: Returns an InetAddress object that represents the IP address of the given hostname.
  - `getByAddress(byte[] addr)`: Returns an InetAddress object that represents the IP address specified by the byte array.
  - `getLocalHost()`: Returns an InetAddress object that represents the IP address of the local host.

- InetAddress objects can be used in conjunction with other classes in the java.net package to perform network communication. For example, a Socket object can be created using an InetAddress object to connect to a remote host.

In summary, InetAddress is a useful class in Java for working with IP addresses and hostnames. It provides methods to get information about an IP address or hostname and can be used in network communication.