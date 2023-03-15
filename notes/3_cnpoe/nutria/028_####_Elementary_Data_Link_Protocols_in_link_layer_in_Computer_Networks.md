
### Elementary Data Link Protocols in Link Layer in Computer Networks

- **Data Link Layer** is the second layer in the OSI model and is responsible for the reliable transfer of data frames between two nodes connected by a physical layer.
- **Elementary Data Link Protocols** are the protocols that are used at the data link layer to provide reliable transmission of frames between two nodes.
- **Stop-and-Wait Protocol** is the simplest and most widely used data link protocol. It works by sending one frame at a time, and the sender waits for an acknowledgement from the receiver before sending the next frame.
- **Sliding Window Protocol** is an advanced data link protocol that allows for greater throughput than the Stop-and-Wait protocol. It works by sending multiple frames at a time, and the sender keeps track of the frames that have been acknowledged by the receiver.
- **Go-Back-N Protocol** is a variation of the Sliding Window protocol. It works by sending multiple frames at a time, and the sender keeps track of the frames that have been acknowledged by the receiver. If a frame is lost or corrupted, the sender will resend all the frames that have not been acknowledged.
- **Selective Repeat Protocol** is another variation of the Sliding Window protocol. It works by sending multiple frames at a time, and the sender keeps track of the frames that have been acknowledged by the receiver. If a frame is lost or corrupted, only that frame will be resent.
- **Flow Control** is an important part of data link protocols. It is used to ensure that data is not sent faster than the receiver can process it.
- **Error Detection and Correction** is also an important part of data link protocols. It is used to detect and correct errors in the data that is being transmitted.
- **Mnemonics** and learning tricks can be used to help remember the different types of data link protocols. For example, "Stop-and-Wait" can be remembered as "Stop and Wait for Acknowledgement".