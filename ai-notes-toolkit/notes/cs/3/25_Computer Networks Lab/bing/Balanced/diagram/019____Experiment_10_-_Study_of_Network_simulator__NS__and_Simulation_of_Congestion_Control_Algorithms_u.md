## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3  .
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks .
- NS is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- NS is written in C++ and uses Tcl as a scripting language .
- NS provides a modular library of network components and models, such as nodes, links, queues, protocols, applications, etc .
- NS allows users to create and run network simulations using a graphical user interface (GUI) or a command-line interface (CLI) .
- NS can also be integrated with other tools, such as network animator (NAM), Xgraph, Gnuplot, etc., for visualization and analysis of simulation results .

- Congestion control algorithms are mechanisms that aim to regulate the amount of traffic sent into a network, in order to avoid congestion and improve network performance.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted.
- End-to-end congestion control algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources, such as TCP.
- Network-assisted congestion control algorithms involve the cooperation of the network devices, such as routers, to signal the sources about the network conditions, such as Explicit Congestion Notification (ECN).
- Congestion control algorithms can also be designed for different types of networks, such as wired, wireless, or satellite networks, with different characteristics and challenges.
- Congestion control algorithms can be evaluated using various metrics, such as throughput, delay, packet loss, fairness, etc.

- Simulation of congestion control algorithms using NS involves the following steps:
  - Install and configure NS on your system.
  - Create a network topology using NS components and models, such as nodes, links, queues, etc.
  - Specify the traffic sources and sinks, such as TCP, UDP, FTP, etc., and assign them to the nodes.
  - Choose the congestion control algorithm to be simulated, such as TCP Reno, TCP Vegas, TCP NewReno, etc., and set the parameters accordingly.
  - Run the simulation using the NS command ns or the GUI tool NsTclsh.
  - Collect and analyze the simulation results using NS tools, such as NAM, Xgraph, Gnuplot, etc., or external tools, such as Excel, Matlab, etc.
  - Compare and contrast the performance of different congestion control algorithms using the metrics mentioned above.