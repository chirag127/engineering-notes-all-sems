# Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

## Aim
To study the basic concepts and features of network simulator (NS) and to simulate the congestion control algorithms using NS.

## Theory
- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3. All are discrete-event computer network simulators, primarily used in research and teaching.
- NS simulates the behavior of networks and protocols by using a scripting language called Tcl (Tool Command Language). NS can simulate various types of networks, such as wired, wireless, satellite, and mobile networks.
- NS can also simulate various network components, such as nodes, links, queues, routers, applications, and transport protocols. NS provides a modular and extensible architecture that allows users to create and modify network models.
- Congestion control algorithms are mechanisms that aim to regulate the traffic flow in a network and prevent congestion. Congestion occurs when the network resources, such as bandwidth or buffer space, are insufficient to meet the demand of the traffic.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted. End-to-end algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources. Network-assisted algorithms involve the cooperation of the network devices, such as routers, to signal the sources about the network conditions.
- Some examples of congestion control algorithms are: TCP, which uses end-to-end feedback based on packet loss and round-trip time; RED (Random Early Detection), which uses network-assisted feedback based on queue length; and ECN (Explicit Congestion Notification), which uses network-assisted feedback based on packet marking.

## Procedure
- To install NS on a Linux system, follow the steps given in the official website or use the package manager of your distribution.
- To run a simulation using NS, create a Tcl script that defines the network topology, the traffic sources, the simulation parameters, and the output files.
- To execute the script, use the command `ns <script_name>.tcl` in the terminal.
- To analyze the results of the simulation, use tools such as NAM (Network Animator), Xgraph, or Gnuplot to visualize the network behavior and the performance metrics.
- To simulate the congestion control algorithms using NS, refer to the examples given in the NS documentation or the online tutorials. Modify the script according to your requirements and observe the effects of different parameters and scenarios on the network performance.