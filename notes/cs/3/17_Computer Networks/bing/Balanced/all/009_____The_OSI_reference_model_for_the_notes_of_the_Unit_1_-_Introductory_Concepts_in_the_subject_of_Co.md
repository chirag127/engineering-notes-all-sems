# The OSI reference model

The OSI reference model is a conceptual framework that describes how information from a software application in one computer moves through a physical medium to another computer. It was developed by the International Organization for Standardization (ISO) in the late 1970s and early 1980s to facilitate interoperability and standardization of network protocols and devices.

The OSI reference model consists of seven layers, each of which performs a specific function in the communication process. The layers are:

- **Layer 1: Physical layer**. This layer defines the physical characteristics of the transmission medium, such as the voltage, frequency, modulation, and connector types. It also deals with the transmission and reception of raw bits over the medium .
- **Layer 2: Data link layer**. This layer provides reliable and error-free data transfer between adjacent nodes on the same network. It also handles the framing, addressing, and flow control of data packets. It may use sublayers, such as the Logical Link Control (LLC) and the Media Access Control (MAC), to perform different functions .
- **Layer 3: Network layer**. This layer is responsible for routing data packets across different networks or subnets. It also handles the addressing, fragmentation, and reassembly of packets. It uses protocols, such as the Internet Protocol (IP), to perform these tasks .
- **Layer 4: Transport layer**. This layer provides end-to-end data delivery between applications on different hosts. It also handles the segmentation, reassembly, and error detection and correction of data streams. It may use protocols, such as the Transmission Control Protocol (TCP) or the User Datagram Protocol (UDP), to provide different levels of reliability and service quality .
- **Layer 5: Session layer**. This layer establishes, maintains, and terminates sessions between applications on different hosts. It also manages the synchronization, coordination, and authentication of data exchange. It may use protocols, such as the Session Initiation Protocol (SIP) or the Remote Procedure Call (RPC), to perform these functions .
- **Layer 6: Presentation layer**. This layer is responsible for the representation, encryption, and compression of data. It also handles the translation of data formats and character sets between different applications. It may use protocols, such as the Secure Sockets Layer (SSL) or the Hypertext Transfer Protocol (HTTP), to perform these tasks .
- **Layer 7: Application layer**. This layer provides the interface and services for the user applications to access the network. It also defines the protocols and formats for the exchange of application-specific data, such as email, web, file transfer, etc. It may use protocols, such as the Simple Mail Transfer Protocol (SMTP) or the File Transfer Protocol (FTP), to perform these tasks .

The OSI reference model is often depicted as a stack of layers, with the lower layers closer to the physical medium and the higher layers closer to the user applications. The data flow between the layers is bidirectional, meaning that each layer can send and receive data to and from the adjacent layers. The data units exchanged between the layers are called Protocol Data Units (PDUs), and they may have different names and formats depending on the layer, such as bits, frames, packets, segments, or messages .

The OSI reference model is not a network architecture or a protocol suite, but rather a guideline or a reference for the design and implementation of network protocols and devices. It helps to ensure compatibility and interoperability between different network systems and applications. It also provides a common language and terminology for describing network functions and operations .

The following diagram illustrates the OSI reference model and some of its associated protocols and devices:

![OSI reference model diagram](https://www.networkworld.com/cms/article/3239677/osi-model-1.jpg)