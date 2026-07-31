# ARP

- ARP stands for Address Resolution Protocol  .
- It is a network-specific standard protocol that operates at the network layer of the OSI model .
- It is used for discovering the link layer address, such as a MAC address, associated with a given internet layer address, typically an IPv4 address.
- It is a critical function in the Internet protocol suite as it enables communication between hosts on the same network segment.
- It works by sending broadcast messages to all the hosts on the network and requesting the MAC address of the host that matches the given IP address  .
- The host that has the matching IP address replies with its MAC address, and the sender stores this information in a cache table for future use  .
- ARP can also be used to update or delete entries in the cache table, or to detect duplicate IP addresses on the network .
- ARP has two types of messages: ARP request and ARP reply  .
- An ARP request is a broadcast message that contains the sender's IP and MAC addresses, and the target's IP address  .
- An ARP reply is a unicast message that contains the target's IP and MAC addresses, and the sender's IP address  .
- The format of an ARP message is shown below  :

| Field | Description | Size (bytes) |
| --- | --- | --- |
| Hardware type | Specifies the type of hardware used for the local network | 2 |
| Protocol type | Specifies the type of protocol used for the internet layer | 2 |
| Hardware size | Specifies the length of the hardware address | 1 |
| Protocol size | Specifies the length of the protocol address | 1 |
| Operation | Specifies the type of message: 1 for request, 2 for reply | 2 |
| Sender hardware address | Specifies the MAC address of the sender | Variable |
| Sender protocol address | Specifies the IP address of the sender | Variable |
| Target hardware address | Specifies the MAC address of the target | Variable |
| Target protocol address | Specifies the IP address of the target | Variable |

- An example of an ARP request and reply is shown below  :

![ARP request and reply example](https://www.geeksforgeeks.org/wp-content/uploads/arp-1.png)

- In this example, host A wants to communicate with host B, but does not know its MAC address. Host A sends an ARP request to the broadcast address, asking for the MAC address of host B. Host B receives the ARP request and sends an ARP reply to host A, containing its MAC address. Host A stores this information in its cache table and can now communicate with host B using its MAC address.