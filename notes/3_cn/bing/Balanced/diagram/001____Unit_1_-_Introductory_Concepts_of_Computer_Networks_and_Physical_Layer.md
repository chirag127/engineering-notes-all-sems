## Unit 1 - Introductory Concepts of Computer Networks and Physical Layer

A computer network is any group of interconnected computing devices capable of sending or receiving data. A computing device can be a computer, a tablet, a phone, or a smart sensor. Computer networks can be classified by their size, topology, architecture, and protocols.

The physical layer is the lowest layer of the OSI model of computer networking. It is responsible for the actual physical connection between the devices and the transmission of bits over a medium. It deals with the mechanical and electrical specifications of the interface and the transmission medium. It also coordinates the functions required to carry a bit stream over a physical medium.

A possible ASCII diagram for the physical layer is:

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|   Device A     |     |   Device B     |     |   Device C     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Physical      |     |  Physical      |     |  Physical      |
|  Layer         |     |  Layer         |     |  Layer         |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Interface     |     |  Interface     |     |  Interface     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Medium        |     |  Medium        |     |  Medium        |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
|  Bit Stream    |     |  Bit Stream    |     |  Bit Stream    |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```

The interface is the point where the device connects to the medium. The medium is the physical material that carries the signal, such as copper wire, optical fiber, or radio waves. The bit stream is the sequence of 0s and 1s that represents the data. The physical layer converts the bit stream into electrical, optical, or electromagnetic signals that can be transmitted over the medium.