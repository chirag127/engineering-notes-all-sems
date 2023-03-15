#### Sliding Window protocols in link layer in Computer Networks

- The sliding window protocol is a data link layer protocol that is useful in the sequential and reliable delivery of the data frames  .
- Using the sliding window protocol, the sender can send multiple frames at a time before receiving an acknowledgment from the receiver  .
- The sliding window is also used in Transmission Control Protocol (TCP), which operates at the transport layer  .
- The sliding window protocol manages the flow of data between two network nodes to ensure that the receiver can handle the incoming data  .
- The sliding window protocol uses two types of windows: sender window and receiver window .
- The sender window is the set of frames that the sender can send without waiting for an acknowledgment .
- The receiver window is the set of frames that the receiver can accept without sending an acknowledgment .
- The size of the windows can vary depending on the protocol and the network conditions .
- The sliding window protocol can be classified into three types: stop-and-wait, go-back-N, and selective repeat  .
- In stop-and-wait, the sender sends one frame at a time and waits for an acknowledgment before sending the next frame  .
- In go-back-N, the sender can send up to N frames at a time and waits for an acknowledgment for the first frame before sliding the window  .
- In selective repeat, the sender can send up to N frames at a time and waits for an acknowledgment for each frame before sliding the window  .
- The sliding window protocol improves the efficiency and reliability of data transmission by reducing the waiting time and handling the errors and losses  .