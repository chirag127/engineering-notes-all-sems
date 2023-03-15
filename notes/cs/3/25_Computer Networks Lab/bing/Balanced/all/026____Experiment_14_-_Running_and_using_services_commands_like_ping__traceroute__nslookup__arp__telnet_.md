## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network utilities for troubleshooting and information gathering.
- The network utilities are programs that run on a host computer and interact with the network or other hosts.
- Some of the network utilities that will be covered in this experiment are:

  - **ping**: A program that sends a packet to a destination IP address and waits for a reply. It is used to test the connectivity and latency between two hosts. The ping command can also display statistics such as packet loss, round-trip time, and time to live (TTL)  .
  - **traceroute**: A program that traces the path of a packet from the source to the destination. It shows the IP addresses and hostnames of the routers that the packet passes through. It is used to diagnose routing problems and network congestion. The traceroute command can also display the time it takes for each hop  .
  - **nslookup**: A program that queries the Domain Name System (DNS) to obtain information about a domain name or an IP address. It is used to verify the DNS configuration and resolve domain names to IP addresses or vice versa. The nslookup command can also display other DNS records such as MX, NS, SOA, etc  .
  - **arp**: A program that displays or modifies the Address Resolution Protocol (ARP) cache. The ARP cache is a table that maps IP addresses to MAC addresses on the local network. It is used to find the MAC address of a host with a known IP address or vice versa. The arp command can also add or delete entries from the ARP cache  .
  - **telnet**: A program that establishes a remote connection to another host using the Telnet protocol. It is used to access and control a host that runs a Telnet server. The telnet command can also send commands and receive output from the remote host  .
  - **ftp**: A program that transfers files between two hosts using the File Transfer Protocol (FTP). It is used to upload and download files from a host that runs an FTP server. The ftp command can also list, create, delete, and rename files and directories on the remote host  .

- To run these network utilities, you need to open a command prompt or a terminal window on your host computer and type the name of the utility followed by the parameters or options. For example, to ping the IP address 8.8.8.8, you would type:

  ```
  ping 8.8.8.8
  ```

- To see the available parameters or options for each utility, you can type the name of the utility followed by a question mark (?) or a slash and a question mark (/?) on Windows, or a hyphen and a letter h (-h) on Linux or Mac OS X. For example, to see the options for the traceroute command on Linux, you would type:

  ```
  traceroute -h
  ```

- To exit from a network utility, you can type Ctrl+C on Windows or Linux, or Ctrl+D on Mac OS X. For some utilities, such as telnet and ftp, you can also type quit or bye to end the session.