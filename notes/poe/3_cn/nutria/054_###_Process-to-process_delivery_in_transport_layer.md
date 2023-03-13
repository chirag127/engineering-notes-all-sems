
### Process-to-process Delivery in Transport Layer

Process-to-process delivery is a type of data transmission in the transport layer of the OSI model. It is used to ensure that data is delivered from the source process to the destination process.

**Mnemonic:** P2P delivery

**Advantages:** 
- Ensures reliable data transfer by providing error detection and correction. 
- Provides flow control to prevent the receiver from being overwhelmed by the sender.
- Provides congestion control to prevent network congestion.

**Disadvantages:** 
- Slower than other types of data transmission, such as datagram delivery.
- More complex to implement than other types of data transmission.

**Applications:** 
- File transfer 
- VoIP 
- Video streaming 

**Example:** 
Consider a file transfer between two computers. The source computer sends the file to the destination computer using process-to-process delivery. The source computer breaks the file into packets, adds error detection and correction information to each packet, and sends the packets to the destination computer. The destination computer then checks the packets for errors, reassembles the packets into the original file, and sends an acknowledgement to the source computer.

**Learning Tricks:** 
- Remember that process-to-process delivery is used to ensure reliable data transfer. 
- Think of a file transfer as an example of process-to-process delivery. 
- Remember that process-to-process delivery is slower than other types of data transmission.