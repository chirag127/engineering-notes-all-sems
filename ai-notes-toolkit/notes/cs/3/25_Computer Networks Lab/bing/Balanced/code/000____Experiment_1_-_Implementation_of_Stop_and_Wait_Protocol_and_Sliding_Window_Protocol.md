## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

Stop and wait protocol is a flow control protocol that is used for transmitting data over noiseless channels. It provides unidirectional data transmission, which means that either sending or receiving of data will take place at a time. It is a special category of sliding window protocol where the window size is 1. It requires only two sequence numbers, 0 and 1, to distinguish between the packets. It is also known as stop and wait ARQ (automatic repeat request), which means that the sender will retransmit the packet if it does not receive an acknowledgment from the receiver within a certain time.

Sliding window protocol is a flow control protocol that is used for transmitting data over noisy channels. It provides bidirectional data transmission, which means that both sending and receiving of data can take place simultaneously. It is a general category of protocols that use a window size greater than 1 to allow multiple packets to be sent and received without waiting for acknowledgments. It uses a larger range of sequence numbers to identify the packets. It is also known as sliding window ARQ, which means that the sender will retransmit the packets that are not acknowledged by the receiver within a certain time.

The main objectives of this experiment are:

- To understand the concepts and working of stop and wait protocol and sliding window protocol.
- To implement the stop and wait protocol and sliding window protocol using a programming language such as C, Java, or Python.
- To compare the performance and efficiency of stop and wait protocol and sliding window protocol in terms of throughput, delay, and error handling.