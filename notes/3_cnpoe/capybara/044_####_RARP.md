#### RARP

RARP stands for Reverse Address Resolution Protocol. It is a protocol used to map a physical address to an IP address. In other words, RARP is used when a device wants to know its IP address, but only knows its physical address.

Here are some key points to remember about RARP:

- RARP is used in situations where a device does not have an IP address and wants to discover it.
- RARP is a simple protocol that requires a RARP server to be present on the network.
- RARP operates at the Data Link Layer of the OSI model.
- RARP requires a device's physical address (MAC address) to be registered with the RARP server before it can acquire an IP address.
- RARP sends broadcast messages to the network in order to discover the RARP server.
- RARP is not widely used anymore, as it has been largely replaced by DHCP (Dynamic Host Configuration Protocol).

Here are some advantages and disadvantages of RARP:

Advantages:
- RARP is a simple protocol that is easy to implement.
- RARP requires less overhead than DHCP, as it does not involve the negotiation of leases, etc.

Disadvantages:
- RARP requires a RARP server to be present on the network, which can be a single point of failure.
- RARP is not very scalable, as it requires each device on the network to be registered with the RARP server.

Here's an example of how RARP works:

1. A device without an IP address sends a broadcast message requesting its IP address.
2. The RARP server receives the message and looks up the device's physical address in its database.
3. The RARP server sends a unicast message back to the device with its IP address.
4. The device can now use its IP address to communicate on the network.

Some applications of RARP include bootstrapping diskless workstations and network appliances, such as routers and switches.

While RARP is not widely used anymore, it is still important to understand how it works and its advantages and disadvantages.