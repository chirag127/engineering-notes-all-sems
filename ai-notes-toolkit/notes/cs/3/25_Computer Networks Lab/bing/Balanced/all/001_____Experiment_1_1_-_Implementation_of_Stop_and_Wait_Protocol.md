# Experiment 1.1 - Implementation of Stop and Wait Protocol

## Objective
The objective of this experiment is to implement the stop and wait protocol, which is a flow control protocol that ensures reliable data transmission over a noisy channel.

## Theory
- The stop and wait protocol is a data link layer protocol that uses a half-duplex link between the sender and the receiver. This means that only one direction of data transmission is possible at a time.
- The sender sends one data packet at a time and waits for an acknowledgment (ACK) from the receiver before sending the next packet. The receiver sends an ACK after receiving a packet and checking its error detection code.
- The sender and the receiver use sequence numbers to identify the packets and avoid duplication. The sequence numbers alternate between 0 and 1, as only two sequence numbers are required for this protocol.
- The stop and wait protocol can handle three types of errors: lost packets, corrupted packets, and delayed packets. The sender uses a timer to detect lost or delayed packets and retransmits them after the timer expires. The receiver discards corrupted packets or packets with incorrect sequence numbers and sends a negative acknowledgment (NAK) to the sender.
- The efficiency of the stop and wait protocol is low, as the sender has to wait for an ACK before sending the next packet. The efficiency can be calculated as:

`Efficiency = Tt / (Tt + 2Tp)`

where Tt is the transmission time of a packet and Tp is the propagation time of a packet.

## Procedure
- To implement the stop and wait protocol, we need two programs: one for the sender and one for the receiver. The programs can be written in any programming language, such as C, Java, or Python.
- The sender program should perform the following steps:
  - Create a socket and bind it to a port number.
  - Generate a data packet with a sequence number and an error detection code, such as a checksum or a cyclic redundancy check (CRC).
  - Send the data packet to the receiver and start a timer.
  - Wait for an ACK or a NAK from the receiver or until the timer expires.
  - If an ACK is received, increment the sequence number and generate the next data packet.
  - If a NAK is received or the timer expires, retransmit the same data packet.
  - Repeat the steps until all the data packets are sent.
- The receiver program should perform the following steps:
  - Create a socket and bind it to a port number.
  - Listen for incoming data packets from the sender.
  - Receive a data packet and check its error detection code and sequence number.
  - If the data packet is valid and has the expected sequence number, send an ACK to the sender and process the data.
  - If the data packet is invalid or has an unexpected sequence number, send a NAK to the sender and discard the data.
  - Repeat the steps until all the data packets are received.

## Output
- The output of the experiment should show the data packets sent and received by the sender and the receiver, along with their sequence numbers and error detection codes.
- The output should also show the ACKs and NAKs exchanged by the sender and the receiver, and the timer values used by the sender.
- The output should demonstrate the working of the stop and wait protocol in different scenarios, such as normal transmission, lost packets, corrupted packets, and delayed packets.