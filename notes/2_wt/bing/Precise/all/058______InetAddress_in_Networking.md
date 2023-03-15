#### InetAddress in Networking

- `InetAddress` is a class in the `java.net` package that represents an Internet Protocol (IP) address.
- An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
- The `InetAddress` class provides methods to resolve hostnames to their IP addresses and vice versa.
- The `InetAddress` class has no visible constructors. To create an `InetAddress` object, you have to use one of the available factory methods such as `getByName`, `getAllByName`, or `getLocalHost`.
- `getByName` returns an `InetAddress` object representing the IP address of the given hostname. If the hostname is a literal IP address, this method simply returns an `InetAddress` object created from the given IP address.
- `getAllByName` returns an array of `InetAddress` objects representing all the IP addresses of a given hostname. This is useful when a hostname resolves to multiple IP addresses.
- `getLocalHost` returns the `InetAddress` object representing the local host.
- `getHostName` returns the hostname of the `InetAddress` object.
- `getHostAddress` returns the IP address of the `InetAddress` object in textual representation.
- `isReachable` tests whether that address is reachable.

Here is an example code that demonstrates the use of the `InetAddress` class:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {
    public static void main(String[] args) {
        try {
            InetAddress address = InetAddress.getByName("www.google.com");
            System.out.println("Host name: " + address.getHostName());
            System.out.println("IP address: " + address.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
```

This code creates an `InetAddress` object representing the IP address of the hostname "www.google.com" and prints its hostname and IP address.

A mnemonic to remember the methods of the `InetAddress` class is "NABHLR":
- N: `getByName`
- A: `getAllByName`
- B: `getHostAddress`
- H: `getHostName`
- L: `getLocalHost`
- R: `isReachable`
