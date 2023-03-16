### MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol (single-path)  .
- MPTCP enables a transport connection to operate across multiple paths simultaneously, and brings network connection redundancy to user endpoint devices  .
- MPTCP aims at allowing a TCP connection to use multiple paths to maximize throughput and increase redundancy .
- MPTCP is a set of extensions to regular TCP that enables a single data flow to be separated and carried across multiple connections .
- MPTCP uses the concept of subflows, which are TCP connections established between different IP addresses of the same hosts  .
- MPTCP provides the following advantages compared to the single-path TCP  :
  - Improved connection stability and resilience to failures, as MPTCP can switch to another path if one path fails or degrades.
  - Increased bandwidth utilization and performance, as MPTCP can aggregate the available bandwidth of multiple paths.
  - Enhanced mobility and seamless handover, as MPTCP can maintain the connection even if the IP address changes due to moving to a different network.
  - Reduced congestion and load balancing, as MPTCP can distribute the traffic across multiple paths and avoid congested links.