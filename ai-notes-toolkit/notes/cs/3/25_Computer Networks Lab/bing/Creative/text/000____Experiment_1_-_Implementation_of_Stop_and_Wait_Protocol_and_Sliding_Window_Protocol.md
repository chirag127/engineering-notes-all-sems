## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

- Stop and Wait Protocol is a flow control protocol that ensures reliable data transmission over a noiseless channel.
- Sliding Window Protocol is a flow control protocol that allows multiple packets to be sent and received concurrently over a noisy channel.
- Both protocols use sequence numbers and acknowledgments to coordinate the sender and receiver.
- The main difference between the two protocols is the window size, which is the number of packets that can be sent or received without waiting for an acknowledgment.
- In Stop and Wait Protocol, the window size is 1, which means the sender has to wait for an acknowledgment after sending each packet, and the receiver has to send an acknowledgment after receiving each packet.
- In Sliding Window Protocol, the window size can be larger than 1, which means the sender can send multiple packets without waiting for acknowledgments, and the receiver can receive multiple packets without sending acknowledgments for each one.
- The advantage of Sliding Window Protocol over Stop and Wait Protocol is that it can utilize the channel bandwidth more efficiently and achieve higher throughput.
- The disadvantage of Sliding Window Protocol over Stop and Wait Protocol is that it is more complex to implement and requires more buffer space at the sender and receiver.