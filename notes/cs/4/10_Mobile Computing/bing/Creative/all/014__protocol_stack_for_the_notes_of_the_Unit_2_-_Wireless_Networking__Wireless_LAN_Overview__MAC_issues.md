### Protocol stack for the notes of the Unit 2 - Wireless Networking, Wireless LAN Overview: MAC issues, IEEE 802.11, Blue Tooth, Wireless

- A protocol stack is a set of rules or agreed-upon guidelines for communication between different devices or layers in a network. 
- A protocol stack usually consists of several layers, each with a specific function or purpose. 
- A protocol stack can be implemented in software, hardware, or a combination of both. 
- A protocol stack can be specific to a certain network technology, such as wireless networking, or general to a network architecture, such as TCP/IP.  
- A protocol stack can be divided into three major sections: media, transport, and applications. 
- The media layer defines how the data is transmitted and received over the physical medium, such as radio waves, cables, or optical fibers. 
- The transport layer defines how the data is organized, segmented, and delivered reliably and efficiently over the network. 
- The application layer defines how the data is formatted, interpreted, and presented to the user or the application. 
- Some examples of wireless networking protocols are:

  - IEEE 802.11: A family of standards for wireless local area networks (WLANs) that operate in the 2.4 GHz or 5 GHz frequency bands. 
  - IEEE 802.11ax (Wi-Fi 6): The latest version of IEEE 802.11 that supports higher data rates, lower latency, and more devices per network. 
  - IEEE 802.11ac (Wi-Fi 5): A previous version of IEEE 802.11 that supports dual-band operation, multiple-input multiple-output (MIMO) technology, and beamforming. 
  - IEEE 802.11n (Wi-Fi 4): A previous version of IEEE 802.11 that supports MIMO technology and wider channels. 
  - IEEE 802.11g: A previous version of IEEE 802.11 that operates in the 2.4 GHz band and is backward compatible with IEEE 802.11b. 
  - IEEE 802.11a: A previous version of IEEE 802.11 that operates in the 5 GHz band and offers higher data rates than IEEE 802.11b. 
  - IEEE 802.11b: The first widely adopted version of IEEE 802.11 that operates in the 2.4 GHz band and offers data rates up to 11 Mbps. 
  - Bluetooth: A short-range wireless technology that connects devices using radio waves in the 2.4 GHz band. 
  - Bluetooth Low Energy (BLE): A variant of Bluetooth that consumes less power and is designed for Internet of Things (IoT) applications. 
  - Wireless Application Protocol (WAP): A protocol suite that enables wireless devices to access web content and services. 

- A protocol stack for wireless networking can vary depending on the network type, topology, and application. However, a general protocol stack for wireless networking can be illustrated as follows:

```
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Application    |  Application    |  Application    |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Transport      |  Transport      |  Transport      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Network        |  Network        |  Network        |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Data Link      |  Data Link      |  Data Link      |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Physical       |  Physical       |  Physical       |
|                 |                 |                 |
+-----------------+-----------------+-----------------+
|                 |                 |                 |
|  Wireless       |  Wireless       |  Wireless       |
|  Medium         |  Medium         |  Medium         |
|                 |                 |                 |
+-----------------+-----------------+