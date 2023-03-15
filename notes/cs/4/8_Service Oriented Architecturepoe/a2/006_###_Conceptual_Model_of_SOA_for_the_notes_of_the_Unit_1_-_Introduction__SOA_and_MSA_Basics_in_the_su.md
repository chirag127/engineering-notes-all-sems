 Here is the content in markdown format for the topic ### Conceptual Model of SOA for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture:

### Conceptual Model of SOA

- SOA consists of three layers: Service provider, Service registry, and Service consumer.
- **Service provider**: Provides services/business functions over a network. Each service has a defined interface which can be discovered and accessed by service consumers.
- **Service registry**: Stores and manages service descriptions. Service consumers can lookup for services and their interfaces in the registry.
- **Service consumer**: Discovers and invokes services through the service registry. Service consumers do not need to know the implementation details of a service. They can simply invoke a service through its published interface.

Advantages:
- Loose coupling: Services are loosely coupled, can be developed and deployed independently.
- Reusability: Services can be reused by multiple applications.
- Interoperability: Services use standard interfaces to interact, enabling interoperability.
- Platform independence: Services can be accessed from any platform/language as long as they support the service's interface.

Disadvantages:
- Additional overhead: There is additional complexity in implementing SOA. Extra layers like service registry add overhead.
- Versioning: Versioning of services and handling backward compatibility can be challenging.
- Performance: There can be performance issues due to network latency in service calls.
- Security: There are additional security considerations with services exposed over a network.

Applications: SOA is suitable for enterprise applications where reuse and integration of business functions are required. It is a popular choice for developing cloud-based applications.