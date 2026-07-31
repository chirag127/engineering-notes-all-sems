## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc.

In this experiment, we will learn about various services and commands that are used for network troubleshooting and management. These services and commands are essential for any network administrator or IT professional who deals with network-related issues. Here are some of the services and commands that we will explore in this experiment:

- **Ping**: Ping is a command-line utility that is used to test the connectivity between two network devices. It sends an ICMP (Internet Control Message Protocol) echo request to the destination device and waits for a reply. If the destination device responds, it means that the network connection is working fine. Ping is one of the most widely used commands for network troubleshooting.

- **Traceroute**: Traceroute is a command-line utility that is used to trace the path that a packet takes from the source device to the destination device. It sends a series of ICMP echo requests with varying TTL (Time To Live) values to the destination device. As the packets travel through the network, each router that the packets pass through decrements the TTL value. When the TTL value reaches zero, the router discards the packet and sends an ICMP time exceeded message back to the source device. Traceroute uses these ICMP time exceeded messages to build a list of all the routers that the packets pass through.

- **Nslookup**: Nslookup is a command-line utility that is used to query the DNS (Domain Name System) server for information about a specific domain name or IP address. It can be used to resolve domain names to IP addresses or vice versa. Nslookup is a very useful tool for troubleshooting DNS-related issues.

- **Arp**: Arp is a command-line utility that is used to view and manipulate the ARP (Address Resolution Protocol) cache on a device. The ARP cache is a table that maps IP addresses to MAC (Media Access Control) addresses. Arp can be used to view the contents of the ARP cache, add or delete entries from the ARP cache, and flush the entire ARP cache.

- **Telnet**: Telnet is a command-line utility that is used to establish a remote terminal session with a network device. It allows the user to connect to a device over a network and enter commands just as if they were sitting in front of the device. Telnet is a very useful tool for managing network devices remotely.

- **FTP**: FTP (File Transfer Protocol) is a protocol that is used for transferring files over a network. It allows the user to transfer files between two devices that are connected to the network. FTP is a very useful tool for file sharing and distribution.

In conclusion, the above-mentioned services and commands are essential for network troubleshooting and management. They are widely used by network administrators and IT professionals to diagnose and resolve network-related issues. It is important to have a good understanding of these services and commands to be able to effectively manage and troubleshoot networks.