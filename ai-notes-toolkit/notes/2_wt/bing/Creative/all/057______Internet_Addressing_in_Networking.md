#### Internet Addressing in Networking

- Internet addressing is the process of assigning unique identifiers to devices and networks on the Internet.
- The most common form of Internet addressing is the Internet Protocol (IP) addressing, which uses numerical addresses to identify devices and networks.
- IP addresses are divided into two versions: IPv4 and IPv6. IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses.
- IPv4 addresses are written in dotted-decimal notation, such as 192.168.1.1, where each dot separates a byte (8 bits) of the address. IPv6 addresses are written in hexadecimal notation, such as 2001:db8::1, where each colon separates a 16-bit segment of the address.
- IP addresses are divided into two parts: network prefix and host identifier. The network prefix identifies the network to which the device belongs, while the host identifier identifies the device within the network.
- The length of the network prefix and the host identifier varies depending on the address class or the subnet mask. A subnet mask is a binary pattern that indicates which bits of the address belong to the network prefix and which bits belong to the host identifier.
- There are five classes of IPv4 addresses: A, B, C, D, and E. Each class has a different range of values for the first byte of the address and a different default subnet mask. Class A addresses have a first byte between 1 and 126 and a default subnet mask of 255.0.0.0. Class B addresses have a first byte between 128 and 191 and a default subnet mask of 255.255.0.0. Class C addresses have a first byte between 192 and 223 and a default subnet mask of 255.255.255.0. Class D addresses have a first byte between 224 and 239 and are used for multicast communication. Class E addresses have a first byte between 240 and 255 and are reserved for future use.
- IPv6 addresses are divided into two parts: global routing prefix and interface identifier. The global routing prefix identifies the network to which the device belongs, while the interface identifier identifies the device within the network.
- The length of the global routing prefix and the interface identifier is usually 64 bits each, but it can vary depending on the address type or the prefix length. A prefix length is a decimal number that indicates how many bits of the address belong to the global routing prefix and how many bits belong to the interface identifier.
- There are several types of IPv6 addresses, such as global unicast, link-local, site-local, multicast, anycast, and unique local. Each type has a different format and scope of use. Global unicast addresses are the most common type and are used for communication between devices on the Internet. Link-local addresses are used for communication between devices on the same local network. Site-local addresses are used for communication between devices on the same site or organization. Multicast addresses are used for sending data to multiple devices at once. Anycast addresses are used for sending data to the nearest device that shares the same address. Unique local addresses are used for private communication within a local network.

- A mnemonic to remember the ranges of the first byte of IPv4 address classes is:

  - A: **A**nything from 1 to 126
  - B: **B**etween 128 and 191
  - C: **C**lose to 200, from 192 to 223
  - D: **D**ouble 100, from 224 to 239
  - E: **E**nd of the line, from 240 to 255

- A learning trick to convert between dotted-decimal and binary notation of IPv4 addresses is:

  - To convert from dotted-decimal to binary, write each byte of the address in binary and separate them with dots. For example, 192.168.1.1 in binary is 11000000.10101000.00000001.00000001.
  - To convert from binary to dotted-decimal, write each group of 8 bits in decimal and separate them with dots. For example, 11000000.10101000.00000001.00000001 in decimal is 192.168.1.1.

- A learning trick to convert between hexadecimal and binary notation of IPv6 addresses is:

  - To convert from hexadecimal to binary, write each hexadecimal digit in binary and separate them with colons. For example, 2001:db8::1 in binary is 0010 0000 0000 0001:1101 1011 1000 0000:0000 0000 0000 000