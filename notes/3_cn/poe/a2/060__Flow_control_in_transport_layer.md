 Here is the content in markdown format with formal tone and without emojis:

### Flow control in transport layer

1. Flow control is a technique to regulate the transmission of data to prevent overflow. In transport layer, flow control is implemented to prevent the receiving device from being overwhelmed by too much data sent by the sending device.
2. The receiving device has a fixed buffer size. If data is received faster than it can be processed, the buffer may overflow resulting in loss of data. Flow control mechanisms help avoid this situation by controlling the transmission rate.
3. The most commonly used flow control mechanisms are:
 - Sliding window protocol: The sending device is allowed to send only a fixed number of frames before waiting for an acknowledgement from the receiving device. The window size determines how many frames can be sent at a time.
 - Credit-based flow control: The receiving device sets a limit on the number of bytes that can be received, known as credit. The sending device can only send data if it has credits available. As the receiver processes data, it releases credits back to the sender.
4. Flow control is implemented using feedback messages from the receiver to the sender conveying information about its buffer occupancy. The sender can then adjust its transmission rate accordingly to prevent overflow. Effective flow control mechanisms allow for efficient utilization of the network bandwidth while avoiding congestion.

How's that? I have written the content in points in a formal tone without emojis and external links as instructed. Please let me know if you would like me to modify or add anything.