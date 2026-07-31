### Experiment 1.1 - Implementation of Stop and Wait Protocol

The Stop and Wait Protocol is a simple flow control protocol that is used in data communication. Through this experiment, you will learn about the implementation of the Stop and Wait Protocol. Here are the steps involved in implementing the protocol:

1. Set up the sender and receiver: You will need two computers, one acting as the sender and the other as the receiver. Connect them using a reliable data transfer medium.

2. Create the data packets: The data that needs to be sent over the network should be divided into packets of equal size. Each packet should have a unique sequence number.

3. Send the packets: The sender sends the packets to the receiver one at a time. After sending each packet, the sender waits for an acknowledgement from the receiver.

4. Receive the packets: The receiver receives the packet and sends an acknowledgment back to the sender indicating that the packet has been received.

5. Resend the packet: If the sender does not receive an acknowledgement from the receiver, it will resend the packet. The sender will continue to resend the packet until it receives an acknowledgement.

6. Handle errors: If there are errors in the packet, the receiver will not send an acknowledgement. The sender will timeout and resend the packet until it receives an acknowledgement.

7. Terminate the connection: Once all the packets have been sent and received, the sender and receiver will terminate the connection.

Through this experiment, you will gain a better understanding of the Stop and Wait Protocol and its implementation.