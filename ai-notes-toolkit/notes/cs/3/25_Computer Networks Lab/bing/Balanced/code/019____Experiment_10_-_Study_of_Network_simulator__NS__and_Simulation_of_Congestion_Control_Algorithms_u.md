## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3   .
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks .
- NS is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- NS is written in C++ and uses Tcl as a scripting language .
- NS provides a modular framework for creating and composing network components, such as nodes, links, queues, protocols, applications, and traffic sources .
- NS also provides a graphical user interface called NAM (Network Animator) for visualizing the simulation results .
- Congestion control algorithms are mechanisms that aim to regulate the amount of data sent by the sources in a network, in order to avoid congestion and ensure fair and efficient use of the network resources.
- Some examples of congestion control algorithms are TCP Reno, TCP NewReno, TCP Vegas, TCP Tahoe, and TCP SACK.
- Each congestion control algorithm has its own characteristics and performance in different network scenarios, such as packet loss, delay, throughput, fairness, and stability.
- NS can be used to simulate and compare different congestion control algorithms, by setting the parameters and variables of the network topology, traffic sources, and protocols.
- The steps to simulate and compare congestion control algorithms using NS are:

  - Install NS on your system, following the instructions from the official website.
  - Create a Tcl script that defines the network topology, traffic sources, protocols, and output files for the simulation.
  - Run the script using the command `ns filename.tcl`.
  - Analyze the output files, such as trace files and NAM files, using tools like awk, gnuplot, xgraph, or NAM.
  - Compare the results of different congestion control algorithms, such as packet loss, delay, throughput, fairness, and stability.