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
  - UDP (user datagram protocol) scans: Attackers can send UDP packets to each port and wait for a response. If the response is an ICMP (internet control message protocol) port unreachable message, the port is closed. If there is no response, the port is either open or filtered by a firewall .
  - Stealth or FIN scans: Attackers can send a FIN (finish) packet to each port and wait for a response. If the response is a RST packet, the port is closed. If there is no response, the port is either open or filtered by a firewall. This technique can bypass some firewalls and intrusion detection systems that only monitor SYN packets .
  - Xmas or NULL scans: Attackers can send packets with different combinations of flags, such as FIN, URG (urgent), and PSH (push), or no flags at all, to each port and wait for a response. If the response is a RST packet, the port is closed. If there is no response, the port is either open or filtered by a firewall. These techniques can also evade some firewalls and intrusion detection systems that only monitor SYN packets .
  - ACK (acknowledgment) scans: Attackers can send ACK packets to each port and wait for a response. If the response is a RST packet, the port is either open or closed, but not filtered by a firewall. If there is no response, the port is filtered by a firewall. This technique can help determine the type of firewall in place .
  - Idle or zombie scans: Attackers can use a third-party host, called a zombie, to scan a target system without revealing their own IP address. The attacker sends a SYN packet to the zombie, which responds with a SYN-ACK packet. The attacker then sends a spoofed SYN packet to the target system, using the zombie's IP address as the source. If the target system responds with a SYN-ACK packet, the port is open, and the zombie's IP ID (identification) field will increase by one. If the target system responds with a RST packet, the port is closed, and the zombie's IP ID field will not change. The attacker can then send another SYN-ACK packet to the zombie and check the IP ID field to determine the state of the