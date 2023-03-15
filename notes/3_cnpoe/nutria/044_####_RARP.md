
#### RARP

RARP (Reverse Address Resolution Protocol) is a protocol used to map a MAC address to an IP address. It is used by computers to determine their own IP address when they are connected to a network.

RARP works by sending a broadcast request to the network, asking for the IP address associated with the computer's MAC address. The computer's MAC address is sent in the request, and the server responds with the IP address associated with the MAC address.

Mnemonics and Learning Tricks:

1. RARP stands for Reverse Address Resolution Protocol.
2. RARP is used to map a MAC address to an IP address.
3. RARP sends a broadcast request to the network, asking for the IP address associated with the computer's MAC address.

Advantages:

1. RARP is a simple protocol and easy to implement.
2. It is a fast way to determine an IP address.
3. It is a reliable protocol, as it ensures that the IP address is mapped correctly to the MAC address.

Disadvantages:

1. RARP is not suitable for large networks as it does not scale well.
2. The broadcast request is sent over the network, which can cause network congestion.
3. RARP does not provide any security, as the MAC address is sent in plain text.

Examples:

RARP is commonly used in LANs (Local Area Networks) to map the IP address of each computer in the network. It is also used in booting diskless workstations, as the computer needs to know its own IP address before it can access the network resources.

Applications:

RARP is used in networks to map the IP address of each computer in the network. It is also used in booting diskless workstations, as the computer needs to know its own IP address before it can access the network resources. Additionally, it can be used to determine the IP address of a computer on a network without having to manually configure the IP address.