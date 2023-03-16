### DDoS Attacks

- A DDoS attack is a **distributed denial-of-service** attack that aims to disrupt the normal functioning of a target server, service, or network by overwhelming it with a large amount of traffic from multiple sources   .
- A DDoS attack can be motivated by various reasons, such as cybercrime, hacktivism, cyberwarfare, or personal vendetta .
- A DDoS attack can have different types and techniques, depending on the layer of the network protocol stack that is targeted, the type of traffic that is generated, and the source of the attack traffic   .
- Some common types of DDoS attacks are:
  - **SYN flood**: This attack exploits the TCP handshake process by sending a large number of SYN packets to the target server, without completing the connection. This causes the server to allocate resources for half-open connections, eventually exhausting its memory and bandwidth  .
  - **UDP flood**: This attack sends a large number of UDP packets to random ports on the target server, causing it to respond with ICMP packets indicating that the port is unreachable. This consumes the server's network resources and bandwidth  .
  - **HTTP flood**: This attack sends a large number of HTTP requests to the target web server, simulating legitimate users. This consumes the server's CPU and memory resources, as well as its application layer resources  .
  - **DNS amplification**: This attack exploits the DNS protocol by sending spoofed DNS queries to open DNS resolvers, with the source IP address set to the target server. The DNS resolvers then send large DNS responses to the target server, amplifying the attack traffic by a factor of 10 to 100  .
  - **NTP amplification**: This attack exploits the NTP protocol by sending spoofed NTP requests to open NTP servers, with the source IP address set to the target server. The NTP servers then send large NTP responses to the target server, amplifying the attack traffic by a factor of 200 to 1000  .
- Some common techniques to mitigate DDoS attacks are:
  - **Firewalls**: These devices can filter out malicious traffic based on predefined rules, such as blocking traffic from certain IP addresses, ports, or protocols  .
  - **Load balancers**: These devices can distribute the incoming traffic among multiple servers, reducing the load on each server and increasing the availability of the service  .
  - **Intrusion detection and prevention systems (IDS/IPS)**: These devices can monitor the network traffic and detect anomalous patterns, such as a sudden spike in traffic or a large number of packets from a single source. They can also take actions to block or redirect the malicious traffic  .
  - **DDoS protection services**: These services can provide cloud-based solutions to detect and mitigate DDoS attacks, by using techniques such as traffic scrubbing, traffic shaping, and content delivery networks (CDN)   .