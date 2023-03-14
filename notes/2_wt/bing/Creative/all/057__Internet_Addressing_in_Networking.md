#### Internet Addressing in Networking

- Internet addressing is the process of assigning unique identifiers to devices that communicate over the internet using the TCP/IP protocol suite.
- An internet address, also known as an IP address, works like a postal address, allowing data to be routed to the chosen destination .
- An IP address is a 32-bit binary number, usually written in decimal notation, with four numbers separated by dots, such as 192.168.1.34.
- Each number in an IP address can range from 0 to 255, which corresponds to the possible values of an 8-bit binary number, or an octet.
- An IP address consists of two parts: a network ID and a host ID  .
- The network ID identifies the specific network on which the device is located, while the host ID identifies the specific device on the network  .
- The network ID and the host ID are separated by a subnet mask, which is another 32-bit binary number that indicates which bits of the IP address belong to the network ID and which bits belong to the host ID.
- For example, the IP address 192.168.1.34 with a subnet mask of 255.255.255.0 means that the first 24 bits (or three octets) of the IP address are the network ID (192.168.1) and the last 8 bits (or one octet) are the host ID (34).
- The subnet mask can also be written in slash notation, where the number after the slash indicates the number of bits in the network ID. For example, 192.168.1.34/24 is equivalent to 192.168.1.34 with a subnet mask of 255.255.255.0.
- There are two versions of IP addresses: IPv4 and IPv6. IPv4 is the most widely used version, but it has a limited address space of about 4.3 billion possible addresses. IPv6 is the newer version, which has a much larger address space of about 340 undecillion possible addresses. IPv6 addresses are 128-bit binary numbers, usually written in hexadecimal notation, with eight groups of four digits separated by colons, such as 2001:db8:abcd:1234:5678:90ab:cdef:1234.
- Some IP addresses have special meanings or purposes, such as loopback addresses, broadcast addresses, multicast addresses, and anycast addresses.
- A loopback address is an IP address that refers to the device itself, rather than a remote device. The loopback address for IPv4 is 127.0.0.1, and the loopback address for IPv6 is ::1.
- A broadcast address is an IP address that sends a message to all devices on the same network. The broadcast address for IPv4 is the IP address with all bits in the host ID set to 1, such as 192.168.1.255 for the network 192.168.1.0/24. The broadcast address for IPv6 is ff02::1, which sends a message to all devices on the same link.
- A multicast address is an IP address that sends a message to a group of devices that have joined a multicast group. Multicast addresses for IPv4 start with 224 to 239, and multicast addresses for IPv6 start with ff00::/8.
- An anycast address is an IP address that sends a message to the nearest device that has the same anycast address. Anycast addresses are usually used for load balancing and redundancy. Anycast addresses for IPv4 and IPv6 are indistinguishable from unicast addresses, which are the normal IP addresses that send a message to a single device.

Some mnemonics and learning tricks for internet addressing in networking are:

- To remember the range of each number in an IP address, think of the acronym BANANA, which stands for Binary And Numbers Are Not Alphabetical. This reminds you that each number is a binary number, and that the highest number you can write with 8 bits is 255, not 256 or higher.
- To remember the difference between network ID and host ID, think of the analogy of a street address. The network ID is like the street name, which identifies