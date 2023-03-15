## Unit 2 - Link layer in Computer Networks and Medium Access Control and Local Area Networks

- The link layer is the lowest layer in the TCP/IP network model and is equivalent to layer 2 in the OSI model.
- The link layer is responsible for transferring data between adjacent network nodes in a wide area network or between nodes on the same local area network.
- The link layer consists of two sublayers: the logical link control (LLC) sublayer and the media access control (MAC) sublayer .
- The LLC sublayer is responsible for managing communications links and handling frame traffic.
- The MAC sublayer is responsible for governing protocol access to the physical network medium.
- The MAC sublayer defines how nodes share the common channel and avoid collisions.
- The MAC sublayer can use different techniques to coordinate the access to the channel, such as contention-based, reservation-based, polling-based, or token-based.
- The MAC sublayer can also use different protocols to handle collisions, such as CSMA/CD, CSMA/CA, or ALOHA.
- The MAC sublayer can be implemented in different ways depending on the type of network, such as Ethernet, Wi-Fi, Bluetooth, or cellular.
- The link layer frames are the smallest units of bits on a link layer network and contain a header, a payload, and a trailer.
- The link layer header contains information such as the source and destination MAC addresses, the frame type, and the frame length.
- The link layer trailer contains information such as the frame check sequence, which is used to detect errors.
- The link layer can provide various services to the network layer, such as framing, error detection, error correction, flow control, and link management.
- The link layer can also provide various functions to the physical layer, such as encoding, decoding, synchronization, and modulation.

### Mnemonics and learning tricks

- To remember the two sublayers of the link layer, use the acronym **L**ink **L**ayer = **L**LC + **M**AC.
- To remember the four types of MAC techniques, use the acronym **C**ontention, **R**eservation, **P**olling, **T**oken = **CRPT**.
- To remember the three types of collision handling protocols, use the acronym **C**SMA/**C**D, **C**SMA/**C**A, **A**LOHA = **CCA**.
- To remember the four types of network where MAC can be implemented, use the acronym **E**thernet, **W**i-Fi, **B**luetooth, **C**ellular = **EWBC**.
- To remember the three parts of a link layer frame, use the acronym **H**eader, **P**ayload, **T**railer = **HPT**.
- To remember the five services that the link layer can provide to the network layer, use the acronym **F**raming, **E**rror detection, **E**rror correction, **F**low control, **L**ink management = **FEEL F**.
- To remember the four functions that the link layer can provide to the physical layer, use the acronym **E**ncoding, **D**ecoding, **S**ynchronization, **M**odulation = **EDSM**.