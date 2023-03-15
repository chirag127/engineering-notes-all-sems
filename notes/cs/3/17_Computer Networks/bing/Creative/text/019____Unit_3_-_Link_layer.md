## Unit 3 - Link layer

- The link layer is the lowest layer in the Internet protocol suite, the networking architecture of the Internet.
- The link layer is the group of methods and communications protocols confined to the link that a host is physically connected to.
- The link layer is responsible for transferring data between nodes on a network segment across the physical layer.
- The link layer can be divided into two sublayers: the logical link control (LLC) and the media access control (MAC).
- The LLC sublayer provides services such as error detection, flow control, and multiplexing to the upper layers.
- The MAC sublayer deals with the access and allocation of the shared medium, such as Ethernet, Wi-Fi, or Bluetooth.
- Some of the common link layer protocols are Ethernet, Wi-Fi, PPP, HDLC, and SLIP.
- The link layer performs the following functions:
  - Framing: The packet received from the network layer is known as a frame in the link layer. The link layer divides the packets into small frames and sends each frame bit-by-bit to the physical layer.
  - Addressing: The link layer assigns a unique address to each node on the network segment, which is called the MAC address or the physical address.
  - Error control: The link layer detects and corrects errors that may occur during the transmission of frames. The link layer uses techniques such as parity check, checksum, and cyclic redundancy check (CRC) to detect errors.
  - Flow control: The link layer regulates the flow of data between the sender and the receiver to avoid congestion and buffer overflow. The link layer uses techniques such as stop-and-wait, sliding window, and backpressure to control the flow of data.
  - Access control: The link layer coordinates the access and allocation of the shared medium among the competing nodes. The link layer uses techniques such as contention-based, reservation-based, and polling-based to control the access of the medium.