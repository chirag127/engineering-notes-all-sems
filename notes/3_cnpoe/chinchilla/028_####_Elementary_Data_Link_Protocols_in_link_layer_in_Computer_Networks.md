#### Elementary Data Link Protocols in Link Layer in Computer Networks

The Link Layer is the second layer of the OSI model and is responsible for providing reliable data transfer between two adjacent nodes over a physical link. The Data Link Protocols are used to ensure error-free transmission of data between nodes in a network. Elementary Data Link Protocols are the simplest form of Data Link Protocols that are used in low-speed communication links.

Here are some important Elementary Data Link Protocols that are commonly used in computer networks:

1. Stop-and-Wait Protocol:
   - It is a simple and reliable protocol used for communication over a low-speed link.
   - The sender sends one data frame at a time and waits for an acknowledgement from the receiver before sending the next frame.
   - If the sender does not receive an acknowledgement within a specified time, it retransmits the frame.
   - Mnemonic: "Stop and Wait" - The sender stops and waits for an acknowledgement before sending the next frame.

2. Go-Back-N Protocol:
   - It is a protocol used for communication over a high-speed link.
   - The sender sends multiple frames without waiting for an acknowledgement from the receiver.
   - The receiver sends an acknowledgement for the last correctly received frame.
   - If the sender does not receive an acknowledgement for a frame, it retransmits all the frames starting from that frame.
   - Mnemonic: "Go-Back-N" - The sender goes back and retransmits all the frames starting from the lost frame.

3. Selective Repeat Protocol:
   - It is a protocol used for communication over a high-speed link.
   - The sender sends multiple frames without waiting for an acknowledgement from the receiver.
   - The receiver sends an acknowledgement for each correctly received frame.
   - If the sender does not receive an acknowledgement for a frame, it retransmits only that frame.
   - Mnemonic: "Selective Repeat" - The sender selectively repeats only the lost frame.

Advantages of Elementary Data Link Protocols:
- Simple and easy to implement.
- Suitable for low-speed communication links.
- Ensure reliable data transfer between two adjacent nodes.

Disadvantages of Elementary Data Link Protocols:
- Inefficient for high-speed communication links.
- Wasteful of bandwidth as it waits for acknowledgement before sending the next frame.
- Not suitable for large networks.

Examples of Elementary Data Link Protocols:
- HDLC (High-Level Data Link Control)
- PPP (Point-to-Point Protocol)
- SLIP (Serial Line Internet Protocol)

Applications of Elementary Data Link Protocols:
- Used in low-speed communication links such as dial-up modems, serial ports, and wireless networks.
- Used in embedded systems and IoT devices that require simple and reliable communication protocols.