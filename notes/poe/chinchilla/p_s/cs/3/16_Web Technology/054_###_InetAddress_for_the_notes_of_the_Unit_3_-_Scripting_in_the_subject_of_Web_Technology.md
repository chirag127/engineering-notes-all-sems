### InetAddress

InetAddress is a class in the java.net package that represents an Internet Protocol (IP) address. An IP address is a unique identifier assigned to each device connected to a network. InetAddress class provides methods to manipulate IP addresses.

#### Creating an InetAddress Object

An InetAddress object can be created using one of the following methods:

- `InetAddress.getByName(String host)` - returns an InetAddress object representing the IP address of the given hostname.
- `InetAddress.getByAddress(byte[] ipAddress)` - returns an InetAddress object representing the IP address specified as a byte array.
- `InetAddress.getLocalHost()` - returns an InetAddress object representing the IP address of the local host.

#### Manipulating IP Addresses

Once an InetAddress object is created, the following methods can be used to manipulate IP addresses:

- `getHostAddress()` - returns a string representation of the IP address.
- `getHostName()` - returns the hostname for the IP address.
- `getAddress()` - returns the raw IP address as a byte array.

#### Advantages of InetAddress

- It provides an easy way to manipulate IP addresses.
- It can be used to resolve hostnames to IP addresses and vice versa.
- It can be used to check if a device is reachable over the network.

#### Disadvantages of InetAddress

- It only supports IPv4 and not IPv6.
- It may not work correctly in certain network configurations.

#### Examples

```java
import java.net.*;

public class InetAddressExample {
    public static void main(String[] args) {
        try {
            InetAddress address = InetAddress.getByName("www.google.com");
            System.out.println("Host name: " + address.getHostName());
            System.out.println("IP address: " + address.getHostAddress());
            byte[] ipAddress = {127, 0, 0, 1};
            InetAddress local = InetAddress.getByAddress(ipAddress);
            System.out.println("Local host name: " + local.getHostName());
            System.out.println("Local IP address: " + local.getHostAddress());
        } catch (UnknownHostException e) {
            System.err.println("Unable to resolve hostname");
        }
    }
}
```

Output:

```
Host name: www.google.com
IP address: 172.217.168.36
Local host name: localhost
Local IP address: 127.0.0.1
```

#### Applications

InetAddress can be used in various network-related applications such as:

- Network monitoring and management tools
- Remote desktop applications
- Network-based games and applications
- Web servers and clients