The WAP architecture is a layered model that consists of five protocols: Wireless Application Environment (WAE), Wireless Session Protocol (WSP), Wireless Transaction Protocol (WTP), Wireless Transport Layer Security (WTLS), and Wireless Datagram Protocol (WDP). These protocols enable wireless devices to access web content and services through a gateway that adapts the WAP protocols to the Internet protocols, such as HTTP, TCP, and UDP. The WAE layer provides the application environment, which includes the Wireless Markup Language (WML) and the WMLScript, a scripting language for WML. The WSP layer provides session management and caching functions. The WTP layer provides reliable and efficient data transfer over wireless networks. The WTLS layer provides security features, such as encryption, authentication, and integrity protection. The WDP layer provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS.

The following diagram illustrates the basic architecture of a WAP system:

```
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WAP Client    |        |  WAP Gateway   |        |  Web Server    |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WAE           |        |  WAE           |        |  HTML          |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WSP           |        |  WSP           |        |  HTTP          |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WTP           |        |  WTP           |        |  TCP           |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WTLS          |        |  WTLS          |        |  TLS           |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  WDP           |        |  WDP           |        |  UDP           |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
|                |        |                |        |                |
|  Bearer        |<------>|  Bearer        |<------>|  IP            |
|  Services      |        |  Services      |        |                |
|                |        |                |        |                |
+----------------+        +----------------+        +----------------+
```