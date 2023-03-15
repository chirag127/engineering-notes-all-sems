### Basic internetworking in network layer

- Internetworking is the process of connecting different networks using routers and other devices to form a larger network that can exchange data across different protocols and technologies.
- Internetworking is implemented in the network layer (layer 3) of the OSI model, which is responsible for routing, addressing, and fragmentation of packets across multiple networks.
- The most common example of internetworking is the Internet, which is a global network of networks that uses the Internet Protocol (IP) to communicate.
- There are three main types of internetworking:
  - Internet: A public network that connects millions of networks and devices worldwide using IP and other protocols.
  - Intranet: A private network that connects networks and devices within an organization using IP and other protocols. An intranet may or may not have access to the Internet.
  - Extranet: A private network that connects networks and devices from different organizations using IP and other protocols. An extranet may or may not have access to the Internet.
- Internetworking involves the following components and concepts:
  - Routers: Devices that forward packets between networks based on their destination addresses. Routers operate at the network layer and use routing tables and algorithms to determine the best path for each packet.
  - Data-link layer addresses: Addresses that uniquely identify each physical network interface of a device. Data-link layer addresses are also known as MAC addresses or hardware addresses. They are usually assigned by the manufacturer and are fixed for each device.
  - Network layer addresses: Addresses that uniquely identify each logical network interface of a device. Network layer addresses are also known as IP addresses or logical addresses. They are usually assigned by the network administrator or a DHCP server and can be changed for each device.
  - Address resolution: The process of mapping network layer addresses to data-link layer addresses. Address resolution is performed by protocols such as ARP (Address Resolution Protocol) or NDP (Neighbor Discovery Protocol).
  - Packet fragmentation: The process of breaking a large packet into smaller packets that can fit the maximum transmission unit (MTU) of the underlying network. Packet fragmentation is performed by the sender and the intermediate routers and is reassembled by the receiver.
  - Packet reassembly: The process of combining the fragments of a packet into the original packet. Packet reassembly is performed by the receiver and requires the fragments to have identification and sequence numbers.
  - Packet delivery: The process of sending and receiving packets across an internetwork. Packet delivery can be either connectionless or connection-oriented. Connectionless packet delivery does not require any prior agreement or acknowledgment between the sender and the receiver, such as IP. Connection-oriented packet delivery requires a prior agreement and acknowledgment between the sender and the receiver, such as TCP.