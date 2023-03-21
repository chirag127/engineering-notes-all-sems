 Here is the content in Markdown format without any emojis or external links as per your instructions:

### Sliding Window protocols for the notes of the Unit 3 - Link layer in the subject of Computer Networks.

1. Sliding Window Protocols are used for flow control and congestion control in data transfer between two hosts.
2. The sender and receiver communicate using sequence and acknowledgement numbers which help in identifying the packets and their order.
3. The sender maintains a sending window which is the number of packets it can send before waiting for an acknowledgement. The receiving window is the number of packets the receiver can buffer before it starts dropping packets.
4. The window size depends on the capacity of the sender and receiver buffers. Larger window size leads to higher throughput but more packets in transit leading to more delay and chances of packet loss.
5. The two main sliding window protocols are:
- Stop and Wait Protocol: Sender can send only one packet and waits for acknowledgement before sending the next packet. Low throughput but no congestion or out of order packets.
- Sliding Window Protocol: Sender can send multiple packets (defined by window size) before waiting for acknowledgements thereby increasing throughput. The window slides over the sequence numbers as packets are sent and acknowledged.

The content aims to highlight the key points about sliding window protocols in a formal tone with points for easy understanding as a part of the study material. Please let me know if you would like me to modify or expand the content.