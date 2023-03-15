 Here is the content in markdown format for the topic ### Strawman Architecture for Enterprise-wide SOA for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture:

### Strawman Architecture for Enterprise-wide SOA

- The strawman architecture for enterprise-wide SOA consists of the following layers:

1. Service consumers layer: This layer consists of applications that consume services. Examples include web applications, desktop applications, etc.

2. Services layer: This layer consists of business services that encapsulate business logic and processes. Services can be coarse-grained or fine-grained.

3. Service broker: The service broker acts as a registry and intermediary for service consumers and services. It takes care of service discovery, service selection, routing, composition, and aggregation.

4. Operational services layer: This layer consists of services that provide operational functions such as security, billing, monitoring, logging, etc.

5. Enterprise service bus: The enterprise service bus acts as a communication backbone and messaging system for the SOA. It facilitates connectivity and messaging between the different layers of the SOA.

6. Integration with legacy systems: Existing legacy systems can be wrapped as services and plugged into the SOA. This enables incremental adoption of SOA in enterprise environments.

Advantages:

- Loose coupling between components leading to flexibility and interoperability
- Incremental adoption and heterogeneous integration of components
- Reusability of business services across applications
- Separation of concerns across layers

Disadvantages:

- Can be complex to implement and govern
- Performance challenges can arise due to multiple layers and indirection
- Versioning of services can lead to compatibility issues

Applications: The strawman architecture is a theoretical reference architecture for enterprise-wide SOA adoption. Specific implementations would differ based on enterprise requirements and technologies used. The layers provide a logical separation of concerns that can guide the design of an enterprise SOA.