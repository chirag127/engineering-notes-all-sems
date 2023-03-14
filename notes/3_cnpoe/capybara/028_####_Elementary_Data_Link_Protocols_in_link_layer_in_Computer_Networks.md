#### Elementary Data Link Protocols in Link Layer in Computer Networks

In computer networks, the data link layer is responsible for transmitting data between two adjacent network nodes. Elementary Data Link Protocols are the simplest protocols used in the data link layer. They are the building blocks of more complex protocols and are widely used in various network technologies.

Here are some important elementary data link protocols:

1. Stop-and-Wait Protocol:
   - This protocol is used for reliable data transmission between two nodes.
   - In this protocol, the sender sends a data packet and waits for an acknowledgement from the receiver.
   - The receiver sends an acknowledgement if the packet is received successfully.
   - If the sender doesn't receive an acknowledgement within a specified time, it retransmits the packet.

2. Go-Back-N Protocol:
   - This protocol is used when multiple packets are sent from the sender to the receiver.
   - The sender sends a fixed number of packets and waits for an acknowledgement from the receiver.
   - If the sender doesn't receive an acknowledgement for a packet, it retransmits all the packets from that point.

3. Selective Repeat Protocol:
   - This protocol is similar to the Go-Back-N protocol but differs in retransmission.
   - In this protocol, only the lost packets are retransmitted, not all the packets from that point.

Mnemonics and Tricks:

1. Stop-and-Wait Protocol: Imagine a person in a race who stops after running a certain distance and waits for the acknowledgement from the judge before running again.

2. Go-Back-N Protocol: Imagine a person carrying a plate with multiple dishes. If the plate falls, they have to go back and pick up all the dishes and start again.

3. Selective Repeat Protocol: Imagine a person carrying a bag with multiple items. If they drop one item, they only need to pick up that item and continue, not all the items in the bag.

Advantages of Elementary Data Link Protocols:

1. Simple and easy to implement.
2. Low overhead and efficient use of bandwidth.
3. Reliable data transmission.

Disadvantages of Elementary Data Link Protocols:

1. Limited error detection and correction capabilities.
2. Inefficient for large data transmission.

Example: Ethernet uses the Stop-and-Wait protocol for reliable data transmission.

Applications: Elementary Data Link Protocols are used in various network technologies such as Ethernet, Wi-Fi, and Bluetooth.

In conclusion, Elementary Data Link Protocols are the basic building blocks in the data link layer of computer networks. They provide reliable data transmission, efficient use of bandwidth, and are widely used in various network technologies. Understanding these protocols is essential for anyone working in the field of computer networks.