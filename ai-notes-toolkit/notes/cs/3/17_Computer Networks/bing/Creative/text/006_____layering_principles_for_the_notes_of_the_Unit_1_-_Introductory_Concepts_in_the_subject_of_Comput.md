### Layering Principles for the Notes of the Unit 1 - Introductory Concepts in the Subject of Computer Networks

- Layering is a process that is used to simplify network communication and help the host and server interact with each other quickly.
- Layering divides the communication process into smaller and simpler components, called layers, that can be handled independently.
- Each layer of a specific network model may be responsible for a different function of the network, such as error control, routing, encryption, etc.
- Each layer will pass information up and down to the next subsequent layer as data is processed. The information may be encapsulated or decapsulated with additional headers or trailers as it moves between layers.
- The most widely used network model is the Open Systems Interconnection (OSI) model, which consists of seven layers: physical, data link, network, transport, session, presentation, and application.
- The network layer is the third layer of the OSI model, and it is responsible for providing logical addressing, routing, and packet delivery across different networks .
- The network layer itself relies on the following principles:
  - Each network layer entity is identified by a network layer address. This address is independent of the data link layer addresses that it may use.
  - The service provided by the network layer does not depend on the service or the internal organization of the underlying data link layers.
  - The network layer is conceptually divided into two planes: the data plane and the control plane. The data plane is responsible for forwarding packets based on their network layer addresses, while the control plane is responsible for exchanging routing information and maintaining routing tables.
- The independence of the network layer from the underlying data link layer is a key principle of the network layer. It ensures that the network layer can be used to allow hosts attached to different types of data link layers to exchange packets through intermediate routers.
- The function of each layer should be chosen with an eye toward defining internationally standardized protocols that can be implemented by different vendors and interoperate with each other.
- Layering provides several benefits, such as modularity, scalability, flexibility, and interoperability.