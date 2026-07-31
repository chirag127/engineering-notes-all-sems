### Experiment 1.1 - Implementation of Stop and Wait Protocol

#### Objective
To implement the stop and wait protocol for reliable data transmission over a noiseless channel.

#### Theory
The stop and wait protocol is a flow control protocol where the sender sends one data packet and waits for the acknowledgment from the receiver before sending the next packet. It is a simple and reliable protocol that ensures that no data is lost or duplicated. However, it is inefficient as the sender has to wait for the round trip time (RTT) of each packet, which reduces the throughput.

The stop and wait protocol can be implemented using two sequence numbers, 0 and 1, to distinguish between the packets and the acknowledgments. The sender attaches a sequence number to each packet and expects the receiver to send back an acknowledgment with the same sequence number. If the sender does not receive the acknowledgment within a timeout period, it retransmits the packet. The receiver discards any duplicate packets that it receives.

The stop and wait protocol can handle the following scenarios:

- Normal operation: The sender sends a packet and receives an acknowledgment within the timeout period. The sender then sends the next packet with the alternate sequence number.
- Lost packet: The sender sends a packet but it is lost in the channel. The sender does not receive an acknowledgment within the timeout period and retransmits the packet with the same sequence number. The receiver eventually receives the packet and sends back an acknowledgment.
- Lost acknowledgment: The sender sends a packet and receives an acknowledgment, but the acknowledgment is lost in the channel. The sender does not receive the acknowledgment within the timeout period and retransmits the packet with the same sequence number. The receiver receives the duplicate packet and discards it, but sends back an acknowledgment with the same sequence number. The sender receives the acknowledgment and sends the next packet with the alternate sequence number.

#### Procedure
To implement the stop and wait protocol, the following steps are required:

- Create a sender and a receiver program that can communicate over a socket connection.
- Define the packet and acknowledgment formats, which should include a sequence number, a checksum, and a data field.
- Implement a function to calculate the checksum of a packet or an acknowledgment, which can be used to detect errors.
- Implement a function to generate a random number, which can be used to simulate packet loss or acknowledgment loss.
- Implement the sender logic, which should perform the following tasks:
  - Create a socket and connect to the receiver.
  - Read the data from a file and divide it into packets of fixed size.
  - For each packet, calculate the checksum and attach the sequence number.
  - Send the packet to the receiver and start a timer.
  - Wait for the acknowledgment from the receiver or the timeout event.
  - If the acknowledgment is received and matches the sequence number, stop the timer and send the next packet with the alternate sequence number.
  - If the timeout occurs, retransmit the packet with the same sequence number.
  - Repeat until all the packets are sent and acknowledged.
  - Close the socket and the file.
- Implement the receiver logic, which should perform the following tasks:
  - Create a socket and listen for the sender's connection.
  - Accept the connection and create a file to store the data.
  - For each packet received from the sender, calculate the checksum and verify it with the checksum in the packet.
  - If the checksum is valid and the sequence number is expected, write the data to the file and send back an acknowledgment with the same sequence number.
  - If the checksum is invalid or the sequence number is not expected, discard the packet and send back an acknowledgment with the previous sequence number.
  - Repeat until all the packets are received and acknowledged.
  - Close the socket and the file.
- Run the sender and the receiver programs on different terminals and observe the output.
- Vary the packet loss and acknowledgment loss probabilities and observe the effect on the performance of the protocol.