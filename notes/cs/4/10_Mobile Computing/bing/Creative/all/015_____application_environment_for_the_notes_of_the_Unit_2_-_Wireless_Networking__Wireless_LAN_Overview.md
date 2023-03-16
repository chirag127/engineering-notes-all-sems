# Application Environment for Wireless Networking

- An application environment is a set of protocols, standards, and tools that enable wireless devices to communicate with web servers and access internet-based services.
- One example of an application environment for wireless networking is the Wireless Application Environment (WAE), which is part of the Wireless Application Protocol (WAP) framework.
- WAE is based on the World Wide Web (WWW) model, but adapts it to the constraints and requirements of wireless devices, such as limited bandwidth, memory, processing power, and user interface.
- WAE consists of the following components :
  - Wireless Markup Language (WML): A markup language similar to HTML, but optimized for small screens and low bandwidth. WML defines the structure and content of web pages for wireless devices.
  - Wireless Markup Language Script (WMLScript): A scripting language similar to JavaScript, but with a smaller footprint and less functionality. WMLScript enables dynamic and interactive web pages for wireless devices.
  - Wireless Telephony Application Interface (WTAI): A set of extensions to WML and WMLScript that allow wireless devices to access telephony services, such as making and receiving calls, sending and receiving messages, and accessing phonebook entries.
  - Wireless Datagram Protocol (WDP): A transport layer protocol that provides a common interface for different wireless network technologies, such as GSM, CDMA, and GPRS. WDP enables WAE applications to be independent of the underlying network.
  - Wireless Session Protocol (WSP): A session layer protocol that provides reliable and secure communication between wireless devices and web servers. WSP supports features such as connection-oriented and connectionless modes, caching, and content encoding.
  - Wireless Transaction Protocol (WTP): A transaction layer protocol that provides efficient and reliable data exchange between wireless devices and web servers. WTP supports features such as segmentation and reassembly, acknowledgements, and retransmissions.
  - Wireless Application Protocol Binary XML (WBXML): A binary representation of XML documents that reduces the size and complexity of data transmission. WBXML is used to encode WML, WMLScript, and WTAI documents for wireless devices.

# Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- A wireless LAN (WLAN) is a local area network that uses wireless communication to connect devices within a limited geographic area, such as a home, office, or campus.
- A WLAN typically consists of the following components:
  - Wireless stations: Devices that have wireless network adapters, such as laptops, smartphones, tablets, and printers.
  - Access points: Devices that act as bridges between wireless stations and wired networks, such as routers, switches, and gateways.
  - Distribution system: The wired network that connects access points and provides access to other networks, such as the internet.
- A WLAN operates in one of the following modes:
  - Infrastructure mode: Wireless stations communicate with each other and with the wired network through access points. This mode provides more coverage, security, and scalability than ad hoc mode.
  - Ad hoc mode: Wireless stations communicate with each other directly without using access points. This mode is suitable for temporary or spontaneous networks, such as peer-to-peer file sharing or gaming.
- A WLAN faces several challenges at the medium access control (MAC) layer, which is responsible for coordinating the access of multiple devices to a shared wireless medium, such as radio frequency (RF) spectrum. Some of these challenges are:
  - Hidden terminal problem: A situation where two wireless stations are within the range of an access point, but not within the range of each other. This may cause collisions and interference when both stations transmit at the same time.
  - Exposed terminal problem: A situation where two wireless stations are within the range of each other, but not within the range of the intended receiver. This may cause unnecessary waiting and inefficiency when one station defers its transmission to avoid colliding with the other station's transmission.
  - Fading and multipath propagation: The phenomenon where the wireless signal strength varies due to obstacles, reflections, and interference. This may cause errors and losses in data transmission.
  - Mobility and handoff: The phenomenon where wireless stations move from one access point to another. This may cause interruptions and delays in data transmission.
- IEEE 802.11 is a family of standards that define the physical and MAC layers of WLANs. The most common variants of IEEE 802.11 are:
  - IEEE 802.11a: Operates in the 5 GHz