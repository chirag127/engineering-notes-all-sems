# DHCP

- DHCP stands for Dynamic Host Configuration Protocol  .
- It is a network management protocol that automatically provides an Internet Protocol (IP) host with its IP address and other related configuration information such as the subnet mask and default gateway .
- It uses a client-server architecture, where a DHCP server allocates IP addresses and other parameters to DHCP clients that request them  .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless systems to obtain configuration information from a network server .
- It is defined by RFCs 2131 and 2132, and is an Internet Engineering Task Force (IETF) standard.
- It operates on the application layer of the TCP/IP model, and uses UDP port 67 for server and UDP port 68 for client communication .
- It supports four types of messages: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK .
- It follows a four-step process to assign an IP address to a client: discover, offer, request, and acknowledge .
- It can assign IP addresses in three ways: manual, automatic, and dynamic .
- It can also provide other options, such as DNS servers, NTP servers, domain name, etc. to the clients .
- It can be used for various purposes, such as simplifying network administration, reducing configuration errors, supporting mobile users, etc. .