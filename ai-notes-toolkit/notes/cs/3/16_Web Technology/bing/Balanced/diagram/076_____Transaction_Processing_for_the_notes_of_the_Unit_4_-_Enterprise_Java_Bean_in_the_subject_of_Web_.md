### Transaction Processing for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- A transaction is a logical unit of work that consists of a sequence of operations that must be executed atomically, consistently, isolated, and durable (ACID).
- Transaction processing is the management of transactions in a distributed system, such as a web application that uses enterprise java beans (EJBs).
- EJBs are server-side components that encapsulate the business logic of an application and can be accessed remotely by clients.
- EJBs can participate in transactions to ensure data integrity and consistency across multiple data sources, such as databases, message queues, or web services.
- There are two types of transactions in EJBs: container-managed transactions (CMT) and bean-managed transactions (BMT).
- In CMT, the EJB container sets the boundaries of the transactions and controls their propagation, commit, and rollback. The developer can specify the transaction attributes of each EJB method using annotations or deployment descriptors.
- In BMT, the EJB code explicitly marks the boundaries of the transactions using the Java Transaction API (JTA). The developer can obtain a reference to the UserTransaction interface and invoke its methods to begin, commit, or rollback a transaction.
- CMT simplifies development and reduces the complexity of transaction management, but BMT gives more flexibility and control to the developer. CMT is required for entity beans, but BMT can be used with session or message-driven beans.
- EJBs support flat transactions, which means that each transaction is independent of other transactions in the system. Nested transactions, which allow a transaction to be composed of subtransactions, are not supported by the EJB specification.
- EJBs use the two-phase commit protocol to coordinate transactions across multiple XA resources, such as databases or message queues. The protocol ensures that all resources either commit or rollback the transaction in a consistent manner.