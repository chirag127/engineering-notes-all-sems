## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

### Aim
To study the basic features and commands of NS and to simulate the congestion control algorithms using NS.

### Theory
- NS (Network Simulator) is a discrete event simulator targeted at networking research. It provides substantial support for simulation of TCP, routing, and multicast protocols over wired and wireless networks.
- NS is written in C++ and uses an object-oriented design. It also has a scripting language called OTcl (Object-oriented Tool Command Language) that is used to configure and control the simulation scenarios.
- NS has a rich set of components that can be used to model different network scenarios. Some of the components are:
  - Nodes: represent routers, hosts, or other network devices.
  - Links: represent physical connections between nodes, with attributes such as bandwidth, delay, and error rate.
  - Agents: represent transport layer protocols, such as TCP, UDP, or FTP.
  - Applications: represent application layer protocols, such as HTTP, Telnet, or CBR (Constant Bit Rate).
  - Queues: represent buffers at the links, with different queue management algorithms, such as DropTail, RED (Random Early Detection), or FQ (Fair Queueing).
  - Traces: represent the output of the simulation, such as packet traces, throughput, delay, or congestion window size.
- NS uses a Tcl script to define the network topology, the traffic sources, the simulation parameters, and the output format. The script can also invoke C++ code to create new components or modify existing ones.
- NS can also use a graphical user interface called NAM (Network Animator) to visualize the simulation results. NAM can show the packet movements, the link states, the queue sizes, and the node statistics.

- Congestion control is the process of managing the network resources to avoid congestion and ensure fair and efficient data transmission. Congestion occurs when the network demand exceeds the network capacity, resulting in packet loss, long delays, and reduced throughput.
- Congestion control algorithms are implemented at the transport layer, mainly by TCP. TCP uses a window-based mechanism to regulate the amount of data that can be sent without receiving an acknowledgment. The window size is dynamically adjusted based on the network feedback, such as packet loss, delay, or explicit signals.
- Some of the congestion control algorithms used by TCP are:
  - TCP Tahoe: the original TCP algorithm that uses slow start, congestion avoidance, and fast retransmit. Slow start increases the window size exponentially until a threshold is reached or a packet is lost. Congestion avoidance increases the window size linearly until a packet is lost. Fast retransmit retransmits the lost packet without waiting for a timeout. When a packet is lost, the threshold is halved and the window size is reset to one segment.
  - TCP Reno: an improvement over TCP Tahoe that uses fast recovery. Fast recovery keeps the threshold at half of the previous window size and reduces the window size to the threshold when a packet is lost. Then it increases the window size by one segment for each duplicate acknowledgment received, until a new acknowledgment arrives or a timeout occurs.
  - TCP NewReno: a modification of TCP Reno that handles multiple packet losses better. NewReno uses a partial acknowledgment to indicate that some packets have been received after a loss, and retransmits only one lost packet per round trip time. It exits fast recovery when all the packets sent before entering fast recovery have been acknowledged.
  - TCP Vegas: a variant of TCP that uses delay-based congestion detection and avoidance. Vegas measures the actual throughput and the expected throughput of a connection, and adjusts the window size accordingly. If the actual throughput is much lower than the expected throughput, it means that there is congestion and the window size is decreased. If the actual throughput is close to or higher than the expected throughput, it means that there is no congestion and the window size is increased.

### Procedure
- To install NS on a Linux system, follow these steps:
  - Download the NS source code from https://www.isi.edu/nsnam/ns/ns-build.html
  - Extract the tar file to a directory, such as ~/ns-allinone-2.35
  - Change to the directory and run the install script: ./install
  - Set the environment variables for NS and NAM: 
    - export NS_HOME=~/ns-allinone-2.35
    - export PATH=$PATH:$NS_HOME/bin:$NS_HOME/tcl8.5.10/unix:$NS_HOME/tk8.5.10/unix
    - export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$NS_HOME/otcl-1.14:$NS_HOME/lib
  -