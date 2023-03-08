 Here is the content in markdown format:

### Sliding Window protocols in link layer in Computer Networks

- Sliding window protocols are used for flow control and congestion control in data link layer.
- The sender and receiver maintain a window which is basically a range of sequence numbers of frames which can be sent or received respectively without acknowledgement.
- The size of the window is the maximum number of frames that can be sent or received at a time.
- The window 'slides' as acknowledgements are received for frames sent or when frames are sent from the window.
- Two types of sliding window protocols:
	- Go-Back-N (GBN) protocol: The sender can send N frames before receiving acknowledgement. If acknowledgement is not received for a frame, all N frames are retransmitted.
	- Selective Repeat (SR) protocol: The sender can send N frames before receiving acknowledgement. If acknowledgement is not received for a particular frame, only that frame is retransmitted instead of all N frames.
	- SR protocol is more efficient than GBN protocol due to less retransmissions.
- Example: Consider a window size of 4 frames.
	- In GBN, if acknowledgement is not received for 3rd frame, frames 3, 4, 5, 6 are retransmitted.
	- In SR, only 3rd frame is retransmitted if its acknowledgement is not received.
- Use cases: Used in data link layer protocols like HDLC, Ethernet, etc. Provides reliability and flow control.

[Detailed diagrams and examples can be added if required.]