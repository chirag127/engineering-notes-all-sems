### MPTCP

Multipath TCP (MPTCP) is an extension to TCP that enables the use of multiple network paths between two endpoints. It is designed to improve the performance and resilience of TCP-based applications in networks with multiple paths, such as mobile networks, data centers, and cloud environments.

Here are some key points to know about MPTCP:

- MPTCP allows a single TCP connection to use multiple paths simultaneously. This means that data can be sent and received across multiple network interfaces (e.g., Wi-Fi and cellular) at the same time, increasing the overall throughput and reducing latency.

- MPTCP uses subflows to manage the different paths. Each subflow is a separate TCP connection that runs in parallel with the others, and they all share the same congestion control algorithm and sequence numbering scheme.

- MPTCP can dynamically add or remove subflows based on network conditions. For example, if one path becomes congested, MPTCP can shift traffic to another path that has more capacity. This helps to avoid network congestion and improve the user experience.

- MPTCP is backward-compatible with traditional TCP. If only one path is available, MPTCP will behave like regular TCP and use that path exclusively.

- MPTCP requires modification to both the client and server endpoints. The client must be MPTCP-enabled and negotiate the use of MPTCP with the server. The server must also be MPTCP-enabled and be able to handle multiple subflows.

- MPTCP has been implemented in various operating systems and networking stacks, including Linux, FreeBSD, and Windows. It is also supported by some mobile devices and routers.

- MPTCP has several use cases, including improving the performance of real-time applications (such as video streaming), providing seamless handoffs between different network interfaces, and increasing fault tolerance in data center networks.

In summary, MPTCP is a TCP extension that enables the use of multiple network paths between two endpoints. It provides improved performance and resilience in networks with multiple paths, and can dynamically adjust to changing network conditions. MPTCP is backward-compatible with traditional TCP and has several use cases in different environments.