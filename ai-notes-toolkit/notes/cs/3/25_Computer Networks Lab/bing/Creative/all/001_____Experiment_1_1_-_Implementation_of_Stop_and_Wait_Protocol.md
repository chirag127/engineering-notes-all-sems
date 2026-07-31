# Experiment 1.1 - Implementation of Stop and Wait Protocol

## Objective
The objective of this experiment is to implement the stop and wait protocol, which is a flow control protocol that ensures reliable data transmission over a noiseless channel.

## Theory
- The stop and wait protocol is a data-link layer protocol that uses a half-duplex link between the sender and the receiver. This means that only one direction of data transmission is possible at a time.
- The sender sends one data packet or frame at a time and waits for an acknowledgment (ACK) from the receiver before sending the next packet. The receiver sends an ACK after receiving a packet and checking its validity.
- The sender and the receiver use sequence numbers to identify the packets and avoid duplication. The sequence numbers alternate between 0 and 1, as the window size of the protocol is 1.
- The stop and wait protocol is simple and easy to implement, but it has low efficiency and throughput. The efficiency is the ratio of the useful time to the total cycle time, and the throughput is the rate of data transmission. The efficiency and the throughput depend on the propagation delay, which is the time taken by a packet to travel from the sender to the receiver, and the transmission time, which is the time taken by a packet to be transmitted on the channel.
- The efficiency of the stop and wait protocol is given by:

  `Efficiency = Tt / (Tt + 2Tp)`

  where Tt is the transmission time and Tp is the propagation delay.

  The throughput of the stop and wait protocol is given by:

  `Throughput = L / (Tt + 2Tp)`

  where L is the length of the packet.

## Procedure
- To implement the stop and wait protocol, we need two programs: one for the sender and one for the receiver. We can use any programming language, such as C, Java, Python, etc., to write the programs.
- The sender program should perform the following steps:

  1. Create a socket and bind it to a port number.
  2. Initialize the sequence number to 0 and the buffer to store the data to be sent.
  3. Read the data from a file or the user input and store it in the buffer.
  4. Create a packet with the data and the sequence number and send it to the receiver using the socket.
  5. Start a timer and wait for an ACK from the receiver.
  6. If the ACK is received and matches the sequence number, stop the timer and increment the sequence number. Go to step 3 and repeat until all the data is sent.
  7. If the ACK is not received or does not match the sequence number, resend the packet and restart the timer. Go to step 5 and repeat until the ACK is received or the maximum number of retries is reached.
  8. Close the socket and exit the program.

- The receiver program should perform the following steps:

  1. Create a socket and bind it to a port number.
  2. Initialize the sequence number to 0 and the buffer to store the received data.
  3. Receive a packet from the sender using the socket and check its validity.
  4. If the packet is valid and matches the sequence number, store the data in the buffer and send an ACK with the same sequence number to the sender using the socket. Increment the sequence number.
  5. If the packet is invalid or does not match the sequence number, discard the packet and send a negative acknowledgment (NAK) with the same sequence number to the sender using the socket. Do not increment the sequence number.
  6. Go to step 3 and repeat until all the data is received.
  7. Write the data from the buffer to a file or the user output.
  8. Close the socket and exit the program.

## Results and Observations
- After running the sender and the receiver programs, we can observe the data transmission and the ACK/NAK exchange between them. We can also measure the efficiency and the throughput of the protocol using the formulae given in the theory section.
- We can observe that the stop and wait protocol works correctly for a noiseless channel, but it has low efficiency and throughput due to the waiting time and the overhead of the ACK/NAK packets. We can also observe that the protocol can handle packet loss and duplication by resending the packets and using the sequence numbers.