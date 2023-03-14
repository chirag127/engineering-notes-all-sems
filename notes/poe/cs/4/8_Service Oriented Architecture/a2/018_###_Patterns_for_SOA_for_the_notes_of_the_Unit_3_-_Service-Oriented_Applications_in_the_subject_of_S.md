 Here is the content in markdown format for the topic ### Patterns for SOA for the notes of the Unit 3 - Service-Oriented Applications in the subject of Service Oriented Architecture:

### Patterns for SOA

The following are some commonly used patterns for Service Oriented Architecture:

1. Service Layer Pattern: This pattern involves separating an application into layers where the service layer contains business logic and handles communication with the data layer. The service layer exposes the application functionality as services which can be consumed by presenting layers. This pattern enables loose coupling and reusability.

Advantages: Loose coupling, separation of concerns, reuse of business logic.
Disadvantages: Can add complexity and overhead.

2. Service Façade Pattern: This pattern provides a single interface to access a set of internal services/systems. The façade handles communication with the actual services and aggregates their responses. This pattern simplifies interaction with a set of services and reduces coupling.

Advantages: Simpler interface, reduces coupling.
Disadvantages: The façade can become a bottleneck and single point of failure.

3. Composite Service Pattern: This pattern involves composing a service by aggregating other basic services. The composite service acts as a single service but internally orchestrates multiple services to achieve its functionality. This pattern enables reuse and separation of concerns.

Advantages: Reuse, separation of concerns.
Disadvantages: Can add latency and complexity.

[Further details, diagrams, examples, etc. can be added here for the above points.]

The above points can be remembered using the mnemonics:

SLP: Service Layer Pattern
SFP: Service Façade Pattern
CSP: Composite Service Pattern

[Additional mnemonics or learning tricks can be included if easy to remember.]