### DHCP

- DHCP stands for Dynamic Host Configuration Protocol  .
- It is a network management protocol that automatically provides an Internet Protocol (IP) address and other related configuration information to devices connected to a network using a client–server architecture .
- The configuration information includes the subnet mask, default gateway, and DNS server information .
- DHCP is based on the Bootstrap Protocol (BOOTP), which is an older protocol for assigning IP addresses to devices.
- DHCP uses four basic messages to communicate between the client and the server: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK.
- The DHCP client broadcasts a DHCPDISCOVER message to find a DHCP server on the network.
- The DHCP server responds with a DHCPOFFER message that contains an IP address and other configuration information for the client.
- The DHCP client chooses one of the DHCPOFFER messages and sends a DHCPREQUEST message to the server to request the offered IP address.
- The DHCP server confirms the IP address assignment by sending a DHCPACK message to the client.
- The DHCP client can use the IP address and configuration information until the lease time expires or is renewed.
- DHCP has many benefits, such as reducing manual configuration errors, saving network administration time, and allowing efficient use of IP address space  .