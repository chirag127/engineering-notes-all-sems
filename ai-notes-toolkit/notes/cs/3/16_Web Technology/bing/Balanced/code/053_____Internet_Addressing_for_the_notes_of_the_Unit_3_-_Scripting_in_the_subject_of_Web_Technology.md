### Internet Addressing

- Internet addressing is the process of assigning unique identifiers to devices and networks that communicate over the Internet.
- The most common internet addressing scheme is the Internet Protocol (IP), which defines a standard format and structure for IP addresses.
- IP addresses are 32-bit or 128-bit numbers that are divided into four or eight groups of bits, called octets or hextets, respectively.
- IP addresses are written in decimal notation for IPv4 (e.g., 192.168.1.1) or hexadecimal notation for IPv6 (e.g., 2001:db8::1).
- IP addresses consist of two parts: a network prefix and a host identifier. The network prefix identifies the network or subnetwork to which the device belongs, while the host identifier identifies the specific device within that network or subnetwork.
- The network prefix and the host identifier are separated by a slash (/) and a number that indicates the length of the network prefix in bits (e.g., 192.168.1.1/24 or 2001:db8::1/64).
- The network prefix can be further divided into subnetworks by using subnet masks, which are binary numbers that indicate which bits of the IP address belong to the network prefix and which belong to the host identifier.
- Subnet masks are also written in decimal or hexadecimal notation, and are usually aligned with the octet or hextet boundaries of the IP address (e.g., 255.255.255.0 or ffff:ffff:ffff:ffff::).
- Subnetting allows for more efficient use of IP address space and better control of network traffic and security.
- IP addresses can be classified into different types based on their functions and scopes. Some of the common types are:

  - Unicast addresses: These are addresses that identify a single device or interface on the Internet. They are used for one-to-one communication between devices.
  - Broadcast addresses: These are addresses that identify all devices or interfaces on a network or subnetwork. They are used for one-to-many communication between devices, such as sending announcements or requests.
  - Multicast addresses: These are addresses that identify a group of devices or interfaces on the Internet. They are used for many-to-many communication between devices, such as streaming media or conferencing.
  - Anycast addresses: These are addresses that identify multiple devices or interfaces on the Internet that provide the same service or function. They are used for one-to-nearest communication between devices, such as load balancing or redundancy.
  - Loopback addresses: These are addresses that identify the device itself. They are used for testing or troubleshooting purposes, such as checking the connectivity or configuration of the device.
  - Special-purpose addresses: These are addresses that have specific meanings or uses in the IP protocol, such as reserved addresses, private addresses, link-local addresses, or global addresses.