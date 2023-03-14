#### CIDR
- CIDR stands for Classless Inter-Domain Routing, a method for allocating IP addresses and for IP routing.
- CIDR was introduced in 1993 to replace the previous classful network addressing architecture on the Internet, which had five classes of IP addresses (A, B, C, D, and E) with fixed network prefixes and host identifiers.
- CIDR allows for variable-length subnet masking (VLSM), in which network prefixes have variable length, depending on the size and number of subnets needed by an organization. This allows for more efficient use of the IP address space and reduces the size of routing tables on routers across the Internet.
- CIDR notation is a way of writing IP addresses with a suffix indicating the number of bits of the network prefix. For example, 192.168.1.0/24 means that the network prefix is 24 bits long, and the host identifier is 8 bits long. The network prefix can be any number of bits between 1 and 32 for IPv4, and between 1 and 128 for IPv6.
- CIDR blocks are groups of IP addresses that share the same network prefix. For example, 192.168.0.0/16 is a CIDR block that contains 65,536 IP addresses, from 192.168.0.0 to 192.168.255.255. CIDR blocks can be aggregated or subdivided as needed, as long as the network prefix remains contiguous. For example, 192.168.0.0/16 can be subdivided into four CIDR blocks of /18, or aggregated into one CIDR block of /14.
- CIDR table is a table that shows the number of IP addresses, subnets, and hosts for each network prefix length. For example, the following table shows the CIDR table for IPv4:

| Network prefix length | Number of IP addresses | Number of subnets | Number of hosts per subnet |
|-----------------------|------------------------|-------------------|----------------------------|
| /1                    | 2,147,483,648          | 2                 | 1,073,741,823              |
| /2                    | 1,073,741,824          | 4                 | 268,435,455                |
| /3                    | 536,870,912            | 8                 | 134,217,727                |
| /4                    | 268,435,456            | 16                | 67,108,863                 |
| /5                    | 134,217,728            | 32                | 33,554,431                 |
| /6                    | 67,108,864             | 64                | 16,777,215                 |
| /7                    | 33,554,432             | 128               | 8,388,607                  |
| /8                    | 16,777,216             | 256               | 4,194,303                  |
| /9                    | 8,388,608              | 512               | 2,097,151                  |
| /10                   | 4,194,304              | 1,024             | 1,048,575                  |
| /11                   | 2,097,152              | 2,048             | 524,287                    |
| /12                   | 1,048,576              | 4,096             | 262,143                    |
| /13                   | 524,288                | 8,192             | 131,071                    |
| /14                   | 262,144                | 16,384            | 65,535                     |
| /15                   | 131,072                | 32,768            | 32,767                     |
| /16                   | 65,536                 | 65,536            | 16,383                     |
| /17                   | 32,768                 | 131,072           | 8,191                      |
| /18                   | 16,384                 | 262,144           | 4,095                      |
| /19                   | 8,192                  | 524,288           | 2,047                      |
| /20                   | 4,096                  | 1,048,576         | 1,023                      |
| /21                   | 2,048                  | 2,097,152         | 511                        |
| /22                   | 1,024                  |