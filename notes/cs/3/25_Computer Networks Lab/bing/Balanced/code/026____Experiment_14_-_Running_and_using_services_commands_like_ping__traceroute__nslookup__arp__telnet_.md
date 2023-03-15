## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network utilities for troubleshooting and information gathering.
- The network utilities are programs that run on a host computer and interact with the network or other hosts.
- Some of the network utilities that will be covered in this experiment are:

  - ping: a program that sends a packet to a destination IP address and waits for a reply. It is used to test the connectivity and latency between two hosts .
  - traceroute: a program that sends a series of packets to a destination IP address and records the routers that the packets pass through. It is used to trace the path and measure the hop count and delay between two hosts .
  - nslookup: a program that queries the Domain Name System (DNS) to obtain the IP address or domain name of a host or other DNS records. It is used to verify the DNS configuration and resolve host names  .
  - arp: a program that displays or modifies the Address Resolution Protocol (ARP) cache of a host. The ARP cache is a table that maps the IP addresses to the MAC addresses of the hosts on the same network. It is used to view or manipulate the ARP entries of a host  .
  - telnet: a program that establishes a remote terminal session with another host using the Telnet protocol. It is used to access and control another host over the network .
  - ftp: a program that transfers files between two hosts using the File Transfer Protocol (FTP). It is used to upload or download files over the network .

- To run these network utilities, you need to open a command prompt or a terminal window on your host computer and type the name of the utility followed by the parameters or options. For example, to ping the IP address 8.8.8.8, you would type:

  ```
  ping 8.8.8.8
  ```

- The output of the network utilities will vary depending on the operating system, the network configuration, and the destination host. You can use the help option (-h or /?) to see the available parameters or options for each utility. For example, to see the help for ping, you would type:

  ```
  ping -h
  ```

- In this experiment, you will run and use the network utilities to perform various tasks and observe the results. You will also learn how to interpret the output and troubleshoot common network problems.