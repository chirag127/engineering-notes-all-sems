#### DHCP
```
DHCP (Dynamic Host Configuration Protocol) is a protocol used to automatically assign IP addresses to devices on a network.

Here is an ASCII diagram of the DHCP process:

Client                            DHCP Server
   |                                   |
   |-------DHCPDISCOVER-------------->|
   |                                   |
   |<------DHCPOFFER------------------|
   |                                   |
   |-------DHCPREQUEST--------------->|
   |                                   |
   |<------DHCPACK--------------------|
   |                                   |
   |-------DHCPINFORM---------------->|
   |                                   |
   |<------DHCPACK--------------------|
   |                                   |
```
The DHCP process involves the following steps:
1. The client sends a broadcast message (DHCPDISCOVER) to discover available DHCP servers.
2. The DHCP server responds with a message (DHCPOFFER) containing an IP address offer.
3. The client sends a message (DHCPREQUEST) to request the offered IP address.
4. The DHCP server sends a message (DHCPACK) to acknowledge the request and assign the IP address to the client.
5. The client sends a message (DHCPINFORM) to request additional configuration information.
6. The DHCP server sends a message (DHCPACK) to acknowledge the request and provide the requested information.
