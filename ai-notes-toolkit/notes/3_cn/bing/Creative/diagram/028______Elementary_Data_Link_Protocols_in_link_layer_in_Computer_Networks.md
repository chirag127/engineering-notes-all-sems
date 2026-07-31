#### Elementary Data Link Protocols in link layer in Computer Networks

Elementary data link protocols are designed to perform the basic functions of the data link layer, such as framing, error control and flow control. They are classified into three categories, as given below :

- Protocol 1: Unrestricted simplex protocol
- Protocol 2: Simplex stop and wait protocol
- Protocol 3: Simplex protocol for noisy channels

Let us draw a diagram for each protocol using ASCII characters.

- Protocol 1: Unrestricted simplex protocol

This protocol allows the sender to send data frames continuously without waiting for any feedback from the receiver. The receiver simply accepts and processes the frames. There is no error or flow control in this protocol. The diagram for this protocol is as follows:

```
Sender                          Receiver
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 1
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 2
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 3
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 4
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 5
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
```

- Protocol 2: Simplex stop and wait protocol

This protocol allows the sender to send one frame at a time and wait for an acknowledgment from the receiver before sending the next frame. The receiver sends an acknowledgment after receiving and processing the frame. This protocol provides error control but not flow control. The diagram for this protocol is as follows:

```
Sender                          Receiver
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 1
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
| <---------------------------| ACK 1
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 2
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
| <---------------------------| ACK 2
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 3
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
| <---------------------------| ACK 3
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
```

- Protocol 3: Simplex protocol for noisy channels

This protocol allows the sender to send one frame at a time and wait for a positive acknowledgment from the receiver before sending the next frame. The receiver sends a positive acknowledgment if the frame is received correctly, or a negative acknowledgment if the frame is corrupted or lost. The sender retransmits the frame if it receives a negative acknowledgment or a timeout occurs. This protocol provides both error and flow control. The diagram for this protocol is as follows:

```
Sender                          Receiver
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|---------------------------> | Frame 1
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|                              |
|

```
