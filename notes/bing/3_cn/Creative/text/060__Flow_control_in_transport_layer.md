### Flow control in transport layer

- Flow control is a mechanism that regulates the amount of data that can be sent and received between two communicating nodes.
- Flow control is needed in transport layer because it provides end-to-end communication services for applications across different networks.
- Flow control in transport layer prevents data loss due to congestion, buffer overflow, or mismatched speeds between the sender and the receiver.
- Flow control in transport layer can be implemented using different techniques, such as:
  - Sliding window: The sender and the receiver maintain a window of acceptable sequence numbers that indicate how much data can be sent or received at a time. The window size can be adjusted dynamically based on the feedback from the receiver or the network conditions.
  - Stop-and-wait: The sender sends one data unit at a time and waits for an acknowledgment from the receiver before sending the next one. This technique is simple but inefficient, as it wastes the bandwidth and introduces delays.
  - Go-back-N: The sender can send multiple data units without waiting for acknowledgments, but it has to keep a copy of each one in case of retransmission. The receiver sends cumulative acknowledgments for the last received data unit in order. If the sender does not receive an acknowledgment within a timeout period, it retransmits all the data units from the last acknowledged one.
  - Selective repeat: The sender can send multiple data units without waiting for acknowledgments, but it only retransmits the ones that are lost or corrupted. The receiver sends selective acknowledgments for each received data unit individually. This technique reduces the number of retransmissions and improves the efficiency.