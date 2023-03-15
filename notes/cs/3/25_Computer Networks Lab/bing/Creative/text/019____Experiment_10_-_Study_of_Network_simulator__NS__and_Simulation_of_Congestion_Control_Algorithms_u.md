## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a discrete event simulator for network research and education.
- NS can model various network protocols, topologies, traffic patterns, and performance metrics.
- NS is written in C++ and Tcl, and uses an object-oriented approach to design and implement network components.
- NS has a graphical user interface called NAM (Network Animator) that can visualize network simulations and animations.
- NS can simulate various congestion control algorithms, such as TCP, UDP, Reno, NewReno, Vegas, SACK, etc.
- Congestion control algorithms are mechanisms to regulate the flow of data packets in a network and avoid congestion collapse.
- Congestion collapse occurs when the network becomes overloaded and the throughput drops significantly.
- Congestion control algorithms can be classified into two categories: window-based and rate-based.
- Window-based algorithms adjust the size of the sender's window, which is the number of packets that can be sent without receiving an acknowledgment.
- Rate-based algorithms adjust the sending rate of the sender, which is the number of packets that can be sent per unit time.
- Some of the factors that affect the performance of congestion control algorithms are: network bandwidth, delay, packet loss, queue size, etc.
- To simulate congestion control algorithms using NS, the following steps are required:
  - Define the network topology, such as the number and type of nodes, links, and queues.
  - Define the traffic sources and sinks, such as the type and parameters of the application layer protocols.
  - Define the transport layer protocols, such as the type and parameters of the congestion control algorithms.
  - Define the output files and variables, such as the trace files, NAM files, and performance metrics.
  - Run the simulation and analyze the results, such as the throughput, delay, packet loss, etc.