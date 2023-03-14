#### RARP
- RARP stands for Reverse Address Resolution Protocol, which is a protocol based on computer networking that is used by a client computer to request its IP address from a gateway server's Address Resolution Protocol table or cache.
- RARP works by sending the device's physical address (or MAC address) to a specialized RARP server that is on the same local area network (LAN) and is actively listening for RARP requests.
- The RARP server has a table that maps the MAC addresses to corresponding IP addresses, which is created by the network administrator.
- The RARP server responds to the RARP request by sending back the IP address assigned to the device's MAC address, if it is found in the table.
- RARP is different from ARP, which is used to find the MAC address of a remote device given its IP address. RARP uses the value 3 for requests and 4 for responses, while ARP uses the value 1 for requests and 2 for responses.
- RARP was historically used on Ethernet, FDDI and token ring LANs, especially for diskless workstations that did not have a permanent storage for their IP addresses .
- RARP is now obsolete and has been replaced by more advanced protocols such as Bootstrap Protocol (BOOTP) and Dynamic Host Configuration Protocol (DHCP), which offer more features and can scale better on modern LANs that contain multiple IP subnets.