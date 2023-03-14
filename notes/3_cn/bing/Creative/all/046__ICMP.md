#### ICMP

- ICMP stands for Internet Control Message Protocol. It is a network layer protocol that is used by network devices to communicate problems and information related to IP operations.  
- ICMP is mainly used for two purposes: error reporting and network diagnostics.  
- ICMP is a connectionless protocol, which means it does not establish a connection before sending a message. It also does not use ports to identify the source and destination applications. 
- ICMP messages are encapsulated within IP packets, with a specific ICMP header and payload. The ICMP header contains a type and a code field, which indicate the purpose and the details of the message. The payload may contain additional information, such as the original IP header and the first 8 bytes of the original IP payload. 
- Some common ICMP message types are:
  - Echo request and echo reply: used to test the connectivity and latency between two devices, such as in the ping utility. 
  - Destination unreachable: used to inform the source that the destination or the route to the destination is unreachable for some reason, such as network congestion, protocol mismatch, or port unavailability. 
  - Time exceeded: used to inform the source that the IP packet has expired, either in transit (due to TTL decrement) or in reassembly (due to fragmentation). 
  - Parameter problem: used to inform the source that the IP packet has an invalid or missing field in the header. 
  - Source quench: used to inform the source that the destination or an intermediate router is experiencing congestion and requests the source to reduce the sending rate. 
  - Redirect: used to inform the source that there is a better route to the destination and to update its routing table accordingly. 
- ICMP can also be used for malicious purposes, such as in distributed denial-of-service (DDoS) attacks. For example, an attacker can send a large number of ICMP echo requests to a target with a spoofed source IP address, causing the target to send echo replies to the spoofed address, which may be another victim. This is known as an ICMP flood attack. Another example is an attacker sending an IP packet with a size larger than the maximum transmission unit (MTU) of the network, causing the packet to be fragmented and reassembled at the destination. If the reassembled packet exceeds the allowed size of 65,535 bytes, it may cause the destination to crash or reboot. This is known as the ping of death attack.  

: Internet Control Message Protocol - Wikipedia
: What is ICMP? | Internet Control Message Protocol | Cloudflare
: What is ICMP (Internet Control Message Protocol)? | Fortinet
: ICMP (Internet Control Message Protocol) - SearchNetworking