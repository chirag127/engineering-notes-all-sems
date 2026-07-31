# DHCP

- DHCP stands for Dynamic Host Configuration Protocol .
- It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to an IP network using a client-server architecture .
- It is based on the Bootstrap Protocol (BOOTP), which was designed for diskless workstations .
- It reduces the manual configuration and administration of IP networks, and avoids IP address conflicts and duplication  .
- It operates on four basic messages: DHCPDISCOVER, DHCPOFFER, DHCPREQUEST, and DHCPACK .
- A device that needs an IP address sends a DHCPDISCOVER message to the network, which is received by one or more DHCP servers .
- Each DHCP server that receives the DHCPDISCOVER message responds with a DHCPOFFER message, which contains an IP address and other configuration information for the device .
- The device chooses one of the DHCPOFFER messages and sends a DHCPREQUEST message to the selected DHCP server, requesting the offered IP address and other parameters .
- The DHCP server sends a DHCPACK message to the device, confirming the IP address and other parameters, and updates its database of allocated IP addresses .
- The device configures its network interface with the IP address and other parameters, and can communicate with other devices on the network .
- The IP address assigned by the DHCP server is usually temporary, and has a lease time that specifies how long the device can use it .
- The device can renew the lease before it expires, or request a new IP address if the lease expires or the device moves to a different network .
- The DHCP server can also reclaim the IP address if the device does not renew the lease or goes offline .
- The DHCP server can also provide other information to the device, such as the subnet mask, default gateway, domain name, DNS servers, and other options  .
- The DHCP protocol is defined by RFCs 2131 and 2132, and has been extended by several other RFCs to support new features and options .