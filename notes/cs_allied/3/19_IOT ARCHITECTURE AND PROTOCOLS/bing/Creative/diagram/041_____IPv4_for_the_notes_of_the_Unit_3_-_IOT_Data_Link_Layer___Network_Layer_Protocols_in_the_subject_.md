Hello, I am Sydney, your AI assistant. I will help you with your query. Here are some notes on IPv4 for the unit 3 of IOT Architecture and Protocols:

### IPv4
- IPv4 stands for Internet Protocol version 4, which is the fourth version in the development of the Internet Protocol (IP) and the first version of the protocol to be widely deployed.
- IPv4 is a connectionless protocol that operates on the network layer of the OSI model and the internet layer of the TCP/IP model.
- IPv4 uses 32-bit binary numbers to create a single unique address on the network. An IPv4 address is expressed by four numbers separated by dots. Each number is the decimal (base-10) representation for an eight-digit binary (base-2) number, also called an octet.
- For example, an IPv4 address can be written as 192.168.0.1, which in binary is 11000000.10101000.00000000.00000001.
- IPv4 addresses are divided into two parts: network identifier and host identifier. The network identifier specifies the network to which the host belongs, and the host identifier specifies the host within the network.
- IPv4 addresses are classified into five classes: A, B, C, D, and E. Each class has a different range of network identifiers and host identifiers, and a different number of possible networks and hosts.
- Class A addresses have the first bit as 0, and the remaining 7 bits as the network identifier. The host identifier is the remaining 24 bits. Class A addresses can have 2^7 - 2 = 126 possible networks and 2^24 - 2 = 16,777,214 possible hosts per network.
- Class B addresses have the first two bits as 10, and the next 14 bits as the network identifier. The host identifier is the remaining 16 bits. Class B addresses can have 2^14 - 2 = 16,382 possible networks and 2^16 - 2 = 65,534 possible hosts per network.
- Class C addresses have the first three bits as 110, and the next 21 bits as the network identifier. The host identifier is the remaining 8 bits. Class C addresses can have 2^21 - 2 = 2,097,150 possible networks and 2^8 - 2 = 254 possible hosts per network.
- Class D addresses have the first four bits as 1110, and the remaining 28 bits as the multicast group address. Class D addresses are used for multicast communication, where a single source can send data to multiple destinations.
- Class E addresses have the first four bits as 1111, and the remaining 28 bits as reserved for future use or experimental purposes. Class E addresses are not used for public communication.
- IPv4 also supports some special types of addresses, such as loopback address, broadcast address, anycast address, and subnet address.
- IPv4 has a header of 20 bytes, which contains 12 fields: version, header length, type of service, total length, identification, flags, fragment offset, time to live, protocol, header checksum, source address, and destination address.
- IPv4 has some limitations, such as the exhaustion of address space, lack of security, and fragmentation.
- IPv4 is gradually being replaced by IPv6, which is the next generation of the Internet Protocol that uses 128-bit addresses and has many advantages over IPv4.