## Unit 3 - Link layer

The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet. The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to. The link layer is also known as the data link layer or layer 2 in the OSI model.

The main functions of the link layer are:

- Framing: The link layer receives packets from the network layer and divides them into small frames, then sends each frame bit-by-bit to the physical layer.
- Error control: The link layer detects and corrects errors that may occur in the physical layer. The link layer can use techniques such as parity check, checksum, or cyclic redundancy check (CRC) to detect errors, and techniques such as automatic repeat request (ARQ) or forward error correction (FEC) to correct errors.
- Flow control: The link layer regulates the flow of data between the sender and the receiver to avoid congestion or buffer overflow. The link layer can use techniques such as stop-and-wait, sliding window, or backpressure to control the flow of data.
- Media access control: The link layer coordinates the access of multiple devices to a shared medium, such as a wireless channel or a bus network. The link layer can use techniques such as contention-based, reservation-based, or polling-based to manage the media access.
- Addressing: The link layer assigns a unique address to each device on the link, such as a MAC address or a link-local address. The link layer uses the address to identify the source and destination of each frame.
- Link management: The link layer establishes, maintains, and terminates the link between the devices on the network. The link layer can use protocols such as PPP, HDLC, or Ethernet to perform the link management functions.