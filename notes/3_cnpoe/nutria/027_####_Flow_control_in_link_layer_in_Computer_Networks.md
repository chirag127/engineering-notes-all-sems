

### Flow Control in Link Layer in Computer Networks

- Flow control is a mechanism used in the link layer of the OSI model to regulate the amount of data that can be sent between two nodes in a network. 
- It is used to ensure that the receiver does not become overwhelmed with data and can process the data it receives. 
- Flow control is achieved by using a sliding window protocol, which is a type of protocol that uses acknowledgments and window size to control the amount of data that is sent. 
- The sender sends data packets to the receiver and the receiver sends back an acknowledgment (ACK) when it has received the data. 
- The sender keeps track of the acknowledgments it receives and adjusts the window size accordingly. 
- If the sender receives an ACK for all the data it has sent, then it can increase the window size and send more data. 
- If the sender does not receive an ACK for some of the data it has sent, then it will reduce the window size and send less data. 
- This ensures that the receiver is not overwhelmed with data and can process the data it receives.
- Flow control is also used to ensure that the sender does not send more data than the receiver can handle. 
- If the sender sends too much data, then the receiver will not be able to process it and the data will be lost. 
- Flow control helps to ensure that the data is sent at a rate that the receiver can handle.
- Mnemonics and learning tricks for flow control in link layer can be helpful to remember the concept. A popular mnemonic is "SLIDING WINDOW" which stands for Sender, Link Layer, Incoming Data, Acknowledgment, Data, Incoming, Window size, Outgoing Data.