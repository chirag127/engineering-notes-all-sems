#### Layering Principles with Reference to Network Architecture in Computer Networks

- Layering is a mechanism that divides a complex system into smaller and manageable parts, called layers, that interact with each other through well-defined interfaces .
- Layering allows for modularity, abstraction, encapsulation, and interoperability of network components and protocols.
- Layering also facilitates the design, implementation, testing, and maintenance of network systems, as well as the adaptation to new technologies and standards.
- One of the most widely used network models that employs layering is the Open Systems Interconnection (OSI) model, which consists of seven layers: physical, data link, network, transport, session, presentation, and application .
- The principles that were applied to arrive at the seven layers of the OSI model can be briefly summarized as follows:
  - A layer should be created where a different abstraction is needed.
  - Each layer should perform a well-defined function.
  - The function of each layer should be chosen with an eye toward defining internationally standardized protocols.
  - The layer boundaries should be chosen to minimize the information flow across the interfaces.
  - The number of layers should be large enough that distinct functions need not be thrown together in the same layer out of necessity and small enough that the architecture does not become unwieldy.
- The OSI model defines the services, functions, and protocols for each layer, as well as the data units and formats that are exchanged between adjacent layers.
- The data units are called protocol data units (PDUs), which consist of headers, trailers, and payloads. Headers and trailers contain control information, such as source and destination addresses, sequence numbers, error detection codes, etc. Payloads contain the actual data or information.
- The PDUs are encapsulated and decapsulated as they traverse the layers. For example, when data is sent from the application layer to the physical layer, each layer adds its own header and trailer to the PDU received from the upper layer, forming a new PDU. When data is received from the physical layer to the application layer, each layer removes the header and trailer added by the corresponding layer at the sender side, and passes the remaining PDU to the upper layer.
- The OSI model provides a conceptual framework for understanding the network architecture and communication process, but it is not a practical implementation. In reality, most network systems use a simplified version of the OSI model, such as the TCP/IP model, which has four layers: application, transport, internet, and network access.