### Experiment 1.1 - Implementation of Stop and Wait Protocol

Stop and Wait Protocol is a simple flow control protocol that is used in data communication to ensure reliable transmission of data between two devices. In this experiment, we will learn about the implementation of Stop and Wait Protocol.

#### Steps involved in the implementation of Stop and Wait Protocol

1. The sender divides the message into packets of fixed size.

2. The sender sends the first packet to the receiver and waits for an acknowledgment (ACK) from the receiver.

3. Once the receiver receives the packet, it sends an ACK to the sender.

4. The sender waits for the ACK before sending the next packet.

5. If the sender does not receive the ACK within a certain time period, it assumes that the packet was lost and retransmits the packet.

6. Once the receiver receives all the packets, it sends a final ACK to the sender to confirm the successful transmission of the message.

#### Advantages of Stop and Wait Protocol

1. It is a simple and easy-to-implement protocol.

2. It ensures reliable transmission of data.

3. It does not require any additional hardware.

4. It can be used for both synchronous and asynchronous communication.

#### Disadvantages of Stop and Wait Protocol

1. It is not suitable for high-speed networks.

2. It can cause delays in the transmission of data.

3. It can result in lower throughput due to the waiting time for ACK.

#### Example of Stop and Wait Protocol

Consider an example where a sender wants to send a message of 1000 bytes to a receiver using Stop and Wait Protocol. The sender divides the message into packets of 100 bytes each. The sender sends the first packet to the receiver and waits for an ACK from the receiver. Once the receiver receives the packet, it sends an ACK to the sender. The sender waits for the ACK before sending the next packet. If the sender does not receive the ACK within a certain time period, it assumes that the packet was lost and retransmits the packet. Once the receiver receives all the packets, it sends a final ACK to the sender to confirm the successful transmission of the message.

#### Applications of Stop and Wait Protocol

1. It is used in low-speed networks where reliability is more important than speed.

2. It is used in satellite communication.

3. It is used in wireless communication where the signal strength varies.

In conclusion, Stop and Wait Protocol is a reliable flow control protocol that is easy to implement. It ensures the successful transmission of data between two devices.