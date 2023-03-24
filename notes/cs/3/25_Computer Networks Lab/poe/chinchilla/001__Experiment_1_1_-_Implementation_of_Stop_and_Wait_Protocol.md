### Experiment 1.1 - Implementation of Stop and Wait Protocol

The Stop and Wait Protocol is a simple flow control protocol that ensures the reliable transmission of data between two nodes in a communication system. In this experiment, we will implement the Stop and Wait Protocol and observe its performance under different scenarios.

The objective of this experiment is to understand the following concepts:

1. The basic operation of the Stop and Wait Protocol.
2. The impact of the propagation delay on the performance of the protocol.
3. The effect of increasing the packet size on the performance of the protocol.

#### Equipment Required

1. Two computers connected over a network.
2. Programming language of your choice (Python, Java, C++, etc.).
3. Network simulator software (e.g., NS-3, OMNeT++, etc.).
4. Stopwatch or timer.

#### Experimental Setup

1. Implement the Stop and Wait Protocol in your chosen programming language.
2. Set up a network simulator and connect two computers using a reliable transport layer protocol (e.g., TCP).
3. Configure the network simulator to introduce a delay of varying lengths between the two computers.
4. Configure the network simulator to simulate packet loss and packet corruption.
5. Vary the packet size and observe the impact on the performance of the protocol.

#### Experimental Procedure

1. Start the timer and initiate the transmission of a packet from the sender to the receiver.
2. The sender waits for an acknowledgement (ACK) from the receiver before transmitting the next packet.
3. The receiver sends an ACK upon receiving a packet.
4. If the sender does not receive an ACK within a predetermined timeout period, it retransmits the packet.
5. Record the time taken for the transmission of each packet and the number of retransmissions required.
6. Repeat the experiment for different propagation delay values and packet sizes.
7. Analyze the results and draw conclusions based on the observations.

#### Results

The results of the experiment will provide insights into the performance of the Stop and Wait Protocol under different scenarios. The following observations can be made:

1. As the propagation delay increases, the time taken for the transmission of each packet increases, and the number of retransmissions required also increases.
2. Increasing the packet size reduces the number of packets required to transmit the same amount of data, but it also increases the time taken for the transmission of each packet and the number of retransmissions required.
3. The Stop and Wait Protocol is a simple and reliable protocol for transmitting data over a network, but its performance is affected by the propagation delay and packet size.

#### Conclusion

In this experiment, we implemented the Stop and Wait Protocol and observed its performance under different scenarios. The results of the experiment demonstrate the impact of the propagation delay and packet size on the performance of the protocol. The Stop and Wait Protocol is a simple and reliable protocol for transmitting data over a network, but its performance is affected by the propagation delay and packet size. The results of this experiment can be used to optimize the performance of the protocol for a given network configuration.