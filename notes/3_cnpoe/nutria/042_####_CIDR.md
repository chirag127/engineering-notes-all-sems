
#### CIDR
- CIDR stands for **Classless Inter-Domain Routing**. It is a method of allocating IP addresses and routing Internet Protocol packets.
- CIDR notation is a compact representation of an IP address and its associated routing prefix. It is written in the form `<IP address>/<prefix length>`, where the prefix length is the number of leading bits of the address that make up the routing prefix.
- CIDR was introduced as a way to more efficiently use the limited number of IP addresses available in IPv4. It also allows for more flexible routing aggregation, which can reduce the size of routing tables.
- CIDR is used in conjunction with network address translation (NAT) to conserve public IP addresses and reduce the number of public IP addresses needed.
- CIDR is also used for VLSM (Variable Length Subnet Masking), which allows for more efficient use of IP address space by allowing for more granular subnets.
- A common mnemonic for remembering CIDR notation is "slash and number": the slash indicates the number of bits used for the routing prefix.