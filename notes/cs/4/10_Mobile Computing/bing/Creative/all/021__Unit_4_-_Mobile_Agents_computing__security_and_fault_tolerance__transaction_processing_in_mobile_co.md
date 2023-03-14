## Unit 4 - Mobile Agents computing, security and fault tolerance, transaction processing in mobile computing

- Mobile agents are a type of software agents that can migrate from one computer to another autonomously and continue their execution on the destination computer.
- Mobile agents can be classified into two types based on their migration path:
  - Mobile agents with predefined path: these have a static migration path.
  - Free roaming mobile agents: these have a dynamic migration path. Depending on the present network condition, the mobile agent chooses its path.
- Mobile agents have some features that make them suitable for mobile computing :
  - Intelligence: mobile agents can learn and search for knowledge about their domain. They can also transport their state from one environment to another without disturbing the previous holding data and be capable of performing appropriately in the new environment.
  - Autonomy: mobile agents are self-driven and do not require a corresponding node for communication. They can also take autonomous decisions while selecting a node.
  - Mobility: mobile agents can move from one node to another and carry out tasks along with them. This feature distributes the processing and balancing of the load. Another benefit of this capability is that when the user goes offline, the agents will still keep functioning.
  - Communication: mobile agents can communicate effectively with other agents, users and systems. The mobile agents use a communication language for inter-agent communication.
- The life cycle of mobile agents ensures the following conditions:
  - They can adapt to the environment, either home or foreign environment.
  - They are capable of switching among the positions of one node to another.
  - They are autonomous and focused on the final output.
- Mobile agents face some challenges and issues in mobile computing, such as:
  - Security: mobile agents need to protect themselves from malicious hosts and other agents, as well as protect the hosts and other agents from themselves. Some security threats include code tampering, eavesdropping, denial of service, unauthorized access, etc. Some security techniques include encryption, authentication, access control, digital signatures, etc.
  - Fault tolerance: mobile agents need to cope with failures and errors that may occur during their migration and execution. Some fault tolerance mechanisms include checkpointing, replication, recovery, etc.
  - Transaction processing: mobile agents need to ensure the consistency and reliability of the data and operations that they perform on different hosts. Some transaction processing models include flat, nested, atomic, etc. Some transaction processing techniques include locking, logging, commit protocols, etc.