### ARP

- ARP stands for Address Resolution Protocol   .
- It is a communication protocol used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address   .
- It is a critical function in the Internet protocol suite .
- It was defined in 1982 by RFC 826, which is Internet Standard STD 37 .
- It operates in two phases: request and reply  .
- In the request phase, a host sends a broadcast message to all hosts on the network, asking for the MAC address of the host with a specific IP address  .
- In the reply phase, the host with the matching IP address responds with a unicast message containing its MAC address  .
- The requesting host then updates its ARP cache, which is a table that stores the mappings of IP addresses and MAC addresses  .
- ARP can be used for both static and dynamic IP addresses .
- ARP can also be used for proxy ARP, gratuitous ARP, and inverse ARP  .
- Proxy ARP is when a router answers ARP requests on behalf of another host  .
- Gratuitous ARP is when a host sends an ARP request for its own IP address, to detect IP conflicts or update other hosts' ARP caches  .
- Inverse ARP is when a host asks for the IP address of another host with a known MAC address .