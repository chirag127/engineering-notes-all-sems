DHCP stands for Dynamic Host Configuration Protocol. It is a network management protocol that automatically assigns IP addresses and other communication parameters to devices connected to the network using a client–server architecture . DHCP enables information transfer between network nodes without manual configuration.

#### DHCP

The following diagram shows the basic steps of DHCP operation:

```
+--------+    +--------+    +--------+
| Client |    | Server |    | Router |
+--------+    +--------+    +--------+
     |             |             |
     | DHCPDISCOVER|             |
     |------------>|             |
     |             |             |
     |             | DHCPDISCOVER|
     |             |------------>|
     |             |             |
     |             | DHCPOFFER   |
     |             |<------------|
     | DHCPOFFER   |             |
     |<------------|             |
     |             |             |
     | DHCPREQUEST |             |
     |------------>|             |
     |             |             |
     |             | DHCPREQUEST |
     |             |------------>|
     |             |             |
     |             | DHCPACK     |
     |             |<------------|
     | DHCPACK     |             |
     |<------------|             |
     |             |             |
```

The steps are as follows:

1. The client broadcasts a DHCPDISCOVER message to the network, looking for a DHCP server.
2. The server receives the DHCPDISCOVER message and responds with a DHCPOFFER message, containing an IP address and other configuration information for the client.
3. The server also forwards the DHCPOFFER message to the router, which acts as a relay agent for the DHCP messages.
4. The client receives the DHCPOFFER message from the server and sends a DHCPREQUEST message to the server, requesting the offered IP address and other parameters.
5. The client also broadcasts the DHCPREQUEST message to the network, informing other DHCP servers that it has accepted an offer.
6. The server receives the DHCPREQUEST message from the client and sends a DHCPACK message to the client, confirming the IP address and other parameters.
7. The server also sends the DHCPACK message to the router, which relays it to the client.
8. The client receives the DHCPACK message from the server and completes the IP configuration process. The client can now communicate with other devices on the network using the assigned IP address.