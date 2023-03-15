# CIDR

- CIDR stands for **Classless Inter-Domain Routing**   .
- It is a method for **allocating IP addresses** and for **IP routing**   .
- It was introduced in **1993** by the **Internet Engineering Task Force** to replace the previous **classful network addressing** architecture on the Internet .
- In CIDR, there is **no wastage** of IP addresses as compared to classful addressing because only the numbers of IP addresses that are demanded by the customer are allocated to the customer.
- CIDR uses a **slash notation** to specify the **network prefix** and the **host identifier** of an IP address    .
- The network prefix is the **number of bits** that make up the **routing or networking portion** of the IP address.
- The host identifier is the **remaining bits** that make up the **individual device** portion of the IP address.
- For example, the IP address **192.168.1.15/24** means that the network prefix is **24 bits** long and the host identifier is **8 bits** long.
- The network prefix can be used to **identify the network** that the IP address belongs to.
- The host identifier can be used to **identify the device** within the network.
- CIDR allows for **variable-length subnet masking** (VLSM), which means that different subnets within the same network can have different sizes    .
- CIDR also allows for **route aggregation**, which means that multiple contiguous subnets can be represented by a single routing entry    .
- CIDR helps to **reduce the size** of the **routing tables** and to **improve the efficiency** of the **routing process**    .
- CIDR also helps to **slow down the exhaustion** of the **IPv4 address space** by allowing more efficient use of the available addresses    .