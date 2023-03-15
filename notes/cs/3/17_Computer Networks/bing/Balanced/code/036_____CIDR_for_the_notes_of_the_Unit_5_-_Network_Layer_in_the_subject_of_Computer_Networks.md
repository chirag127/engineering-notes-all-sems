# CIDR for the notes of the Unit 5 - Network Layer in the subject of Computer Networks

- CIDR stands for Classless Inter-Domain Routing .
- It is a method for assigning IP addresses and for IP routing.
- It does not use the standard IP address classes like Class A, B or C.
- It is based on variable-length subnet masking (VLSM), which allows for different sizes of subnets.
- It improves the efficiency of address distribution and reduces the size of routing tables .
- It uses a notation of the form x.y.z.w/n, where x.y.z.w is the IP address and n is the number of bits in the network prefix .
- The network prefix identifies the network and the host prefix identifies the host within the network.
- The network prefix can be any length from 1 to 32 bits.
- The larger the network prefix, the smaller the host prefix and the number of hosts in the network.
- The smaller the network prefix, the larger the host prefix and the number of hosts in the network.
- For example, 192.168.1.0/24 is a CIDR notation for a network with 24 bits in the network prefix and 8 bits in the host prefix.
- This network can have up to 2^8 - 2 = 254 hosts (excluding the network and broadcast addresses).
- Another example, 10.0.0.0/8 is a CIDR notation for a network with 8 bits in the network prefix and 24 bits in the host prefix.
- This network can have up to 2^24 - 2 = 16,777,214 hosts (excluding the network and broadcast addresses).