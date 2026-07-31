### RARP

- RARP stands for Reverse Address Resolution Protocol.
- It is a protocol used by a client computer to request its IP address from a gateway server's ARP table or cache .
- It is based on the Network Access Layer of the TCP/IP protocol stack.
- It is used to send data between two points in a network.
- It works by sending the device's physical address (MAC address) to a specialized RARP server that is on the same LAN and is actively listening for RARP requests.
- The RARP server then looks up the MAC address in its ARP table and sends back the corresponding IP address to the client.
- RARP is useful for devices that do not have a permanent IP address, such as diskless workstations or bootstrapping devices .
- RARP is an obsolete protocol that has been replaced by other protocols such as BOOTP and DHCP .
- RARP uses the same packet format as ARP, but with different operation codes.
- RARP packets are encapsulated in Ethernet frames and broadcasted to all devices on the LAN .

: https://www.geeksforgeeks.org/what-is-rarp/
: https://www.techtarget.com/searchnetworking/definition/Reverse-Address-Resolution-Protocol
: https://www.ionos.com/digitalguide/server/know-how/reverse-arp/