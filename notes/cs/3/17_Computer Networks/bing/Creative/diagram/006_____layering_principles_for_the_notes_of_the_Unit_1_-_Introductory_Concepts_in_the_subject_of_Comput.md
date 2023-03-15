### Layering Principles

Layering is a process that is used to simplify network communication and help the host and server interact with each other quickly. It is an important part of the OSI model made to simplify the transmission process by separating communication into pieces that can be sent easily and securely.

Some of the benefits of layering are:

- It allows the modular design of network protocols and services.
- It enables interoperability between different types of network devices and software.
- It facilitates the development and testing of network components.
- It enhances the scalability and performance of network systems.
- It isolates the faults and errors in network communication.

The principles that were applied to arrive at the seven layers of the OSI model can be briefly summarized as follows:

- A layer should be created where a different abstraction is needed.
- Each layer should perform a well-defined function.
- The function of each layer should be chosen with an eye toward defining internationally standardized protocols.
- The layer boundaries should minimize the information flow across the interfaces.
- The number of layers should be large enough that distinct functions need not be thrown together in the same layer out of necessity and small enough that the architecture does not become unwieldy.

The seven layers of the OSI model are:

- Physical layer: It deals with the transmission and reception of the unstructured raw bit stream over a physical medium. It defines the electrical and mechanical characteristics of the devices and the media.
- Data link layer: It provides the functional and procedural means to transfer data between network entities and to detect and possibly correct errors that may occur in the physical layer. It defines the format of the data packets and the access control methods for the shared medium.
- Network layer: It provides the functional and procedural means of transferring variable length data sequences from a source to a destination via one or more networks while maintaining the quality of service requested by the transport layer. It defines the addressing and routing schemes for the data packets.
- Transport layer: It provides the functional and procedural means of transferring data between end systems and is responsible for end-to-end error recovery and flow control. It ensures complete data transfer and maintains the connection between the source and destination.
- Session layer: It provides the mechanism for managing the dialogue between end systems. It establishes, maintains and synchronizes the interaction among communicating systems. It also provides security and name resolution services.
- Presentation layer: It provides the services that allow communication systems to interpret the meaning of data exchanged between them. It performs data transformation, encryption, compression and formatting functions.
- Application layer: It provides the services that directly support user applications, such as file transfer, email, web browsing, remote login, etc. It interacts with the user and provides the interface for the network communication.

The following diagram illustrates the layering concept and the data flow between the layers:

![Layering diagram](https://www.studytonight.com/computer-networks/images/osi-model-1.png)

: The concept of layering - Definition, Topic, Books, Importance & Tips ... (2021, February 26). Retrieved from https://byjusexamprep.com/computer-science-engineering-exams/the-concept-of-layering

: ISO/OSI Model and it's Layers - Physical to Application | Studytonight. Retrieved from https://www.studytonight.com/computer-networks/complete-osi-model