#### DHCP

- DHCP stands for Dynamic Host Configuration Protocol.
- It is a network management protocol used to dynamically assign IP addresses to devices on a network.
- DHCP operates on a client-server model, where a DHCP server assigns IP addresses to DHCP clients.
- The DHCP server maintains a pool of available IP addresses and assigns them to clients on a lease basis.
- When a client connects to the network, it sends a broadcast message requesting an IP address.
- The DHCP server receives the request and assigns an available IP address to the client.
- The server also provides the client with additional network configuration information, such as the subnet mask, default gateway, and DNS server addresses.
- The client uses the assigned IP address for a specified period of time, known as the lease time.
- When the lease time expires, the client must request a new IP address from the DHCP server.
- DHCP can simplify network management by automatically assigning IP addresses to devices, reducing the need for manual configuration.
- A mnemonic to remember the steps of the DHCP process is DORA: Discover, Offer, Request, Acknowledge.
- Discover: The client sends a broadcast message to discover available DHCP servers.
- Offer: The DHCP server sends an offer message to the client, offering an IP address and other network configuration information.
- Request: The client sends a request message to the server, requesting the offered IP address.
- Acknowledge: The server sends an acknowledgement message to the client, confirming the assignment of the IP address.