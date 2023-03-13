#### InetAddress in Networking

- InetAddress is a class in Java that represents an IP address, which is a numerical identifier for a device on a network.
- InetAddress provides methods to get information about an IP address, such as its hostname, its network interface, its reachability, and its type (IPv4 or IPv6).
- InetAddress also provides methods to create an InetAddress object from a hostname or an IP address string, and to check if two InetAddress objects are equal or belong to the same network.
- Some of the common methods of InetAddress are:

  - `static InetAddress getByName(String host)`: returns an InetAddress object for the given hostname or IP address string. Throws an UnknownHostException if the host is not found.
  - `static InetAddress[] getAllByName(String host)`: returns an array of InetAddress objects for the given hostname or IP address string. Throws an UnknownHostException if the host is not found.
  - `static InetAddress getLocalHost()`: returns an InetAddress object for the local host. Throws an UnknownHostException if the local host is not found.
  - `static InetAddress getByAddress(byte[] addr)`: returns an InetAddress object for the given byte array representing an IP address. Throws an UnknownHostException if the byte array is not valid.
  - `static InetAddress getByAddress(String host, byte[] addr)`: returns an InetAddress object for the given hostname and byte array representing an IP address. Throws an UnknownHostException if the hostname or the byte array is not valid.
  - `String getHostName()`: returns the hostname of the InetAddress object, or the IP address string if the hostname is not known.
  - `String getHostAddress()`: returns the IP address string of the InetAddress object.
  - `byte[] getAddress()`: returns the byte array representing the IP address of the InetAddress object.
  - `boolean isReachable(int timeout)`: returns true if the InetAddress object is reachable within the given timeout in milliseconds, false otherwise.
  - `boolean isLoopbackAddress()`: returns true if the InetAddress object is a loopback address, such as 127.0.0.1 or ::1, false otherwise.
  - `boolean isAnyLocalAddress()`: returns true if the InetAddress object is a wildcard address, such as 0.0.0.0 or ::, false otherwise.
  - `boolean isLinkLocalAddress()`: returns true if the InetAddress object is a link-local address, such as 169.254.x.x or fe80::x, false otherwise.
  - `boolean isSiteLocalAddress()`: returns true if the InetAddress object is a site-local address, such as 10.x.x.x or fec0::x, false otherwise.
  - `boolean isMulticastAddress()`: returns true if the InetAddress object is a multicast address, such as 224.x.x.x or ffxx::x, false otherwise.
  - `boolean isMCGlobal()`: returns true if the InetAddress object is a global multicast address, such as 224.0.1.x or ff0x::x, false otherwise.
  - `boolean isMCOrgLocal()`: returns true if the InetAddress object is an organization-local multicast address, such as 239.x.x.x or ff18::x, false otherwise.
  - `boolean isMCSiteLocal()`: returns true if the InetAddress object is a site-local multicast address, such as 239.255.x.x or ff15::x, false otherwise.
  - `boolean isMCLinkLocal()`: returns true if the InetAddress object is a link-local multicast address, such as 224.0.0.x or ff02::x, false otherwise.
  - `boolean isMCNodeLocal()`: returns true if the InetAddress object is a node-local multicast address, such as ff01::x, false otherwise.
  - `boolean equals(Object obj)`: returns true if the InetAddress object is equal to the given object, false otherwise. Two InetAddress objects are equal if they represent the same IP address.
  - `int hashCode()`: returns the hash code of the InetAddress object, which is based on its IP address.
  - `String toString()`: returns a string representation of the InetAddress object, which is the hostname followed by a slash and the IP address.

- An example of using InetAddress in Java is:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {

  public static void main(String[] args) {
    try {
      // Get an InetAddress object for www.google.com
      InetAddress google = InetAddress.getByName("www.google.com");
      // Print its hostname and IP address
      System.out.println("Hostname: " + google.getHostName());
      System.out.println("IP address: " + google.getHostAddress());
      //