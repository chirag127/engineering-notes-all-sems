### Experiment 1.2 - Implementation of Sliding Window Protocol

The Sliding Window Protocol is a widely used protocol for reliable data transfer in computer networks. It allows the sender to transmit multiple packets at a time without waiting for an acknowledgment from the receiver after each packet. In this experiment, we will learn how to implement the Sliding Window Protocol and analyze its performance.

#### Objectives:

- To implement the Sliding Window Protocol for reliable data transfer.
- To analyze the performance of the Sliding Window Protocol under different network conditions.

#### Equipment Required:

- Two computers connected via a network.
- Python programming environment installed on both computers.

#### Procedure:

1. Open the Python programming environment on both computers.
2. Write the code for the sender and receiver programs using the Sliding Window Protocol.
3. The sender program should divide the data into packets and send them to the receiver using the Sliding Window Protocol.
4. The receiver program should receive the packets and send an acknowledgment for each packet received.
5. The sender program should keep track of the acknowledgments received and adjust the size of the sliding window accordingly.
6. Test the implementation by varying the network conditions such as bandwidth and delay.
7. Record the performance of the Sliding Window Protocol under different network conditions.

#### Results:

After implementing the Sliding Window Protocol, we observed that:

- The Sliding Window Protocol allows the sender to transmit multiple packets at a time without waiting for an acknowledgment from the receiver after each packet.
- The performance of the Sliding Window Protocol is affected by the network conditions such as bandwidth and delay.
- Increasing the bandwidth improves the performance of the Sliding Window Protocol.
- Increasing the delay decreases the performance of the Sliding Window Protocol.
- The Sliding Window Protocol can handle packet loss and retransmit the lost packets.

#### Conclusion:

The Sliding Window Protocol is a reliable protocol for data transfer in computer networks. It allows the sender to transmit multiple packets at a time without waiting for an acknowledgment from the receiver after each packet. The performance of the Sliding Window Protocol is affected by the network conditions such as bandwidth and delay. By implementing and testing the Sliding Window Protocol, we can analyze its performance under different network conditions and optimize it accordingly.