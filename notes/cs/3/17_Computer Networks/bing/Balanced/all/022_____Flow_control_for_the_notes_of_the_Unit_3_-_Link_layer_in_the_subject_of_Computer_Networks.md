# Flow control in Data Link Layer

- Flow control is a technique that allows two stations working at different speeds to communicate with each other.
- Flow control regulates the amount of data that a sender can send before it waits for an acknowledgment from the receiver.
- Flow control prevents a fast sender from overwhelming a slow receiver with too many frames or data units.
- Flow control can be implemented at the data link layer using two methods: stop-and-wait and sliding window.
- Stop-and-wait flow control makes the sender send one frame at a time and wait for an acknowledgment from the receiver before sending the next frame.
- Sliding window flow control allows the sender to send multiple frames without waiting for an acknowledgment, but limits the number of frames that can be sent using a window size.
- The window size is the number of frames that can be sent or received at a time.
- The window size can be fixed or variable depending on the protocol.
- Ethernet flow control is an example of flow control at the data link layer using pause frames.
- Pause frames are special frames that are sent by the receiver to the sender to request a temporary halt of data transmission.
- Pause frames are defined by the IEEE standard 802.3x.