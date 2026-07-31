### Link layer connectivity and TCP IP connectivity

- The link layer is the lowest layer of the TCP/IP model, which is a simplified version of the OSI model.
- The link layer is responsible for sending and receiving data frames over a physical medium, such as a cable or a wireless channel.
- The link layer also provides error detection, flow control, and media access control for the data frames.
- The link layer is sometimes called the network access layer or the network interface layer, as it connects the network layer (IP) to the physical layer (hardware).
- The link layer protocols vary depending on the type and topology of the network, such as Ethernet, Wi-Fi, Bluetooth, etc.
- The link layer is often compared to the combination of the data link layer and the physical layer in the OSI model, but they are not identical .
- The network layer is the second layer of the TCP/IP model, which is responsible for routing packets across different networks.
- The network layer uses the Internet Protocol (IP) to assign logical addresses to the packets and to determine the best path to reach the destination.
- The network layer also handles fragmentation and reassembly of packets, as well as congestion control and error reporting.
- The network layer is sometimes called the internet layer, as it enables the interconnection of different networks into a single internet.
- The network layer is similar to the network layer in the OSI model, but it does not include some functions, such as network discovery and network management .
- The link layer and the network layer work together to provide end-to-end connectivity and reliability for the data transmission over the internet.
- The link layer encapsulates the network layer packets into frames and adds a header and a trailer with the source and destination MAC addresses and a checksum.
- The link layer then sends the frames to the physical layer, which converts them into electrical signals or electromagnetic waves and transmits them over the medium.
- The link layer also receives the frames from the physical layer, checks the checksum for errors, and decapsulates the network layer packets from the frames.
- The network layer extracts the source and destination IP addresses from the packets and forwards them to the appropriate interface or router based on the routing table.
- The network layer also splits the packets into smaller fragments if the link layer has a smaller maximum transmission unit (MTU) than the packet size, and reassembles the fragments at the destination .