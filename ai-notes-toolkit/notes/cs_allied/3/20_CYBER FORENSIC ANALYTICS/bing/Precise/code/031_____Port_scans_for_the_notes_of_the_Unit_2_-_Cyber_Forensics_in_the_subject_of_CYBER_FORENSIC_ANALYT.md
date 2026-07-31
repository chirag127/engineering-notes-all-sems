### Port Scans

Port scanning is the process of sending packets to specific ports on a host and analyzing the responses to identify open ports. It is a technique used to discover services that are available on a host. Port scanning is commonly used by attackers to identify potential targets and by administrators to verify the security of their networks.

Some common types of port scans include:

1. **TCP Connect Scan:** This type of scan attempts to establish a full TCP connection with the target host. If the connection is successful, the port is considered open.

2. **SYN Scan:** This type of scan sends a SYN packet to the target host and waits for a response. If the response is a SYN-ACK packet, the port is considered open.

3. **FIN Scan:** This type of scan sends a FIN packet to the target host and waits for a response. If the response is a RST packet, the port is considered closed.

4. **Xmas Scan:** This type of scan sends a packet with the FIN, URG, and PSH flags set to the target host and waits for a response. If the response is a RST packet, the port is considered closed.

5. **Null Scan:** This type of scan sends a packet with no flags set to the target host and waits for a response. If the response is a RST packet, the port is considered closed.

Port scanning can be detected and prevented using various techniques such as firewalls, intrusion detection systems, and rate limiting. It is important for administrators to regularly scan their own networks to identify potential vulnerabilities and to monitor for unauthorized scans.