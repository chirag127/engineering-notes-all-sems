# MPTCP

- MPTCP stands for Multipath TCP, which is an extension to the original TCP protocol (single-path)  .
- MPTCP enables a transport connection to operate across multiple paths simultaneously, and brings network connection redundancy to user endpoint devices  .
- MPTCP aims at allowing a TCP connection to use multiple paths to maximize throughput and increase redundancy .
- MPTCP is a set of extensions to regular TCP that enables a single data flow to be separated and carried across multiple connections .
- MPTCP is an ongoing effort of the Internet Engineering Task Force's (IETF) Multipath TCP working group .
- MPTCP has several advantages over single-path TCP, such as:
  - Improved resilience to path failures and network congestion  .
  - Increased bandwidth utilization and efficiency  .
  - Seamless mobility and handover between different network interfaces  .
  - Reduced need for application-layer adaptations  .
- MPTCP has some challenges and limitations, such as:
  - Compatibility with existing network devices and middleboxes  .
  - Security and privacy issues related to exposing multiple addresses  .
  - Congestion control and fairness issues with other flows  .
  - Implementation and deployment complexity  .
- MPTCP is supported by Red Hat Enterprise Linux 8.3 and later versions .
- MPTCP can be configured and managed using the mptcpd daemon and the mptcpctl command-line tool .
- MPTCP can be enabled or disabled on a per-socket basis using the IP_MPTCP socket option .
- MPTCP can be tested using tools such as iperf3, curl, wget, and nc .

: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/getting-started-with-multipath-tcp_configuring-and-managing-networking
: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/getting-started-with-multipath-tcp_configuring-and-managing-networking
: https://en.wikipedia.org/wiki/Multipath_TCP
: https://www.cisco.com/c/en/us/support/docs/ip/transmission-control-protocol-tcp/116519-technote-mptcp-00.html
: https://developers.redhat.com/blog/2020/08/19/multipath-tcp-on-red-hat-enterprise-linux-8-3-from-0-to-1-subflows