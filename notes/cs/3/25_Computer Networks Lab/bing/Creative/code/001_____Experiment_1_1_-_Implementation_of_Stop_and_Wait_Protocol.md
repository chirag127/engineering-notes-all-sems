### Experiment 1.1 - Implementation of Stop and Wait Protocol

- Stop and wait protocol is a simple and reliable data link layer protocol for reliable and sequential delivery of frames between two nodes.
- It works by sending one frame at a time and waiting for an acknowledgment from the receiver before sending the next frame.
- The sender maintains a timer for each frame and retransmits the frame if the timer expires before receiving the acknowledgment.
- The receiver sends an acknowledgment for each frame it receives and discards any duplicate frames.
- The protocol uses a one-bit sequence number to distinguish between new and retransmitted frames.
- The protocol can handle errors and losses in the transmission channel, but it has a low efficiency and throughput due to the long waiting time.

The following steps describe the implementation of stop and wait protocol using Python:

1. Import the socket and threading modules to create and manage sockets and threads.
2. Define the sender and receiver IP addresses and port numbers.
3. Create a sender socket and bind it to the sender address and port.
4. Create a receiver socket and bind it to the receiver address and port.
5. Define a function to generate frames with a sequence number and a payload.
6. Define a function to send frames from the sender socket to the receiver socket using UDP.
7. Define a function to receive frames from the receiver socket and send acknowledgments to the sender socket using UDP.
8. Define a function to simulate errors and losses in the transmission channel by randomly dropping some frames and acknowledgments.
9. Create a sender thread and a receiver thread and start them.
10. In the sender thread, loop through a list of payloads and call the send function for each payload.
11. In the receiver thread, loop indefinitely and call the receive function for each incoming frame.
12. In the send function, generate a frame with the current sequence number and the payload, and send it to the receiver socket.
13. Start a timer for the frame and wait for an acknowledgment from the receiver socket.
14. If the acknowledgment matches the sequence number, stop the timer and increment the sequence number.
15. If the timer expires or the acknowledgment does not match the sequence number, resend the frame and restart the timer.
16. In the receive function, receive a frame from the sender socket and check the sequence number.
17. If the sequence number matches the expected sequence number, print the payload and send an acknowledgment to the sender socket.
18. If the sequence number does not match the expected sequence number, discard the frame and resend the previous acknowledgment to the sender socket.
19. In the error function, randomly drop some frames and acknowledgments by returning False instead of True.
20. In the main function, create and join the sender and receiver threads.