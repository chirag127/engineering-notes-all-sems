### Port Scans

Port scanning is a technique used to identify open ports on a system. The process involves sending multiple requests to a target machine's port to determine which ports are open and what services are running on them. In this section, we will discuss the different types of port scans and their significance in cyber forensics.

#### Types of Port Scans

1. TCP Connect Scans: This type of scan establishes a full TCP/IP connection with the target machine. It sends a SYN packet to the server and waits for a response. If the server responds with a SYN-ACK packet, the scanner sends an ACK packet to establish a connection. TCP Connect Scans are useful for identifying open ports and services running on a system.

2. SYN Scans: SYN Scans are similar to TCP Connect Scans, but they do not complete the connection process. The scanner sends a SYN packet to the target machine and waits for a response. If the server responds with a SYN-ACK packet, the scanner sends an RST packet to terminate the connection. SYN Scans are faster than TCP Connect Scans but may not be as reliable.

3. UDP Scans: UDP Scans are used to identify open ports on a server that are not associated with TCP connections. UDP packets are sent to the server, and the scanner waits for a response. If the server responds, the port is considered open. UDP Scans are used to identify services such as DNS and DHCP running on a system.

4. XMAS Scans: XMAS Scans are a type of TCP Scan that sends packets with the FIN, URG, and PSH flags set. If a port is open, the server will not respond to these packets. XMAS Scans are useful for identifying servers that are configured to ignore packets that do not adhere to the TCP protocol.

#### Significance of Port Scans

Port Scans are an essential tool in cyber forensics. They are used to identify open ports on a system, which can be used to determine what services are running on the machine. By identifying the services running on a system, investigators can determine what type of data may have been stored on the machine. Additionally, port scans can be used to identify vulnerabilities in a system, which can be exploited by attackers. By identifying these vulnerabilities, investigators can recommend security measures to prevent future attacks.

In conclusion, Port Scans are an essential tool in cyber forensics. The different types of port scans have unique advantages and are used to identify open ports on a system, which can help investigators identify the services running on the machine. By understanding the significance of port scans, investigators can better identify and prevent cyber-attacks.