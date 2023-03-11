 Here is the content written in markdown format for the topic ### InetAddress for the notes of the Unit 3 - Scripting in the subject of Web Technology:

### InetAddress

- InetAddress represents an Internet Protocol (IP) address. It can be an IPv4 address or an IPv6 address.
- It is used to get the host name from the IP address and vice versa.
- It provides methods to check if the address is a valid address or if it is a multicast address.
- Methods:

getAddress() - Returns the raw IP address in an integer format.
getHostAddress() - Returns the IP address as a string.
getHostName() - Returns the hostname for the IP address.
isAnyLocalAddress() - Checks if the address is a wildcard address. Returns boolean.
isLinkLocalAddress() - Checks if the address is a link-local address. Returns boolean.
isLoopbackAddress() - Checks if the address is a loopback address. Returns boolean.
isMCGlobal() - Checks if the address is a multicast address with global scope. Returns boolean.
isMCLinkLocal() - Checks if the address is a multicast address with link-local scope. Returns boolean.
isMCNodeLocal() - Checks if the address is a multicast address with node-local scope. Returns boolean.
isMCOrgLocal() - Checks if the address is a multicast address with organization-local scope. Returns boolean.
isMCSiteLocal() - Checks if the address is a multicast address with site-local scope. Returns boolean.

- Example:

```
import java.net.InetAddress;

public class InetAddressExample {
    public static void main(String[] args) throws UnknownHostException {
        InetAddress ip = InetAddress.getByName("www.google.com");
        System.out.println(ip);
        System.out.println(ip.getHostName());
        System.out.println(ip.getHostAddress());
        System.out.println(ip.isReachable(5000));
    }
}
```

Output:
www.google.com/74.125.21.103
www.google.com
74.125.21.103
true

- Applications: Used in networking applications to get IP address and host name information. Commonly used to check reachability of a host, validate IP addresses, etc.