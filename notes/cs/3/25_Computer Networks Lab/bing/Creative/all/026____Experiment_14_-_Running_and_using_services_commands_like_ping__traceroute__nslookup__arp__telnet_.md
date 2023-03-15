## Experiment 14 - Running and using services/commands like ping, traceroute, nslookup, arp, telnet, ftp, etc

- The objective of this experiment is to learn how to use some common network services and commands that can help in troubleshooting, testing, and managing network connectivity and performance.
- The following are some of the services and commands that will be covered in this experiment:

  - **ping**: A command that sends packets of data to a specified destination and measures the round-trip time and packet loss rate. It can be used to test the reachability and latency of a host or a network.
  - **traceroute**: A command that traces the route of packets from the source to the destination and displays the IP addresses and hostnames of the intermediate routers and switches. It can be used to identify the network path and possible bottleneecs or failures along the way.
  - **nslookup**: A command that queries the Domain Name System (DNS) and resolves a hostname to an IP address or vice versa. It can be used to verify the DNS configuration and records of a domain or a host.
  - **arp**: A command that displays or manipulates the Address Resolution Protocol (ARP) cache, which maps IP addresses to MAC addresses on a local network. It can be used to view or modify the ARP entries or detect ARP spoofing attacks.
  - **telnet**: A service that allows remote login and access to a host using the Telnet protocol, which is a plain-text and unencrypted communication protocol. It can be used to test the connectivity and functionality of a service or a port on a host, but it is not secure and should be avoided for sensitive data transmission.
  - **ftp**: A service that allows file transfer between hosts using the File Transfer Protocol (FTP), which is a standard and widely used protocol for uploading and downloading files. It can be used to transfer files between hosts, but it is also not secure and should be replaced by more secure protocols such as SFTP or SCP.

- The following are some of the steps and procedures to run and use these services and commands:

  - To run the ping command, open a terminal or a command prompt and type `ping <destination>` where `<destination>` can be an IP address or a hostname of the target host or network. For example, `ping 8.8.8.8` or `ping www.google.com`. The command will send a series of packets and display the results for each packet, such as the size, the time, and the status. To stop the ping command, press Ctrl+C. Some of the options that can be used with the ping command are:

    - `-c <count>`: Specifies the number of packets to send. For example, `ping -c 5 8.8.8.8` will send 5 packets and then stop.
    - `-i <interval>`: Specifies the interval in seconds between each packet. For example, `ping -i 2 8.8.8.8` will send a packet every 2 seconds.
    - `-t <ttl>`: Specifies the Time to Live (TTL) value for the packets, which is the maximum number of hops that the packets can traverse before being discarded. For example, `ping -t 10 8.8.8.8` will send packets with a TTL of 10.
    - `-s <size>`: Specifies the size in bytes of the packets to send. For example, `ping -s 100 8.8.8.8` will send packets with a size of 100 bytes.

  - To run the traceroute command, open a terminal or a command prompt and type `traceroute <destination>` where `<destination>` can be an IP address or a hostname of the target host or network. For example, `traceroute 8.8.8.8` or `traceroute www.google.com`. The command will send a series of packets with increasing TTL values and display the results for each hop, such as the IP address, the hostname, and the time. Some of the options that can be used with the traceroute command are:

    - `-n`: Suppresses the hostname resolution and displays only the IP addresses of the hops. For example, `traceroute -n 8.8.8.8`.
    - `-I`: Uses ICMP packets instead of UDP packets for the traceroute. For example, `traceroute -I 8.8.8.8`.
    - `-T`: Uses TCP packets instead of UDP packets for the traceroute. For example, `traceroute -T 8.8.8.8`.
    - `-p <port>`: Specifies the destination