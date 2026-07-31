### Port Scans

Port scanning is the process of sending packets to specific ports on a host and analyzing the responses to determine which ports are open and which are closed. This information can be used to identify potential vulnerabilities and attack vectors on a system.

1. **Types of Port Scans**: There are several types of port scans, including TCP connect scans, SYN scans, FIN scans, Xmas scans, and Null scans. Each type of scan uses a different method to determine the status of a port.

2. **TCP Connect Scans**: A TCP connect scan is the most basic type of port scan. It involves attempting to establish a full TCP connection to each port on the target host. If the connection is successful, the port is considered open. If the connection is refused or times out, the port is considered closed.

3. **SYN Scans**: A SYN scan, also known as a "half-open" scan, is a more stealthy type of port scan. It involves sending a SYN packet to each port on the target host and analyzing the response. If the target host responds with a SYN/ACK packet, the port is considered open. If the target host responds with a RST packet, the port is considered closed.

4. **FIN, Xmas, and Null Scans**: FIN, Xmas, and Null scans are all types of "stealth" scans that can be used to determine the status of a port. These scans involve sending packets with specific flags set to each port on the target host and analyzing the response. The specific flags used and the expected response vary depending on the type of scan.

5. **Uses of Port Scans**: Port scans can be used for a variety of purposes, including network mapping, vulnerability assessment, and penetration testing. They can also be used by attackers to identify potential targets and attack vectors.

6. **Detecting Port Scans**: There are several methods that can be used to detect port scans, including analyzing network traffic for patterns of activity that are indicative of a port scan, and using intrusion detection systems (IDS) to identify and alert on port scan activity.

7. **Preventing Port Scans**: There are several steps that can be taken to prevent or mitigate the impact of port scans, including using firewalls to block incoming traffic to unused ports, and using network segmentation to limit the visibility of internal systems to external attackers.