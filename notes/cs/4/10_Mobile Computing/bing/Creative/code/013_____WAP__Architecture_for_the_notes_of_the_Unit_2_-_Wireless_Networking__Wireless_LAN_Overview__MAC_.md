# WAP: Architecture

- Wireless Application Protocol (WAP) is a specification for a set of communication protocols to standardize the way wireless devices, such as mobile phones and radio transceivers, can be used for internet access, including email, the web, newsgroups and instant messaging.
- WAP is designed in a layered fashion, so that it can be extensible, flexible, and scalable. As a result, the WAP protocol stack is divided into five layers:
  - Application Layer: Wireless Application Environment (WAE). This layer is of most interest to content developers because it contains among other things, device specifications, content formats, and scripting languages. WAE uses Wireless Markup Language (WML) and WMLScript as the main technologies for creating web applications for mobile devices.
  - Session Layer: Wireless Session Protocol (WSP). This layer provides the upper-level application layer with a consistent interface for two session services: connection-oriented and connectionless. WSP also handles the security aspects of the communication, such as encryption and authentication.
  - Transaction Layer: Wireless Transaction Protocol (WTP). This layer provides a reliable request/response service on top of an unreliable datagram service. WTP supports three classes of transactions: unreliable, reliable, and secure. WTP also handles the retransmission and acknowledgement mechanisms for the data packets.
  - Security Layer: Wireless Transport Layer Security (WTLS). This layer provides data integrity, privacy, and authentication services for the wireless communication. WTLS is based on the Transport Layer Security (TLS) protocol, but it is optimized for the wireless environment. WTLS uses encryption algorithms, such as RSA, DES, and RC4, to protect the data from eavesdropping and tampering.
  - Transport Layer: Wireless Datagram Protocol (WDP). This layer provides a common interface for the upper layers to access different wireless networks, such as GSM, CDMA, and CDPD. WDP adapts the transport layer of the underlying network to a common format, so that the upper layers do not need to know the specific characteristics of each network.
- The WAP architecture also includes a WAP gateway, which is a server that acts as an intermediary between the wireless network and the internet. The WAP gateway performs several functions, such as:
  - Translating between HTTP and WAP protocols
  - Encoding and decoding the data using binary formats to reduce the bandwidth consumption
  - Compressing and decompressing the data to improve the transmission speed
  - Caching the data to reduce the network traffic
  - Filtering the data to adapt to the capabilities and preferences of the wireless devices