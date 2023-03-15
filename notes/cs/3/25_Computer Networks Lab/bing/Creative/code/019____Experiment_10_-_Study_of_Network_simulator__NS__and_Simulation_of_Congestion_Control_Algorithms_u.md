# Experiment 10 - Study of Network simulator (NS) and Simulation of Congestion Control Algorithms using NS

## Introduction

- Network simulator (NS) is a name for a series of discrete event network simulators, specifically ns-1, ns-2, and ns-3.
- NS is used for simulation of TCP, routing, and multicast protocols over wired and wireless (local and satellite) networks.
- NS-3 is the latest and most widely used version of NS, which is free, open-source software, licensed under the GNU GPLv2 license, and maintained by a worldwide community.
- Congestion control is a mechanism that controls the entry of data packets into the network, enabling a better use of a shared network infrastructure and avoiding congestive collapse.
- Congestion control algorithms use packet losses and delays as signals to infer congestion and decide how fast to send data.
- TCP congestion control is one of the most important and widely studied congestion control algorithms, which maintains a congestion window (CWND) that determines the number of bytes that can be sent out at any time.

## Objectives

- To learn the basics of NS-3 and how to install and run it on a Linux system.
- To understand the concept and working of congestion control algorithms in TCP.
- To simulate and compare the performance of different TCP congestion control algorithms using NS-3.

## Procedure

- Install NS-3 on a Linux system by following the instructions given at https://www.nsnam.org/wiki/Installation.
- Create a simple network topology consisting of two nodes (sender and receiver) connected by a point-to-point link with a specified bandwidth and delay.
- Configure the TCP socket on the sender node to use a specific congestion control algorithm, such as NewReno, Cubic, or BBR.
- Configure the application layer on the sender node to generate a constant bit rate (CBR) traffic with a specified rate and packet size.
- Configure the application layer on the receiver node to receive and acknowledge the packets sent by the sender.
- Configure the tracing and logging mechanisms to record the packet events, such as transmission, reception, drop, delay, etc.
- Run the simulation for a specified duration and collect the trace and log files.
- Analyze the trace and log files using tools such as Gnuplot, Wireshark, or Python to plot the graphs of throughput, delay, congestion window, packet loss, etc.
- Repeat the simulation with different congestion control algorithms, traffic rates, and network parameters and compare the results.