 Here is the content written in markdown format for the topic ### Experiment 1.1 - Implementation of Stop and Wait Protocol:

### Experiment 1.1 - Implementation of Stop and Wait Protocol

- Stop and Wait is a simple flow control protocol used in data link layer.
- In Stop and Wait, sender sends one frame and waits for acknowledgement (ACK) from receiver before sending next frame.
- If ACK is not received within specified time, sender retransmits the same frame.
- This process continues until all frames are transmitted successfully.
- Pseudo code for sender:

Send frame
Start timer
Wait for ACK
If ACK received:
Stop timer
Send next frame
Else if timer expires:
Resend last frame

- Pseudo code for receiver:

Receive frame
Send ACK
Pass data to upper layer

- Advantages: Simple to implement. Easy to understand.
- Disadvantages: Low bandwidth utilization. Lots of delays.
- Example: When you send an email, you wait for confirmation from recipient before sending next email.
- Application: Used in slow speed networks where propagation delay is significant. Not suitable for high speed networks.

[Detailed diagrams and codes can be added here to explain the protocol in a more visual and programming oriented manner for better understanding.]

[Additional points on advantages, disadvantages, examples and applications of Stop and Wait protocol can be added for more comprehensive learning and reference material.]