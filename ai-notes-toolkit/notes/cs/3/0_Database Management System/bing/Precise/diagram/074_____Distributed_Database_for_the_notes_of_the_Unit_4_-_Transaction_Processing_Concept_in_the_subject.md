### Distributed Database

A distributed database is a database that consists of two or more files located in different sites either on the same network or on entirely different networks. Portions of the database are stored in multiple physical locations and processing is distributed among multiple database nodes.

#### Characteristics of Distributed Databases:
- Data is stored on multiple computers.
- The computers are connected by a network.
- Data is replicated or partitioned among the computers.
- The system appears to the user as a single logical database.

#### Advantages of Distributed Databases:
- Improved reliability and availability.
- Improved performance.
- Easier expansion.
- Local autonomy.

#### Disadvantages of Distributed Databases:
- Increased complexity.
- More difficult to maintain data consistency.
- More difficult to manage.

#### Transaction Processing in Distributed Databases:
- A transaction is a logical unit of work that must be either completed in its entirety or aborted.
- In a distributed database, a transaction may access data on multiple nodes.
- The two-phase commit protocol is used to ensure that a transaction is either committed on all nodes or aborted on all nodes.
- The coordinator node sends a prepare message to all participating nodes.
- Each node responds with a yes or no vote.
- If all nodes vote yes, the coordinator sends a commit message to all nodes.
- If any node votes no, the coordinator sends an abort message to all nodes.
