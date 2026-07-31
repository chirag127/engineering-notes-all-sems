## Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

- Network simulator (NS) is a discrete event simulator that can be used to model and analyze the performance of various network protocols and architectures.
- NS is written in C++ and Tcl (Tool Command Language), and provides a modular framework for creating and configuring network components such as nodes, links, queues, agents, applications, etc.
- NS supports various network technologies such as wired, wireless, satellite, mobile, ad hoc, sensor, optical, etc., and can simulate different aspects of network behavior such as routing, congestion control, traffic generation, error models, etc.
- NS also provides graphical tools for visualizing and animating the network simulation, such as NAM (Network Animator) and Xgraph.
- Congestion control algorithms are mechanisms that aim to regulate the flow of packets in a network, in order to avoid congestion and ensure fair and efficient utilization of network resources.
- Congestion occurs when the demand for network bandwidth exceeds the available capacity, resulting in packet loss, delay, and reduced throughput.
- Congestion control algorithms can be classified into two categories: end-to-end and network-assisted.
- End-to-end congestion control algorithms rely on the feedback from the receivers or the network to adjust the sending rate of the sources, such as TCP (Transmission Control Protocol), which uses acknowledgments and timeouts to detect and recover from packet loss.
- Network-assisted congestion control algorithms involve the cooperation of the network routers or switches to monitor and regulate the traffic flow, such as RED (Random Early Detection), which uses queue length and packet drop probability to signal congestion to the sources.
- NS can be used to simulate and compare the performance of different congestion control algorithms, by varying the network parameters such as link capacity, propagation delay, buffer size, packet size, number of sources, etc., and measuring the metrics such as throughput, delay, packet loss, fairness, etc.