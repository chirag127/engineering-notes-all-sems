 Here is the content in markdown format for #### Sliding Window protocols in link layer in Computer Networks:

#### Sliding Window protocols in link layer in Computer Networks

- Sliding Window protocols are used in link layer to enable efficient transmission of packets over a network. They allow sender to transmit multiple packets before receiving acknowledgement (ACK) for the first packet. This increases throughput.
- The window size refers to the number of packets that can be sent before receiving an ACK. The window slides over the packets as ACKs are received.
- Two popular sliding window protocols are:
	- Stop and Wait ARQ: Window size is 1. After sending each packet, sender waits for ACK before sending next packet. Throughput is low.
	- Sliding Window Protocol: Window size is greater than 1. Sender can send multiple packets before receiving ACKs. Throughput is higher than Stop and Wait ARQ.
- Advantages: Higher throughput, efficient use of bandwidth.
- Disadvantages: Buffering and sequence number overhead. Managing out of order delivery and packet loss is complex.
- Examples: TCP uses sliding window protocol.
- Mnemonics: Think of window sliding over packets as ACKs received. Larger window size means more packets in transit resulting in higher throughput.
- Code example:

Sender:
sending_window = 4  # Window size
next_seq_num = 0
# Send packets with sequence numbers 0, 1, 2, 3
# Receive ACK for packet 0
# Slide window: Send packets with sequence numbers 4, 5, 6, 7
# Receive ACKs for packets 1, 2, 3
# Slide window again...

Receiver:
expected_seq_num = 0
# Receive packet with seq num 0, send ACK
# Receive packets with seq nums 1, 2, 3
# Send ACKs for packets 1, 2, 3
# ...

- Applications: Web browsing, file transfer, video streaming, etc.