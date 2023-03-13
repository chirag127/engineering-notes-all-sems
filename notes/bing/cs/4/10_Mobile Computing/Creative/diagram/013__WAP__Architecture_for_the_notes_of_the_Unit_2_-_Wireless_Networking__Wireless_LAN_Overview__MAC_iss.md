The following is a detailed ASCII diagram for WAP: Architecture for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing.

The WAP architecture is composed of various protocols and an XML-based markup language called the Wireless Markup Language (WML), which is the successor to the Handheld Device Markup Language (HDML) as defined by Openwave Systems.

The WAP architecture is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:

- Application Layer: This layer contains the Wireless Application Environment (WAE), which provides a framework for developing and delivering wireless applications. The WAE includes WML, WMLScript, Wireless Telephony Application (WTA), and content formats such as images, sounds, and text.
- Session Layer: This layer contains the Wireless Session Protocol (WSP), which provides a reliable and efficient session service for wireless applications. The WSP supports features such as connection-oriented and connectionless modes, session suspend and resume, and push and pull methods.
- Transaction Layer: This layer contains the Wireless Transaction Protocol (WTP), which provides a lightweight transaction-oriented service for wireless applications. The WTP supports features such as reliable request/response, unreliable request/response, and one-way transactions.
- Security Layer: This layer contains the Wireless Transport Layer Security (WTLS), which provides data integrity, privacy, and authentication for wireless communications. The WTLS is based on the Transport Layer Security (TLS) protocol, but optimized for wireless networks.
- Transport Layer: This layer contains the Wireless Datagram Protocol (WDP), which provides a common interface for different wireless network technologies. The WDP abstracts the underlying network characteristics and provides a consistent data service for the upper layers.

The WAP architecture also includes two types of entities: the user agent and the origin server. The user agent is the software component that runs on the wireless device and interacts with the WAE. The origin server is the software component that runs on the web server and delivers the WAE content to the user agent.

The WAP architecture also involves a gateway, which is an intermediary between the user agent and the origin server. The gateway performs functions such as protocol translation, content encoding and decoding, and security services.

The following ASCII diagram illustrates the basic architecture of WAP:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|   User Agent    |        |    Gateway      |        |  Origin Server  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|      WAE        |        |      WAE        |        |      WAE        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|      WSP        |        |      WSP        |        |      HTTP       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|      WTP        |        |      WTP        |        |      TCP        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|      WTLS       |        |      WTLS       |        |      TLS        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|      WDP        |        |      WDP        |        |      IP         |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Wireless       |        |  Wired          |        |  Wired          |
|  Network        |        |  Network        |        |  Network        |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```