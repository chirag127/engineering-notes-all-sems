 Here is the content in markdown format for the topic ### Strawman Architecture for Enterprise-wide SOA for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture:

### Strawman Architecture for Enterprise-wide SOA

- The Strawman Architecture for Enterprise-wide SOA consists of the following layers:
- Services Layer: This layer contains the actual business services/functions implemented as service components. These services can be atomic services or composite services orchestrating multiple atomic services.
- Service Integration Layer: This layer handles service integration issues such as service abstraction, mediation, transformation, routing, choreography, and process management. The main components of this layer are the Enterprise Service Bus (ESB) and the Business Process Management (BPM) engine.
- Services Registry: This is a repository of service descriptions (interfaces and semantics) in a standardized format (e.g., WSDL). The registry plays an essential role in service discovery and governance.
- Access Layer: This layer contains the service access mechanisms (e.g., portal, web service invocation, B2B gateway) and the security components (authentication, authorization, auditing).
- Management Layer: This layer contains the components required for the management of the overall SOA, including service-level management, policy management, and repository management.

Advantages:
- It provides a reference architecture for Enterprise-wide SOA
- It clearly separates the different layers and components, facilitating comprehension and implementation
- It supports loose coupling between the layers through standardized interfaces

Disadvantages:
- It is quite abstract and high-level, lacking implementation details
- The distinction between layers may not always be very sharp
- It does not provide mechanisms/guidance for cross-layer interactions (e.g., propagation of security credentials)

Examples: The US Department of Defense's (DoD) Net-Centric Enterprise Services (NCES) reference architecture is based on a strawman architecture for enterprise-wide SOA.

Applications: The strawman architecture can be used as a starting point for the architectural design of enterprise-wide SOA implementations. It highlights the main layers and components to be considered but needs to be refined and customized based on the specific requirements and context.