## Experiment 1 - Implementation of Stop and Wait Protocol and Sliding Window Protocol

### Stop and Wait Protocol
- Stop and Wait Protocol is a flow control protocol.
- It is used in data communication to prevent the sender from overwhelming the receiver with data.
- In this protocol, the sender sends one frame at a time and waits for an acknowledgment from the receiver before sending the next frame.
- If the sender does not receive an acknowledgment within a certain time period, it assumes that the frame was lost and retransmits it.

### Sliding Window Protocol
- Sliding Window Protocol is another flow control protocol.
- It is an improvement over the Stop and Wait Protocol as it allows the sender to send multiple frames before waiting for an acknowledgment.
- The sender maintains a window of frames that it can send without waiting for an acknowledgment.
- The size of the window determines the number of frames that can be sent at a time.
- The receiver also maintains a window of frames that it can receive.
- The receiver sends an acknowledgment for the frames it has received and the sender slides its window to send the next set of frames.

These protocols are used to ensure reliable data transmission in communication networks. They are implemented at the data link layer of the OSI model. They are important concepts to understand for anyone studying computer networks or data communication.