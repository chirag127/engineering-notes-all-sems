### WAP: Architecture for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless in the subject of Mobile Computing

- WAP stands for Wireless Application Protocol, which is a set of communication protocols that enable wireless devices to access data and services from the Internet or other networks.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. The WAP protocol stack is divided into five layers: Wireless Application Environment (WAE), Wireless Session Protocol (WSP), Wireless Transaction Protocol (WTP), Wireless Transport Layer Security (WTLS), and Wireless Datagram Protocol (WDP).
- WAE is the topmost layer in WAP, which provides the application framework and the content development languages for wireless devices. WAE includes the Wireless Markup Language (WML), which is an XML-based language for creating user interfaces and navigation, and the WMLScript, which is a scripting language for adding logic and interactivity to WML pages. WAE also defines the device specifications and capabilities, such as screen size, color, and input methods.
- WSP is the session layer in WAP, which provides a reliable and efficient way of exchanging data between the client and the server. WSP supports both connection-oriented and connectionless modes, and allows fast connection suspension and reconnection. WSP also provides features such as content negotiation, content encoding, and push services.
- WTP is the transaction layer in WAP, which provides a simplified protocol for request-response transactions over wireless networks. WTP runs on top of a datagram service, such as UDP, and offers reliability, segmentation, and reassembly functions. WTP also supports user datagram, result, and invoke primitives for different types of transactions.
- WTLS is the security layer in WAP, which provides data integrity, privacy, service denial, and authentication services for wireless communications. WTLS is based on the Transport Layer Security (TLS) protocol, but adapted for the wireless environment. WTLS supports various cryptographic algorithms, such as RSA, Diffie-Hellman, and Elliptic Curve Cryptography, and various key exchange and certificate formats, such as X.509 and WTLS certificates.
- WDP is the transport layer in WAP, which provides a consistent data format and a common interface to the higher layers of the WAP protocol stack. WDP allows WAP to be bearer-independent, meaning that it can run over any underlying network technology, such as GSM, CDMA, or Bluetooth. WDP also performs adaptation functions, such as addressing, port mapping, and fragmentation, to suit the characteristics of the network bearer.

The following diagram shows the WAP protocol architecture alongside a typical Internet protocol stack:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      WAE        |    Application  |    Application  |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      WSP        |      HTTP       |      HTTP       |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      WTP        |      TCP        |      TCP        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      WTLS       |      TLS        |      TLS        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|      WDP        |      UDP        |      UDP        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Bearer       |      IP         |      IP         |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Network      |    Network      |    Network      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Physical     |    Physical     |    Physical     |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|    Wireless     |    Internet     |    Wireless     |
|    Device       |    Server       |    Gateway      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
```

Some mnemonics and learning tricks for WAP architecture are: