### RARP

RARP stands for Reverse Address Resolution Protocol. It is a network protocol that allows a host computer to obtain its IP address from a gateway server's ARP table or cache. RARP is used when the host computer does not have a permanent IP address assigned to it, such as in diskless workstations or bootstrapping devices. RARP operates on the network access layer of the TCP/IP protocol stack, and uses the same packet format as ARP. RARP works as follows:

- The host computer broadcasts a RARP request packet containing its MAC address to the network.
- The gateway server that has the RARP table receives the request and looks up the IP address that corresponds to the MAC address of the host computer.
- The gateway server sends a RARP reply packet containing the IP address of the host computer to the network.
- The host computer receives the RARP reply and configures its IP address accordingly.

Some of the advantages and disadvantages of RARP are:

- RARP is simple and easy to implement, as it does not require any configuration on the host computer.
- RARP reduces the administrative overhead of assigning and managing IP addresses for network devices.
- RARP is limited to local area networks, as it relies on broadcast messages that cannot cross routers or subnets.
- RARP is obsolete and has been replaced by more advanced protocols such as BOOTP and DHCP, which offer more features and flexibility.