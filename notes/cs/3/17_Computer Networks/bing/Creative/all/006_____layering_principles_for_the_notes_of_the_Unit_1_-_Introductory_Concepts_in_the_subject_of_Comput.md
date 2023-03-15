# Layering Principles for the Notes of the Unit 1 - Introductory Concepts in the Subject of Computer Networks

- Layering is a process that is used to simplify network communication and help the host and server interact with each other quickly.
- Layering divides the communication process into smaller and simpler components, called layers, that can be handled independently.
- Each layer of a specific network model may be responsible for a different function of the network, such as error control, routing, encryption, etc.
- Each layer will pass information up and down to the next subsequent layer as data is processed. The information may be encapsulated or decapsulated with additional headers or trailers as it moves between layers.
- The layered concept of networking was developed to accommodate changes in technology. By separating the functions of different layers, it is possible to update or modify one layer without affecting the others.
- There are different network models that define the number and the functions of the layers, such as the OSI model and the TCP/IP model.
- The network layer is one of the most important layers in the network models. It is responsible for delivering packets from the source host to the destination host across multiple networks or routers.
- The network layer itself relies on the following principles:
  - Each network layer entity is identified by a network layer address. This address is independent of the datalink layer addresses that it may use.
  - The service provided by the network layer does not depend on the service or the internal organisation of the underlying datalink layers.
  - The network layer is conceptually divided into two planes: the data plane and the control plane. The data plane is responsible for forwarding packets based on the network layer addresses. The control plane is responsible for maintaining the routing tables and the network layer addresses.
- The independence of the network layer from the underlying datalink layer is a key principle of the network layer. It ensures that the network layer can be used to allow hosts attached to different types of datalink layers to exchange packets through intermediate routers.
- The network layer can use different protocols to implement its functions, such as IP, ICMP, ARP, etc. Some of these protocols are also used by other layers, such as the transport layer or the application layer.