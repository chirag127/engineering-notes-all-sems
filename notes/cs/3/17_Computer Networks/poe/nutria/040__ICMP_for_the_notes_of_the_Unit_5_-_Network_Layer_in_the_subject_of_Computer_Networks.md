
### ICMP for the Notes of Unit 5 - Network Layer in Computer Networks

* Internet Control Message Protocol (ICMP) is a network layer protocol used for communication between network devices. It is used to report errors and exchange information about network conditions.
* ICMP messages are sent as Internet Protocol (IP) datagrams, and are used to provide error and control messages.
* ICMP messages can be used to inform a host of problems on the network, such as: 
    * Unreachable destination: An ICMP message is sent when a packet is sent to an address that does not exist.
    * Redirect: An ICMP message is sent when a packet is sent to a router that is not the best route.
    * Source Quench: An ICMP message is sent when a router is overloaded and needs to reduce the number of packets it is processing.
    * Time Exceeded: An ICMP message is sent when a packet has been in transit for too long.
* ICMP also provides information about the network, such as: 
    * Echo Request: An ICMP message is sent to a host to check if it is alive.
    * Echo Reply: An ICMP message is sent in response to an Echo Request.
    * Router Advertisement: An ICMP message is sent by a router to inform hosts of its presence.
    * Router Solicitation: An ICMP message is sent by a host to discover routers on the network.