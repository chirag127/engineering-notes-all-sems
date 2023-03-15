 Here is the content in markdown format for the topic ### Fundamental Models for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM:

### Fundamental Models

The fundamental models for distributed systems are:

1. Client-Server Model: In this model, there are dedicated server processes that provide resources or services to client processes on demand. The clients get connected to the servers, requests a service, gets served and disconnected. Example: Web server and browser.
    - Advantage: Server specialization and centralized control.
    - Disadvantage: Single point of failure and bottleneck.

2. Peer-to-Peer Model: In this model, all processes have equal responsibilities and roles. There is no dedicated server. The processes act as both client and server. Example: BitTorrent, Skype.
    - Advantage: Fault tolerance and scalability.
    - Disadvantage: Difficult to implement and complex to maintain.

3. Message Passing Model: In this model, the processes communicate with each other by exchanging messages through message passing. There is no shared memory. Example: Email, instant messaging.
    - Advantage: Decoupled processes and easier to distribute.
    - Disadvantage: Slower than shared memory and cumbersome for complex communication.

[Additional details, diagrams, examples, pros and cons can be added here for better understanding]

The models can be combined in many ways to utilize their advantages in a distributed system. The selection of a model depends on the requirements and objectives of the system.