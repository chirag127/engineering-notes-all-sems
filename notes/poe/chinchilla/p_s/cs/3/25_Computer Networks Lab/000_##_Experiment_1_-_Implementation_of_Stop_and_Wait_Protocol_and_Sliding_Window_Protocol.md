## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

In this experiment, we will study the two widely used protocols in data communication, Stop and Wait Protocol and Sliding Window Protocol. These protocols are used to ensure reliable data transfer between two devices over a communication channel.

### Stop and Wait Protocol

Stop and Wait Protocol is a simple protocol that is used for reliable data transfer between two devices over a communication channel. In this protocol, the sender sends one packet of data and waits for an acknowledgement from the receiver. If the acknowledgement is received, the sender sends the next packet, and if the acknowledgement is not received, the sender retransmits the same packet.

#### Advantages of Stop and Wait Protocol

- Simple to implement
- Ensures reliable data transfer
- Suitable for communication channels with low error rates

#### Disadvantages of Stop and Wait Protocol

- Inefficient for communication channels with high error rates
- Low bandwidth utilization
- High latency

#### Example of Stop and Wait Protocol

Below is an example of Stop and Wait Protocol:

```
Sender                 Receiver
------                 --------
Send Packet 1
                        Receive Packet 1
Send ACK 1
Send Packet 2
                        Receive Packet 2
Send ACK 2
Send Packet 3
                        Receive Packet 3
Send ACK 3
```

### Sliding Window Protocol

Sliding Window Protocol is a protocol that is used for reliable data transfer between two devices over a communication channel. In this protocol, the sender sends multiple packets of data without waiting for an acknowledgement from the receiver. The receiver sends an acknowledgement for the packets that are received successfully. The sender maintains a window of packets that can be sent without waiting for an acknowledgement.

#### Advantages of Sliding Window Protocol

- Efficient for communication channels with high error rates
- High bandwidth utilization
- Low latency

#### Disadvantages of Sliding Window Protocol

- Complex to implement
- Requires more memory to maintain the window
- Not suitable for communication channels with low error rates

#### Example of Sliding Window Protocol

Below is an example of Sliding Window Protocol:

```
Sender                 Receiver
------                 --------
Send Packets 1-4
                        Receive Packets 1-4
Send ACK 1-4
Send Packets 5-8
                        Receive Packets 5-8
Send ACK 5-8
Send Packets 9-12
                        Receive Packets 9-12
Send ACK 9-12
```

### Applications of Stop and Wait Protocol and Sliding Window Protocol

Stop and Wait Protocol and Sliding Window Protocol are widely used in various applications such as:

- File transfer protocols such as FTP and TFTP
- Email protocols such as SMTP and POP
- Web protocols such as HTTP and HTTPS

In conclusion, Stop and Wait Protocol and Sliding Window Protocol are two widely used protocols in data communication. These protocols ensure reliable data transfer between two devices over a communication channel. Stop and Wait Protocol is simple to implement and suitable for communication channels with low error rates, while Sliding Window Protocol is efficient for communication channels with high error rates and high bandwidth utilization.