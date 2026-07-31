# DHCP

- DHCP stands for Dynamic Host Configuration Protocol .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations.
- It supports both static and dynamic IP address allocation, where static allocation assigns a fixed IP address to a client, and dynamic allocation assigns an IP address from a pool of available addresses for a limited period of time .
- It operates on the application layer of the TCP/IP model, and uses UDP port 67 for server and UDP port 68 for client communication .
- It consists of four basic steps: discover, offer, request, and acknowledge (DORA), where a client broadcasts a discover message to find a DHCP server, a server responds with an offer message containing an IP address and other parameters, a client chooses an offer and sends a request message to the server, and the server confirms the allocation with an acknowledge message .
- It can also provide additional information to clients, such as the domain name, DNS server, time server, and vendor-specific options, using DHCP options .
- It is widely used in local area networks (LANs) and wireless networks to simplify IP address management and avoid IP address conflicts .