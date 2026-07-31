### ICMP

- ICMP stands for Internet Control Message Protocol  .
- It is a network layer protocol used by network devices to diagnose network communication issues  .
- It is not associated with any transport layer protocol, such as TCP or UDP. It is a connectionless protocol, meaning a device does not need to open a connection with the target device before sending a message.
- It is used to generate error messages to the source IP address when network problems prevent delivery of IP packets. It is also used to determine whether or not data is reaching its intended destination in a timely manner .
- It is a special type of packet used for inter-device communication, carrying everything from redirect instructions to timestamps for synchronization between devices.
- Some common types of ICMP messages are:
  - Echo request and echo reply: used to test the reachability and latency of a destination device  . This is the basis of the ping command.
  - Destination unreachable: used to inform the source device that the destination device or network is unreachable for some reason  .
  - Time exceeded: used to inform the source device that the time to live (TTL) of a packet has expired and the packet has been discarded  .
  - Parameter problem: used to inform the source device that the header of a packet is invalid or incorrect  .
  - Source quench: used to inform the source device that the destination device is congested and cannot process more packets  .
  - Redirect: used to inform the source device that there is a better route to the destination device or network  .
  - Router advertisement and router solicitation: used to discover and advertise the presence of routers on a network  .
- ICMP is important for IOT devices because it helps to monitor and troubleshoot the connectivity and performance of the network . It also helps to optimize the routing of packets and avoid congestion and delays . ICMP can also be used to detect and prevent malicious attacks on the network, such as denial-of-service (DoS) or ping of death .