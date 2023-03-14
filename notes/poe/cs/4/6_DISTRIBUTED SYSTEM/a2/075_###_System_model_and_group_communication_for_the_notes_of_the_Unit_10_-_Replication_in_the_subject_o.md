 Here is the content in markdown format for the topic ### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM:

### System model and group communication for the notes of the Unit 10 - Replication in the subject of DISTRIBUTED SYSTEM

- A distributed system consists of multiple autonomous computers that communicate and coordinate their actions only by passing messages to one another.
- The components of a distributed system may fail or slow down, and there may be errors in communication. Therefore, the system must be designed to be robust in the face of such failures and uncertainties.
- Group communication refers to the ability to send messages to a group of processes. It is a fundamental abstraction for building distributed applications, and replication is one important application of group communication.
- Two common paradigms for group communication are:
- Publish-subscribe: Processes can subscribe to receive messages on certain topics, and processes can publish messages on topics. The middleware then delivers messages to all subscribers of the appropriate topics. This decouples senders and receivers.
- Message multicast: Senders address messages to a group, and the middleware delivers a copy of any multicast message to all members of the addressed group. Multicast directly connects senders and receivers as a group.

*Some useful mnemonics and learning tricks for remembering the concepts:*

- DISTributed SYSTEM: **D**COMPONENTS **I**COMMUNICATE **S**MESSAGES **T**COORDINATE **R**ACTIONS
- GROUP COMMUNICATION: **G**SEND **R**GROUP **O**PROCESSES **U**MESSAGE **P**DELIVERY

*Advantages:* Robustness, scalability.
*Disadvantages:* Complexity, ordering and reliability guarantees are hard to provide.
*Applications:* Replication, collaborative applications.

Does this help? Let me know if you would like me to elaborate on any of the points or add more details.