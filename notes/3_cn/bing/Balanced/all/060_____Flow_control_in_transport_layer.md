### Flow control in transport layer

- Flow control is a mechanism that regulates the rate of data transmission between a sender and a receiver.
- Flow control ensures that the sender does not overwhelm the receiver with more data than it can process or store.
- Flow control is implemented by using feedback messages from the receiver to the sender, indicating how much data the receiver can accept at a given time.
- Flow control can be classified into two types: stop-and-wait and sliding window.

#### Stop-and-wait flow control

- In stop-and-wait flow control, the sender sends one data unit (such as a packet or a frame) and waits for an acknowledgment from the receiver before sending the next data unit.
- The sender can only have one unacknowledged data unit in transit at any time.
- The receiver sends an acknowledgment after receiving and processing each data unit.
- The acknowledgment can also include a request to stop sending data if the receiver's buffer is full or a request to resume sending data if the receiver's buffer has space.
- Stop-and-wait flow control is simple and reliable, but it has low efficiency and high latency, especially for long-distance or noisy channels.

#### Sliding window flow control

- In sliding window flow control, the sender can send multiple data units without waiting for acknowledgments, as long as the number of unacknowledged data units does not exceed a certain limit, called the window size.
- The window size is determined by the receiver's buffer capacity and the channel's bandwidth-delay product (the product of the channel's bandwidth and the round-trip time between the sender and the receiver).
- The sender maintains a sending window, which is a range of sequence numbers of the data units that can be sent or have been sent but not yet acknowledged.
- The receiver maintains a receiving window, which is a range of sequence numbers of the data units that can be accepted or have been accepted but not yet delivered to the application layer.
- The receiver sends acknowledgments for the data units it receives, and also indicates the current window size or the next expected sequence number.
- The sender slides its window forward when it receives an acknowledgment, and the receiver slides its window forward when it delivers a data unit to the application layer.
- Sliding window flow control can be further divided into two subtypes: go-back-N and selective repeat.

##### Go-back-N sliding window flow control

- In go-back-N sliding window flow control, the sender can send up to N data units without waiting for acknowledgments, where N is the window size.
- The receiver only sends cumulative acknowledgments, which acknowledge all the data units up to a certain sequence number.
- The receiver only accepts data units in order, and discards any out-of-order data units.
- If the sender does not receive an acknowledgment for a data unit within a certain time, it assumes that the data unit or its acknowledgment was lost, and retransmits all the data units starting from that sequence number.
- Go-back-N sliding window flow control is simple and easy to implement, but it has low efficiency and high overhead, especially for large window sizes or high error rates.

##### Selective repeat sliding window flow control

- In selective repeat sliding window flow control, the sender can send up to N data units without waiting for acknowledgments, where N is the window size.
- The receiver sends individual acknowledgments for each data unit it receives, and also indicates the current window size or the next expected sequence number.
- The receiver can accept data units out of order, and buffers them until they can be delivered in order to the application layer.
- If the sender does not receive an acknowledgment for a data unit within a certain time, it assumes that the data unit or its acknowledgment was lost, and retransmits only that data unit.
- Selective repeat sliding window flow control is more efficient and less wasteful than go-back-N sliding window flow control, but it is more complex and requires more buffer space at the receiver.