### Layering Principles

Layering is a process that is used to simplify network communication and help the host and server interact with each other quickly. It is an important part of the OSI model made to simplify the transmission process by separating communication into pieces that can be sent easily and securely.

The layering principles for the notes of the Unit 1 - Introductory Concepts in the subject of Computer Networks are:

- A layer should be created where a different abstraction is needed.
- Each layer should perform a well-defined function.
- The function of each layer should be chosen with an eye toward defining internationally standardized protocols.
- The layer boundaries should be chosen to minimize the information flow across the interfaces.
- The number of layers should be large enough that distinct functions need not be thrown together in the same layer out of necessity and small enough that the architecture does not become unwieldy.
- The independence of the network layer from the underlying datalink layer is a key principle of the network layer. It ensures that the network layer can be used to allow hosts attached to different types of datalink layers to exchange packets through intermediate routers.
- The network layer itself relies on the following principles:
  - Each network layer entity is identified by a network layer address. This address is independent of the datalink layer addresses that it may use.
  - The service provided by the network layer does not depend on the service or the internal organisation of the underlying datalink layers.
  - The network layer is conceptually divided into two planes: the data plane and the control plane.