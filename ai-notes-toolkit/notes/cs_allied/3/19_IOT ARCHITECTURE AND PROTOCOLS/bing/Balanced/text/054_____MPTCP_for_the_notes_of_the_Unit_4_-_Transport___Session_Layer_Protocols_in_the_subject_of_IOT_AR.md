### MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol that allows a transport connection to operate across multiple paths simultaneously .
- MPTCP brings network connection redundancy to user endpoint devices, and improves connection stability, throughput, and resilience compared to single-path TCP  .
- MPTCP works by establishing multiple TCP subflows between the endpoints, each subflow using a different pair of source and destination addresses .
- MPTCP uses a new option in the TCP header to exchange additional information between the endpoints, such as the available addresses, the subflow identifiers, and the data sequence mapping .
- MPTCP is backward compatible with existing TCP applications and network infrastructure, as it falls back to regular TCP when MPTCP is not supported by either endpoint or any intermediate device .
- MPTCP is suitable for scenarios where multiple network interfaces are available, such as mobile devices with Wi-Fi and cellular connections, or data centers with multiple links between servers  .
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions, and can be enabled and configured using the `mptcp` kernel module and the `sysctl` command  .