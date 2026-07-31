### MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol (single-path)   .
- MPTCP enables a transport connection to operate across multiple paths simultaneously, and brings network connection redundancy to user endpoint devices   .
- MPTCP is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group, that aims at allowing a TCP connection to use multiple paths to maximize throughput and increase redundancy .
- MPTCP has several advantages over single-path TCP, such as   :
  - Improved connection stability and resilience to failures, as MPTCP can switch to another path if one path fails or degrades.
  - Increased bandwidth utilization and performance, as MPTCP can aggregate the available bandwidth of multiple paths.
  - Enhanced mobility and seamless handover, as MPTCP can maintain a connection even if the IP address of the device changes due to moving between different networks.
  - Reduced congestion and load balancing, as MPTCP can distribute the traffic across multiple paths and avoid congested links.
- MPTCP works by establishing a regular TCP connection as the initial subflow, and then using additional subflows to utilize other paths between the endpoints   .
- MPTCP uses a set of extensions to regular TCP, such as  :
  - A new TCP option for signaling MPTCP capabilities and exchanging keys for authentication.
  - A new TCP option for advertising and discovering additional addresses for subflow establishment.
  - A new TCP option for managing the subflows and their states.
  - A new TCP option for mapping the data sequence numbers of the subflows to the connection-level sequence numbers.
  - A new TCP option for indicating the data checksum of the subflows to detect data corruption.
  - A new congestion control algorithm that takes into account the characteristics of the subflows and the connection.
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions, and can be configured using the `mptcp` command or the `sysctl` utility   .
- MPTCP is compatible with existing applications and network devices, as it falls back to regular TCP if MPTCP is not supported by either endpoint or any intermediate device   .