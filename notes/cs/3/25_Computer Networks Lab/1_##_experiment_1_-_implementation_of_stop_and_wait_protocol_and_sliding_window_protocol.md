## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

Experiment 1: Implementation of Stop and Wait Protocol and Sliding Window Protocol:

The objective of this experiment is to implement and compare the performance of the Stop and Wait Protocol and the Sliding Window Protocol in a computer network.

Stop and Wait Protocol:

The Stop and Wait Protocol is a simple and reliable data transfer protocol that sends one data packet at a time, and waits for an acknowledgment before sending the next packet. The sender sends a data packet, waits for an acknowledgment, and repeats this process until all data has been transferred.

Implementation Steps:

1. Create a sender and receiver program that implements the Stop and Wait Protocol.
2. The sender program sends data packets one at a time to the receiver program.
3. The receiver program sends an acknowledgment back to the sender program after each data packet is received.
4. The sender program waits for the acknowledgment before sending the next data packet.

Sliding Window Protocol:

The Sliding Window Protocol is a data transfer protocol that allows multiple data packets to be sent at the same time, without waiting for an acknowledgment for each packet. The sender maintains a window of unacknowledged data packets, and slides the window forward as packets are acknowledged by the receiver.

Implementation Steps:

1. Create a sender and receiver program that implements the Sliding Window Protocol.
2. The sender program sends multiple data packets at the same time, within the bounds of the window.
3. The receiver program sends an acknowledgment back to the sender program after each data packet is received.
4. The sender program updates the window based on the acknowledgments received from the receiver program.

In conclusion, the objective of this experiment is to implement and compare the performance of the Stop and Wait Protocol and the Sliding Window Protocol in a computer network. The Stop and Wait Protocol sends one data packet at a time, waiting for an acknowledgment before sending the next packet, while the Sliding Window Protocol allows multiple data packets to be sent at the same time, without waiting for an acknowledgment for each packet. The implementation steps for both protocols involve creating sender and receiver programs, sending data packets, and sending and receiving acknowledgments.
