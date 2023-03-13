### WAP: Architecture for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- WAP stands for Wireless Application Protocol, which is a set of communication protocols for enabling wireless access to the Internet and other services from mobile devices .
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: This layer contains the Wireless Application Environment (WAE), which is the interface for content developers and application programmers. WAE includes an XML-based markup language called the Wireless Markup Language (WML), which is used to create web pages for wireless devices . WML also supports scripting, variables, and events to enable dynamic and interactive content. WAE also provides a Wireless Telephony Application (WTA) interface, which allows access to telephony services such as call control, phone book, and messaging.
  - Session Layer: This layer contains the Wireless Session Protocol (WSP), which provides a reliable and efficient session service for WAE applications. WSP supports both connection-oriented and connectionless modes, and can handle long-lived sessions across multiple requests and responses. WSP also supports features such as content type negotiation, user agent profiling, and push services.
  - Transaction Layer: This layer contains the Wireless Transaction Protocol (WTP), which provides a lightweight transaction service for WSP. WTP supports three classes of transactions: unreliable one-way, reliable one-way, and reliable two-way. WTP also supports features such as segmentation and reassembly, retransmission, and acknowledgement.
  - Security Layer: This layer contains the Wireless Transport Layer Security (WTLS), which provides data integrity, privacy, and authentication for WAP applications. WTLS is based on the Transport Layer Security (TLS) protocol, but adapted for the wireless environment. WTLS supports features such as data encryption, data compression, certificate-based authentication, and handshake protocols.
  - Transport Layer: This layer contains the Wireless Datagram Protocol (WDP), which provides a common data format and interface for WAP applications. WDP is independent of the underlying network technology, and can operate over various bearers such as GSM, CDMA, SMS, and IP. WDP also supports features such as port numbers, fragmentation, and concatenation.
- The WAP architecture also includes two types of entities: the user agent and the origin server. The user agent is the software component that runs on the wireless device and interacts with the WAE applications. The origin server is the software component that runs on the web server and delivers the WAE content to the user agent. Between the user agent and the origin server, there may be one or more intermediaries, such as proxies, gateways, and caches, that perform various functions such as protocol translation, content adaptation, and data compression.
- The WAP architecture is illustrated in the following diagram:

```
+-----------------+   +-----------------+   +-----------------+
|  Application    |   |  Application    |   |  Application    |
|  Layer          |   |  Layer          |   |  Layer          |
+-----------------+   +-----------------+   +-----------------+
|  Session        |   |  Session        |   |  Session        |
|  Layer          |   |  Layer          |   |  Layer          |
+-----------------+   +-----------------+   +-----------------+
|  Transaction    |   |  Transaction    |   |  Transaction    |
|  Layer          |   |  Layer          |   |  Layer          |
+-----------------+   +-----------------+   +-----------------+
|  Security       |   |  Security       |   |  Security       |
|  Layer          |   |  Layer          |   |  Layer          |
+-----------------+   +-----------------+   +-----------------+
|  Transport      |   |  Transport      |   |  Transport      |
|  Layer          |   |  Layer          |   |  Layer          |
+-----------------+   +-----------------+   +-----------------+
|  Bearer         |   |