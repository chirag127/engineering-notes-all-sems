 Here is the content in markdown format for the given topic:

## Experiment 10 - Study of Network simulator (NS).and Simulation of Congestion Control Algorithms using NS

Network Simulator (NS) is a discrete event network simulator which is an open source network simulator targetted for simulating TCP/IP networks. It is primarily used for research and educational purposes to simulate the working of networking protocols and network devices.

Some key points about NS are:

- It is an Object Oriented simulator written in C++ and OTcl.
- It provides support for simulating a variety of networking protocols like TCP, UDP, FTP, etc. and network devices like routers, switches, access points, etc.
- It allows integration of different network modules and addition of new protocols.
- It outputs data in the form of traces and graphs for analysis.

In this experiment, we will study the working of NS and simulate the working of some congestion control algorithms like TCP Tahoe, Reno, New Reno, etc. The key steps involved are:

1. Install NS on your system. NS 2 or NS 3 can be installed depending on your requirements. NS 3 has better graphics and animation capabilities.
2. Learn the basics of OTcl which is used to create NS scripts. Some basic OTcl commands to know are - set, $ns_ at 0.0 "$tcp1ctl window 4000", $ns at 30.0 "finish", etc.
3. Understand the tcl/lib folder which contains files for the various protocols and devices. The specific protocol files to modify for congestion control algorithm simulation would be tcp.tcl and tcp-sink.tcl.
4. Code the NS script to create the required network topology, set protocols like TCP congestion control algorithm to use, set performance metrics to monitor, etc. and run the simulations.
5. Analyze the output traces and graphs to understand the congestion control dynamics like window size changes, packet loss, throughput, etc. Vary parameters and compare different congestion control algorithms.

Thus, NS can be effectively used to simulate and study the working of networking protocols and algorithms. It is a very useful tool for researchers and students to learn, experiment and analyze networking concepts.