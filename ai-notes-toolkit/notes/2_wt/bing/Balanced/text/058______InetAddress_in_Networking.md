#### InetAddress in Networking

- InetAddress is a class in Java that represents an IP address, which is a numerical identifier for a device on a network.
- InetAddress provides methods to get information about an IP address, such as its hostname, its domain name, its type (IPv4 or IPv6), and its reachability.
- InetAddress also provides methods to create an InetAddress object from a hostname, a domain name, or a byte array, and to check if two InetAddress objects are equal or belong to the same network.
- InetAddress is an abstract class, which means it cannot be instantiated directly. Instead, it has two subclasses: Inet4Address and Inet6Address, which represent IPv4 and IPv6 addresses respectively.
- To obtain an InetAddress object, one can use the static methods of the InetAddress class, such as getByName, getByAddress, getLocalHost, getAllByName, or getLoopbackAddress.
- Some examples of using the InetAddress class are:

  - To get the IP address of a hostname:

    ```java
    InetAddress address = InetAddress.getByName("www.google.com");
    System.out.println(address); // prints /142.250.181.4
    ```

  - To get the hostname of an IP address:

    ```java
    InetAddress address = InetAddress.getByAddress(new byte[]{(byte) 142, (byte) 250, (byte) 181, (byte) 4});
    System.out.println(address.getHostName()); // prints www.google.com
    ```

  - To get the local IP address of the device:

    ```java
    InetAddress address = InetAddress.getLocalHost();
    System.out.println(address); // prints /192.168.1.100
    ```

  - To get all the IP addresses associated with a domain name:

    ```java
    InetAddress[] addresses = InetAddress.getAllByName("www.google.com");
    for (InetAddress a : addresses) {
      System.out.println(a); // prints /142.250.181.4, /142.250.181.36, /142.250.181.68, etc.
    }
    ```

  - To get the loopback address, which is used to refer to the device itself:

    ```java
    InetAddress address = InetAddress.getLoopbackAddress();
    System.out.println(address); // prints /127.0.0.1
    ```