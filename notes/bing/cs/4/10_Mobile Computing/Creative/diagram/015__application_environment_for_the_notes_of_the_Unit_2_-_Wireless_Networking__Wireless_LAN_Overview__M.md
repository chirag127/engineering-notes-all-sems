The application environment for wireless networking is based on the Wireless Application Protocol (WAP), which is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.

The Wireless Application Environment (WAE), which is part of the WAP, provides an architecture for communication between wireless devices and web servers. It is based mainly on existing technologies and philosophies of the world wide web (WWW), but adapted to the constraints and limitations of wireless networks and devices .

The following diagram illustrates the basic architecture of the WAE:

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Wireless       |      |  Wireless       |      |  Web            |
|  Device         |      |  Gateway        |      |  Server         |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  WAE User       |      |  WAE Proxy      |      |  WAE Server     |
|  Agent          |      |  Agent          |      |  Agent          |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  WAE Library    |      |  WAE Library    |      |  WAE Library    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  WAE Protocols  |      |  WAE Protocols  |      |  WAE Protocols  |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  WAP Protocols  |      |  WAP Protocols  |      |  HTTP           |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Wireless       |      |  Wireless       |      |  TCP/IP         |
|  Network        |      |  Network        |      |  Network        |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

The WAE consists of four components:

- The WAE User Agent, which is a software application on the wireless device that interacts with the user and requests content from the web server via the wireless gateway.
- The WAE Proxy Agent, which is a software application on the wireless gateway that translates between the WAE protocols and the HTTP protocol, and performs caching, filtering, and transcoding of content for the wireless device.
- The WAE Server Agent, which is a software application on the web server that generates and delivers content for the wireless device, using the WAE library and protocols.
- The WAE Library, which is a set of common functions and data formats that are used by the WAE agents to create and process content for the wireless device.

The WAE protocols are:

- The Wireless Markup Language (WML), which is a markup language similar to HTML, but optimized for small screens and low bandwidth.
- The Wireless Markup Language Script (WMLScript), which is a scripting language similar to JavaScript, but optimized for low memory and processing power.
- The Wireless Telephony Application (WTA), which is a set of extensions to WML and WMLScript that enable access to telephony services, such as voice calls, messaging, and phone book.
- The Wireless Datagram Protocol (WDP), which is a transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and TDMA.
- The Wireless Session Protocol (WSP), which is a session layer protocol that provides reliable and secure communication between the wireless device and the wireless gateway, using WDP as the underlying transport.
- The Wireless Transaction Protocol (WTP), which is a transaction layer protocol that provides efficient and reliable request-response services, using WSP as the underlying session protocol.
- The Wireless Application Environment Protocol (WAEP), which is an application layer protocol that defines the format