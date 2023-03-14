 Here is the content in markdown format for the topic ### Service oriented Architecture and Microservices architecture for the notes of the Unit 1 - Introduction: SOA and MSA Basics in the subject of Service Oriented Architecture:

### Service Oriented Architecture (SOA)

- SOA is a style of software design where applications are built as a set of services that are loosely coupled to exchange data through standard interfaces.
- Services are self-contained, platform independent and accessible over the network.
- Services communicate with each other by passing data in XML or JSON format.
- Services can be reused and composed into other services and applications.
- Some of the core principles of SOA are:
** Loose coupling: Services are loosely coupled so that they interact through standard interfaces and can be changed independently.
** Service reusability: Services should be designed to be reusable by multiple systems and processes.
** Abstraction: Details are hidden behind interfaces and are used without knowledge of their internal implementation.
** Autonomy: Services can be developed and managed independently as long as they conform to the interface contract.
** Interoperability: Services are interoperable as they interact through standard interfaces and messages.
- advantages: Flexibility, interoperability, loose coupling, reusability.
- disadvantages: Can be complex to implement, lack of governance can lead to chaos, performance issues if not designed properly.
- Examples: Amazon Web Services (AWS), Google APIs, etc.

### Microservices Architecture (MSA)

- MSA is a variant of SOA where applications are built as a set of independent, self-contained services.
- Services are fine-grained and each service runs a unique process and communicates over lightweight mechanisms like HTTP.
- There is a heavy emphasis on decentralization, isolation and automation.
- Some key characteristics are:
** Small, focused services: Each service handles a specific task and has a narrow purpose.
** Decentralized: There is no centralized control and each service is autonomous.
** Lightweight communication: Services communicate over lightweight mechanisms like HTTP and pass messages in JSON or XML format.
** Automation: There is extensive automation of tasks like deployment, scaling, failure recovery, etc.
- advantages: Increased scalability, improved modularity, technology heterogeneity, fault isolation.
- disadvantages: Can be complex to manage and debug, distributed transactions can be difficult, latency due to network calls.
- Examples: Netflix, Uber, Airbnb, etc.