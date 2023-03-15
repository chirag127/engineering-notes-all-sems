#### Internet Addressing in Networking

- Internet addressing refers to the process of assigning unique IP addresses to devices connected to the internet.
- IP addresses are used to identify devices on the internet and to route data between them.
- There are two versions of IP addresses in use: IPv4 and IPv6.
- IPv4 addresses are 32-bit numbers, written in dotted-decimal notation, for example, 192.168.1.1.
- IPv6 addresses are 128-bit numbers, written in hexadecimal notation, for example, 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
- The IPv4 address space is limited and has mostly been exhausted, while the IPv6 address space is much larger and is expected to last for the foreseeable future.
- IP addresses can be assigned statically or dynamically.
- Static IP addresses are manually assigned to a device and do not change.
- Dynamic IP addresses are assigned by a DHCP server and can change over time.
- IP addresses can be public or private.
- Public IP addresses are globally unique and can be reached from anywhere on the internet.
- Private IP addresses are used within a local network and are not reachable from the internet.
- Network Address Translation (NAT) is used to map private IP addresses to public IP addresses, allowing devices with private IP addresses to communicate with the internet.
- Subnetting is the process of dividing an IP address space into smaller subnets, allowing for more efficient use of IP addresses.
- A subnet mask is used to determine which part of an IP address represents the network and which part represents the host.
- CIDR notation is used to represent IP addresses and their associated subnet masks, for example, 192.168.1.0/24.

Mnemonic for remembering private IP address ranges:
- **C**lass **A**: 10.0.0.0 to 10.255.255.255 (10/8 prefix)
- **C**lass **B**: 172.16.0.0 to 172.31.255.255 (172.16/12 prefix)
- **C**lass **C**: 192.168.0.0 to 192.168.255.255 (192.168/16 prefix)

Remember **ABC** for the classes and the starting numbers of each range (10, 172, 192).