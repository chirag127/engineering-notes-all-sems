### InetAddress

- `InetAddress` is a class in the `java.net` package that represents an Internet Protocol (IP) address.
- An IP address is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication.
- The `InetAddress` class provides methods to resolve hostnames to their IP addresses and vice versa.
- The `InetAddress` class has no public constructor. Instead, instances of this class are created using the factory methods `getByName()`, `getAllByName()`, and `getLocalHost()`.
- The `getByName()` method returns an `InetAddress` object representing the IP address of the given hostname.
- The `getAllByName()` method returns an array of `InetAddress` objects representing all the IP addresses of the given hostname.
- The `getLocalHost()` method returns an `InetAddress` object representing the local host's IP address.
- The `InetAddress` class also provides methods to check if an `InetAddress` object represents a loopback address, a link-local address, or a site-local address.
- The `getHostName()` method returns the hostname of the `InetAddress` object.
- The `getHostAddress()` method returns the IP address of the `InetAddress` object in textual representation.
- The `getCanonicalHostName()` method returns the fully qualified domain name of the `InetAddress` object.
