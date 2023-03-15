A URL (Uniform Resource Locator) is a unique identifier used to locate a resource on the Internet. It is also referred to as a web address. URLs consist of multiple parts -- including a protocol and domain name -- that tell a web browser how and where to retrieve a resource.

A URLConnection is a class that represents a connection between a Java application and a URL. It allows the application to read from and write to the resource pointed by the URL, using various methods and properties.

A URLConnection can be obtained by calling the openConnection method of a URL object. This method returns a URLConnection object, or one of its protocol specific subclasses, such as HttpURLConnection for HTTP URLs.

The URLConnection object is not connected to the resource until the connect method is called. This method initializes a communication link between the application and the URL over the network.

The following is a possible ASCII diagram for a URL connection in networking:

```
+-----------------+     openConnection     +-----------------+
| Java application| ---------------------->| URL object      |
+-----------------+                        +-----------------+
                                           | protocol        |
                                           | domain name     |
                                           | path            |
                                           | port            |
                                           | reference       |
                                           | query           |
                                           +-----------------+
                                                 | connect
                                                 v
                                           +-----------------+
                                           | URLConnection   |
                                           | object          |
                                           +-----------------+
                                           | connect         |
                                           | getInputStream  |
                                           | getOutputStream |
                                           | getHeaderField  |
                                           | setRequestProperty |
                                           | ...              |
                                           +-----------------+
                                                 | read/write
                                                 v
                                           +-----------------+
                                           | Resource        |
                                           | (web page, file,|
                                           | image, etc.)    |
                                           +-----------------+
```