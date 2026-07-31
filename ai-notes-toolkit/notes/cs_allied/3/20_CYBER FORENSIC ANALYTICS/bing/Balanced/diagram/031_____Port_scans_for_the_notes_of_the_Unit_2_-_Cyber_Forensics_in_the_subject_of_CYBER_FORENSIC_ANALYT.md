### Port scans

- A port scan is a technique used by cybercriminals to find out information about a system they are going to target .
- It involves scanning through a network system and determining which ports are open, which are sending data, and which are receiving data .
- A port is a logical endpoint of communication in a network, identified by a number from 0 to 65535.
- A port scan can reveal whether active security devices like firewalls are being used by an organization, and what services or applications are running on the system .
- Port scanning is a fundamental part of the pre-attack phase of a penetration test, as it can help locate vulnerabilities in a network that malicious hackers can exploit.
- There are several different port scanning techniques, including :
  - Ping scans: A ping is used to check whether a network data packet can reach an IP address without any issues. Ping scans can identify which hosts are alive on a network.
  - Half-open or SYN scans: Attackers can check the state of a port without creating a full connection, by sending a SYN packet and waiting for a response. If the response is a SYN-ACK packet, the port is open. If the response is a RST packet, the port is closed.
  - Full connection or TCP scans: Attackers can establish a full connection with a port by sending a SYN packet, receiving a SYN-ACK packet, and sending an ACK packet. This can confirm the port state and the service running on it, but it can also be detected by firewalls and intrusion detection systems.
  - Stealth or FIN scans: Attackers can avoid detection by sending a FIN packet to a port, which normally indicates the end of a connection. If the port is closed, it will send a RST packet. If the port is open, it will ignore the packet. This can bypass some firewalls and IDS.
  - UDP scans: Attackers can scan for UDP ports, which are used for connectionless protocols. They can send a UDP packet to a port and wait for a response. If the response is an ICMP port unreachable message, the port is closed. If there is no response, the port is open or filtered by a firewall.
  - Service or version scans: Attackers can scan for the specific service or application running on a port, by sending a probe packet and analyzing the response. This can reveal the name, version, and configuration of the service, which can help identify potential vulnerabilities.
- Port scanning can be detected and prevented by using various methods, such as :
  - Firewalls: Firewalls can block or filter incoming and outgoing traffic based on rules and policies. They can also log and alert on suspicious activity, such as multiple connection attempts from the same source.
  - Intrusion detection systems (IDS): IDS can monitor and analyze network traffic for signs of malicious activity, such as port scans. They can also alert or respond to potential attacks, such as blocking the source IP address or sending a fake response.
  - Honeypots: Honeypots are decoy systems that are designed to attract and trap attackers. They can simulate real services and ports, and record the attackers' actions and techniques. They can also divert the attackers' attention from the real systems and ports.
  - Port knocking: Port knocking is a technique that involves hiding a port until a specific sequence of packets is sent to other ports. This can prevent unauthorized access to the port, as only the legitimate users know the secret sequence.