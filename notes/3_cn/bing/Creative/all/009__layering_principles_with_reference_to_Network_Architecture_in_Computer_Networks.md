#### Layering principles with reference to Network Architecture in Computer Networks

Layering is a design principle that divides a complex system into smaller and simpler components, called layers, that can be developed and tested independently. Each layer provides a set of services to the higher layer by using the services of the lower layer and adding some value to them. Layering helps to modularize the network architecture, reduce complexity, increase interoperability, and facilitate standardization.

Some of the layering principles that are applied to design network architectures are :

- A layer should be created where a different abstraction is needed. For example, the physical layer deals with the transmission of bits over a medium, while the data link layer deals with the framing and error control of those bits.
- Each layer should perform a well-defined function. For example, the network layer is responsible for routing packets across multiple networks, while the transport layer is responsible for end-to-end communication and reliability.
- The function of each layer should be chosen with an eye toward defining internationally standardized protocols. For example, the OSI model defines seven layers with common protocols for each layer, such as Ethernet for the data link layer and TCP for the transport layer.
- The layer boundaries should be chosen to minimize the information flow across the interfaces. For example, the interface between the network layer and the data link layer should only contain the necessary information for addressing and routing, not the application data or the transport protocol.
- The number of layers should be large enough that distinct functions need not be thrown together in the same layer out of necessity and small enough that the architecture does not become unwieldy. For example, the OSI model has seven layers, while the TCP/IP model has four layers.

The most widely used network architectures are the OSI model and the TCP/IP model, which have different layering schemes and protocols. The OSI model has seven layers: physical, data link, network, transport, session, presentation, and application. The TCP/IP model has four layers: link, internet, transport, and application. The following table shows the comparison of the two models:

| OSI Model | TCP/IP Model | Function |
| --- | --- | --- |
| Application | Application | Provides user interface and high-level services, such as file transfer, email, web browsing, etc. |
| Presentation | (Application) | Provides data representation, encryption, compression, etc. |
| Session | (Application) | Provides dialog control, synchronization, authentication, etc. |
| Transport | Transport | Provides end-to-end communication, reliability, flow control, multiplexing, etc. |
| Network | Internet | Provides routing, addressing, fragmentation, etc. |
| Data Link | Link | Provides framing, error control, medium access, etc. |
| Physical | (Link) | Provides transmission of bits over a medium, modulation, coding, etc. |

The following diagram shows the layered packet format for the OSI model and the TCP/IP model:

```
+-------------------------+-------------------------+
| Application Data        | Application Data        |
+-------------------------+-------------------------+
| Presentation Header     |                         |
+-------------------------+                         |
| Session Header          |                         |
+-------------------------+-------------------------+
| Transport Header        | Transport Header        |
+-------------------------+-------------------------+
| Network Header          | Internet Header         |
+-------------------------+-------------------------+
| Data Link Header        | Link Header             |
+-------------------------+-------------------------+
| Physical Header         |                         |
+-------------------------+-------------------------+
| OSI Model               | TCP/IP Model            |
+-------------------------+-------------------------+
```

The data that is transmitted from one layer to another is called a Protocol Data Unit (PDU), which consists of a header and a payload. The header contains the information that is needed by the layer to process the data, such as source and destination addresses, sequence numbers, checksums, etc. The payload contains the data that is passed from the higher layer or the lower layer. The payload of one layer becomes the header of the next layer, and vice versa. For example, the payload of the transport layer is the application data, which becomes the header of the application layer. The header of the transport layer is the transport header, which becomes the payload of the network layer.

The following table shows the names of the PDUs for each layer of the OSI model and the TCP/IP model:

| OSI Model | TCP/IP Model | PDU Name |
| --- | --- | --- |
| Application | Application | Message |
| Presentation | (Application) | N/A |
| Session | (Application) | N/A |
| Transport | Transport |