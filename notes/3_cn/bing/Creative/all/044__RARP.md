#### RARP

RARP stands for Reverse Address Resolution Protocol, which is a protocol based on computer networking that is used by a client computer to request its IP address from a gateway server's Address Resolution Protocol (ARP) table or cache . The network administrator creates a table in the gateway-router, which is used to map the MAC address to the corresponding IP address. This protocol is used to communicate data between two points in a network. The client does not necessarily need prior knowledge of the server identities capable of serving its request.

RARP was proposed in 1984 by the University Network Group and was included in the TCP/IP protocol stack . It was mainly used for diskless workstations that did not have a permanent storage to store their IP address . These workstations were also the platform for the first workstations from Sun Microsystems.

The working of RARP is as follows  :

- The RARP client program sends its physical MAC address to the RARP server on the router using an Ethernet broadcast address.
- The RARP server, which has a table of MAC addresses and IP addresses, looks up the IP address that matches the MAC address of the client and sends it back to the client.
- The RARP client program receives the IP address and configures its network interface with it.

The RARP uses the value 3 for requests and 4 for responses. It is available for the LAN technologies like Ethernet, FDDI, token ring LANs, etc .

RARP has some disadvantages that led to its replacement by BOOTP and DHCP . Some of them are:

- RARP requires a RARP server on the same LAN as the client, which limits its scalability and flexibility .
- RARP only provides the IP address to the client, not other configuration parameters like subnet mask, default gateway, DNS server, etc .
- RARP is not secure, as anyone can spoof the MAC address and get the IP address of another device.

Some mnemonics and learning tricks for RARP are:

- RARP is the reverse of ARP, which means it finds the IP address from the MAC address, not the other way around.
- RARP is used for diskless workstations, which means they do not have a disk to store their IP address .
- RARP uses the values 3 and 4, which are the next numbers after 1 and 2, which are used by ARP.