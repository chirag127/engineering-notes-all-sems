CIDR stands for Classless Inter-Domain Routing. It is a method for allocating IP addresses and for IP routing that replaces the previous classful network addressing architecture on the Internet. CIDR allows blocks of addresses to be grouped into single routing table entries, reducing the size and complexity of routing tables and slowing down the exhaustion of IPv4 addresses.

CIDR notation is a way of writing IP addresses that indicates the network prefix and the host identifier. The network prefix is the number of bits that are common to all the addresses in the network. The host identifier is the number of bits that are unique to each address in the network. CIDR notation uses a slash (/) to separate the IP address from the network prefix length. For example, 192.168.1.0/24 means that the network prefix is 24 bits long, and the host identifier is 8 bits long. The network prefix is 192.168.1, and the host identifier can range from 0 to 255.

CIDR blocks are ranges of IP addresses that share the same network prefix. They are also called subnets or supernets, depending on their size. CIDR blocks are represented by the lowest and highest IP address in the range, or by the network prefix and the prefix length. For example, 192.168.1.0/24 is a CIDR block that contains 256 IP addresses, from 192.168.1.0 to 192.168.1.255. The following table shows some common CIDR blocks and their equivalent number of addresses and network masks.

#### CIDR

| CIDR block | Number of addresses | Network mask |
|------------|---------------------|--------------|
| /32        | 1                   | 255.255.255.255 |
| /31        | 2                   | 255.255.255.254 |
| /30        | 4                   | 255.255.255.252 |
| /29        | 8                   | 255.255.255.248 |
| /28        | 16                  | 255.255.255.240 |
| /27        | 32                  | 255.255.255.224 |
| /26        | 64                  | 255.255.255.192 |
| /25        | 128                 | 255.255.255.128 |
| /24        | 256                 | 255.255.255.0   |
| /23        | 512                 | 255.255.254.0   |
| /22        | 1024                | 255.255.252.0   |
| /21        | 2048                | 255.255.248.0   |
| /20        | 4096                | 255.255.240.0   |
| /19        | 8192                | 255.255.224.0   |
| /18        | 16384               | 255.255.192.0   |
| /17        | 32768               | 255.255.128.0   |
| /16        | 65536               | 255.255.0.0     |
| /15        | 131072              | 255.254.0.0     |
| /14        | 262144              | 255.252.0.0     |
| /13        | 524288              | 255.248.0.0     |
| /12        | 1048576             | 255.240.0.0     |
| /11        | 2097152             | 255.224.0.0     |
| /10        | 4194304             | 255.192.0.0     |
| /9         | 8388608             | 255.128.0.0     |
| /8         | 16777216            | 255.0.0.0       |
| /7         | 33554432            | 254.0.0.0       |
| /6         | 67108864            | 252.0.0.0       |
| /5         | 134217728           | 248.0.0.0       |
| /4         | 268435456           | 240.0.0.0       |
| /3         | 536870912           | 224.0.0.0       |
| /2         | 107374182