### WAP: Architecture

- WAP stands for Wireless Application Protocol. It is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: Wireless Application Environment (WAE). This layer is of most interest to content developers because it contains among other things, device specifications, content formats, scripting languages, and protocols for content delivery and user interaction. The main components of this layer are:
    - Wireless Markup Language (WML): An XML-based markup language that defines the content and layout of web pages for wireless devices. WML is optimized for small screens, low bandwidth, and limited input capabilities.
    - Wireless Markup Language Script (WMLScript): A scripting language that allows dynamic content generation and client-side logic on wireless devices. WMLScript is similar to JavaScript, but with some differences and limitations.
    - Wireless Telephony Application (WTA): A set of extensions to WML and WMLScript that enable telephony services, such as call control, messaging, phone book, and voice mail, on wireless devices.
    - Wireless Datagram Protocol (WDP): A protocol that provides a common interface for data transport across different wireless networks, such as GSM, CDMA, and TDMA. WDP acts as an adaptation layer that maps WAP requests and responses to the specific features of the underlying network.
  - Session Layer: Wireless Session Protocol (WSP). This layer provides session management and service invocation for WAP applications. WSP supports two modes of operation: connection-oriented and connectionless. In connection-oriented mode, WSP establishes a reliable session between the client and the server, and provides features such as segmentation, reassembly, retransmission, and transaction management. In connectionless mode, WSP provides a simple datagram service that does not require a session establishment or maintenance.
  - Transaction Layer: Wireless Transaction Protocol (WTP). This layer provides a lightweight transaction-oriented service on top of WDP. WTP supports three classes of transactions: unreliable one-way, reliable one-way, and reliable two-way. WTP also provides features such as user datagram segmentation, reassembly, and retransmission, as well as optional acknowledgment and confirmation mechanisms.
  - Security Layer: Wireless Transport Layer Security (WTLS). This layer provides data integrity, privacy, and authentication for WAP communications. WTLS is based on the Transport Layer Security (TLS) protocol, but with some modifications and optimizations for wireless environments. WTLS supports various cryptographic algorithms, such as RSA, Diffie-Hellman, and Elliptic Curve, and various cipher suites, such as RC4, DES, and AES.
  - Transport Layer: Wireless Transport Protocol (WTP). This layer provides a reliable transport service on top of WDP. WTP supports features such as congestion control, flow control, and error recovery. WTP also provides optional features such as delayed acknowledgments, selective acknowledgments, and fast retransmit.

- The WAP architecture also includes some additional components, such as:
  - WAP Gateway: A server that acts as an intermediary between the wireless network and the internet. The WAP gateway performs functions such as protocol translation, content encoding and decoding, content adaptation, and caching.
  - WAP Proxy: A server that acts as a proxy for the wireless device. The WAP proxy performs functions such as content filtering, access control, and caching.
  - WAP Push: A mechanism that allows the server to initiate a WAP session and push content to the wireless device. The WAP push uses a protocol called Wireless Push Access Protocol (WPAP), which is based on WSP and WTP.
  - WAP Browser: A software application that runs on the wireless device and allows the user to access WAP content and services. The WAP browser interprets WML, WMLScript, and WTA, and communicates with the WAP gateway and the WAP server using WDP, WSP, WTP, and WTLS.

- The following diagram illustrates the WAP architecture and the protocol stack:

```
+-----------------+    +-----------------+    +-----------------+
|  WAP Server     |    |  WAP Gateway    |    |  WAP Device