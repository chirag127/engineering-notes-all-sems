# Port scans

- A port scan is a technique used by cybercriminals to find out information about a system they are going to target .
- It involves scanning through a network system and determining which ports are open, which are sending data, and which are receiving data .
- A port is a logical endpoint of communication in a network, identified by a number from 0 to 65535.
- A port scan can reveal the services, applications, and operating systems running on a system, as well as the security devices such as firewalls and intrusion detection systems .
- Port scanning is a fundamental part of the pre-attack phase of a penetration test, as it can help identify vulnerabilities and potential entry points for an attack.
- Port scanning can also be used for legitimate purposes, such as network monitoring, troubleshooting, and auditing.

## Port scanning techniques

- There are several different port scanning techniques, each with its own advantages and disadvantages .
- Some of the common port scanning techniques are:

  - Ping scans: A ping is used to check whether a network data packet can reach an IP address without any issues. Ping scans can determine if a host is alive and responsive on a network.
  - Half-open or SYN scans: Attackers can check the state of a port without creating a full connection, by sending a SYN (synchronization) packet and waiting for a response. If the response is a SYN-ACK (synchronization-acknowledgment) packet, the port is open. If the response is a RST (reset) packet, the port is closed .
  - Full connection or TCP connect scans: Attackers can establish a full TCP (transmission control protocol) connection with each port, by sending a SYN packet, receiving a SYN-ACK packet, and sending an ACK (acknowledgment) packet. This technique is more reliable but also more detectable and slower than a SYN scan .
  - Stealth or FIN scans: Attackers can send a FIN (finish) packet to a port, which normally indicates the end of a connection. If the port is closed, it will respond with a RST packet. If the port is open, it will ignore the packet. This technique can bypass some firewalls and intrusion detection systems, but it may not work on some operating systems .
  - UDP (user datagram protocol) scans: Attackers can send a UDP packet to a port, which is a connectionless protocol that does not require a handshake. If the port is closed, it will respond with an ICMP (internet control message protocol) error message. If the port is open, it will either respond with a UDP packet or remain silent. This technique can be used to find UDP services, but it is slow and unreliable, as some firewalls and routers may block or filter UDP packets .

## Port scan detection and prevention

- Port scanning can be detected and prevented by using various methods, such as:

  - Firewalls: Firewalls can filter and block incoming and outgoing traffic based on predefined rules and policies. Firewalls can also log and alert on suspicious or malicious activity, such as port scans.
  - Intrusion detection systems (IDS): IDS can monitor and analyze network traffic and detect anomalies and patterns that indicate a port scan. IDS can also generate alerts and reports on port scan incidents.
  - Intrusion prevention systems (IPS): IPS can perform the same functions as IDS, but also take actions to stop or mitigate a port scan, such as blocking the source IP address, dropping the packets, or resetting the connection.
  - Honeypots: Honeypots are decoy systems that are designed to attract and trap attackers. Honeypots can be used to divert port scans away from the real systems, and to collect information and evidence on the attackers and their techniques.