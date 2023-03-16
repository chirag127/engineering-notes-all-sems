### Port scans

- A port scan is a technique used by attackers to discover the services running on a target system.
- A port is a logical endpoint for network communication. Each port is associated with a protocol and an application that listens for incoming or outgoing data.
- There are 65535 ports in total, divided into well-known ports (0-1023), registered ports (1024-49151), and dynamic or private ports (49152-65535).
- A port scan can reveal the following information about a target system:
  - The operating system and its version
  - The network services and their versions
  - The network configuration and security policies
  - The vulnerabilities and exploits that can be used to compromise the system
- A port scan can be performed using various tools and techniques, such as:
  - TCP connect scan: This scan attempts to establish a full TCP connection with each port by sending a SYN packet and waiting for a SYN/ACK or RST/ACK response. This scan is reliable but noisy and can be detected by firewalls and intrusion detection systems (IDS).
  - TCP SYN scan: This scan sends a SYN packet to each port and analyzes the response. If the response is a SYN/ACK, the port is open. If the response is a RST/ACK, the port is closed. If there is no response, the port is filtered. This scan is faster and stealthier than a TCP connect scan, but it may not work against some firewalls or IDS that drop SYN packets.
  - TCP ACK scan: This scan sends an ACK packet to each port and analyzes the response. If the response is a RST/ACK, the port is either open or closed. If there is no response, the port is filtered. This scan can be used to determine the state of the firewall rules on the target system.
  - TCP FIN, Xmas, or Null scan: These scans send packets with different TCP flags to each port and analyze the response. If the response is a RST/ACK, the port is closed. If there is no response, the port is either open or filtered. These scans can bypass some firewalls or IDS that only check for SYN packets, but they may not work against some operating systems that do not follow the TCP RFC specifications.
  - UDP scan: This scan sends a UDP packet to each port and analyzes the response. If the response is an ICMP port unreachable message, the port is closed. If there is no response, the port is either open or filtered. This scan is slow and unreliable, as many UDP services do not respond to unsolicited packets, and many firewalls or IDS drop UDP packets.
  - ICMP scan: This scan sends an ICMP echo request (ping) to the target system and analyzes the response. If the response is an ICMP echo reply, the system is alive. If the response is an ICMP destination unreachable or time exceeded message, the system is unreachable or filtered. If there is no response, the system is either dead or filtered. This scan can be used to discover the hosts on a network, but it may not work against some firewalls or IDS that block ICMP packets.
  - Service scan: This scan attempts to identify the application and version running on each open port by sending specific probes or requests and analyzing the response. This scan can provide more detailed information about the target system, but it may also trigger some alarms or defenses on the target system.