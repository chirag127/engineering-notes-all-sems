### Window management in transport layer

Window management is a flow control mechanism used in the transport layer of the OSI model. It is used to control the amount of data that can be sent by a sender before receiving an acknowledgment from the receiver. This mechanism helps to prevent network congestion and ensures reliable data transmission.

- The sender maintains a sending window, which is the maximum amount of data that can be sent without receiving an acknowledgment from the receiver.
- The receiver maintains a receiving window, which is the maximum amount of data that can be received before sending an acknowledgment to the sender.
- The size of the sending and receiving windows can be adjusted dynamically based on network conditions.
- The sender can only send data within the sending window and must wait for an acknowledgment from the receiver before sending more data.
- The receiver can only receive data within the receiving window and must send an acknowledgment to the sender before receiving more data.

Advantages of window management:
- It helps to prevent network congestion by controlling the amount of data that can be sent by the sender.
- It ensures reliable data transmission by requiring the sender to wait for an acknowledgment from the receiver before sending more data.
- It allows for dynamic adjustment of the window size based on network conditions, which can improve the efficiency of data transmission.

Disadvantages of window management:
- It can add complexity to the transport layer protocol.
- It can increase the latency of data transmission if the window size is too small.

Example of window management:
- The Transmission Control Protocol (TCP) uses window management as part of its flow control mechanism. The sender and receiver negotiate the initial window size during the connection establishment phase, and the window size is adjusted dynamically during data transmission based on network conditions.

Mnemonic for remembering the concept of window management:
- **W**indow management **I**s **N**ecessary to **D**ecrease **O**verflow of data and **W**ait for **A**cknowledgment before **S**ending more data. (WINDOW WAS)