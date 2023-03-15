
### Process-to-process delivery in transport layer

* Process-to-process delivery is a reliable transport layer protocol which ensures that messages are delivered in the same order in which they were sent. 
* It provides a connection-oriented service which requires that a connection is established between two processes before data can be exchanged. 
* It also provides an error-checking mechanism to ensure that data is not corrupted in transit.
* The process-to-process delivery protocol is based on the sliding window protocol which uses acknowledgements and timeouts to ensure reliable data transfer. 
* The sender sends a message and waits for an acknowledgement from the receiver. If the acknowledgement is not received within a certain time, the sender retransmits the message. 
* The receiver sends an acknowledgement for each message it receives.
* The process-to-process delivery protocol also provides flow control which prevents the sender from sending too much data at once. 
* The sender and receiver agree on a window size which is the maximum number of messages that can be sent without an acknowledgement. 
* The window size is adjusted dynamically depending on the network conditions.
* The process-to-process delivery protocol also provides congestion control which prevents the sender from sending too much data too quickly. 
* The sender monitors the network conditions and adjusts its transmission rate accordingly. 
* This helps to ensure that the network does not become congested and that data is delivered reliably.
* Mnemonics and learning tricks for process-to-process delivery:
  * P for Process-to-process
  * W for Window size
  * A for Acknowledgement
  * F for Flow control
  * C for Congestion control