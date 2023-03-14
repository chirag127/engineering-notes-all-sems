### Basic internetworking in network layer

- Internetworking is the process of connecting different networks using intermediate devices such as routers or gateways.
- Internetworking enables communication across heterogeneous networks that use different technologies, protocols, or addressing schemes.
- Internetworking is implemented in the network layer of the OSI-ISO model, which is responsible for routing packets from source to destination across multiple networks.
- The most notable example of internetworking is the Internet, which is a global network of networks that uses the Internet Protocol (IP) as the common protocol for packet delivery.
- Internetworking can be classified into three types, depending on who administers and who participates in them: extranet, intranet, and internet.

  - Extranet: A network of networks that is restricted to a single organization or entity, but that also has limited connections to the networks of one or more other organizations or entities. For example, a company may have an extranet that connects its branches, suppliers, and customers.
  - Intranet: A network of networks that uses the Internet Protocol and IP-based tools such as web browsers and FTP, but that is under the control of a single administrative entity. For example, a university may have an intranet that connects its campuses, departments, and libraries.
  - Internet: A network of networks that is open to the public and that uses the Internet Protocol and IP-based tools as the standard for communication. For example, the World Wide Web is a service that runs on the Internet.

- Internetworking requires some mechanisms to enable packet forwarding, address translation, host configuration, error reporting, and virtual networks and tunnels. Some of these mechanisms are:

  - IP Forwarding: The process of moving a packet from one network to another based on the destination IP address. IP forwarding is performed by routers, which have routing tables that store the best paths to reach different networks.
  - Address Translation (ARP): The process of mapping a network layer address (such as an IP address) to a link layer address (such as a MAC address). Address translation is performed by the Address Resolution Protocol (ARP), which allows hosts and routers to discover the link layer addresses of other nodes on the same network.
  - Host Configuration (DHCP): The process of assigning network layer parameters (such as IP address, subnet mask, default gateway, etc.) to a host. Host configuration is performed by the Dynamic Host Configuration Protocol (DHCP), which allows hosts to request and obtain network configuration information from a server.
  - Error Reporting (ICMP): The process of sending and receiving diagnostic messages about the status of the network. Error reporting is performed by the Internet Control Message Protocol (ICMP), which allows hosts and routers to send and receive error messages, such as destination unreachable, time exceeded, echo request, and echo reply.
  - Virtual Networks and Tunnels: The process of creating a logical network that spans multiple physical networks. Virtual networks and tunnels are performed by various protocols, such as Virtual Private Network (VPN), which allows hosts to establish secure and encrypted connections over the Internet, or IP tunneling, which allows hosts to encapsulate and decapsulate IP packets within other IP packets.

- A simple mnemonic to remember the types of internetworking is EII: Extranet, Intranet, Internet. A simple mnemonic to remember the mechanisms of internetworking is FAHET: Forwarding, Address translation, Host configuration, Error reporting, Tunnels.