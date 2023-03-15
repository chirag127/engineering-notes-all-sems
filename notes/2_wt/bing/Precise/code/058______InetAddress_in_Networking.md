#### InetAddress in Networking
InetAddress is a class in the `java.net` package that represents an Internet Protocol (IP) address. Here is an example of how to use the InetAddress class to get the IP address of a given hostname:

```java
import java.net.InetAddress;
import java.net.UnknownHostException;

public class InetAddressExample {
    public static void main(String[] args) {
        try {
            InetAddress address = InetAddress.getByName("www.example.com");
            System.out.println(address.getHostAddress());
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
    }
}
```
