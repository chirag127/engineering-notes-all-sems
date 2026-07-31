#### InetAddress in Networking

InetAddress is a class in Java that represents an IP address, which is a unique numerical label assigned to a machine in a network. An IP address can be either 32-bit (IPv4) or 128-bit (IPv6). An instance of InetAddress consists of an IP address and possibly its corresponding host name, depending on whether it is constructed with a host name or whether it has already done reverse host name resolution.

There are two types of IP addresses: unicast and multicast. A unicast address identifies a single interface in a network, and a packet sent to a unicast address is delivered to the interface identified by that address. A multicast address identifies a group of interfaces in a network, and a packet sent to a multicast address is delivered to all the interfaces that belong to the group.

InetAddress class has no visible constructor. To create an instance of InetAddress, one of the factory methods provided by the class must be used. Some of the commonly used factory methods are:

- `getByName(String host)`: Returns an InetAddress object representing the IP address of the given host name.
- `getByAddress(byte[] addr)`: Returns an InetAddress object representing the IP address of the given byte array.
- `getLocalHost()`: Returns an InetAddress object representing the local host address.
- `getAllByName(String host)`: Returns an array of InetAddress objects representing all the IP addresses of the given host name  .

Some of the commonly used methods of InetAddress class are:

- `getHostAddress()`: Returns the IP address string in textual presentation.
- `getHostName()`: Returns the host name for this IP address, or the IP address string if the host name is unknown.
- `isAnyLocalAddress()`: Returns true if this IP address is a wildcard address, which is 0.0.0.0 or ::0.
- `isLoopbackAddress()`: Returns true if this IP address is a loopback address, which is 127.0.0.1 or ::1.
- `isMulticastAddress()`: Returns true if this IP address is a multicast address, which is in the range of 224.0.0.0 to 239.255.255.255 or ff00:: to ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff  .

Here is an example of using InetAddress class in Java:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {

    public static void main(String[] args) {
        try {
            // Get the local host address
            InetAddress local = InetAddress.getLocalHost();
            System.out.println("Local host: " + local);

            // Get the IP address and host name of a given host
            InetAddress google = InetAddress.getByName("www.google.com");
            System.out.println("Google: " + google);

            // Get all the IP addresses of a given host
            InetAddress[] yahoo = InetAddress.getAllByName("www.yahoo.com");
            System.out.println("Yahoo: ");
            for (InetAddress address : yahoo) {
                System.out.println(address);
            }

            // Check if an IP address is a loopback address
            InetAddress loopback = InetAddress.getByName("127.0.0.1");
            System.out.println("Is loopback: " + loopback.isLoopbackAddress());

            // Check if an IP address is a multicast address
            InetAddress multicast = InetAddress.getByName("224.0.0.1");
            System.out.println("Is multicast: " + multicast.isMulticastAddress());

        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
```