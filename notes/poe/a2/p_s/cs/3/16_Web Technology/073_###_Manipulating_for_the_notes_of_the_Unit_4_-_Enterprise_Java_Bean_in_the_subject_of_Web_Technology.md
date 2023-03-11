 Here is the content in markdown format for the topic ### Manipulating for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology:

### Enterprise JavaBeans (EJB)

- Enterprise JavaBeans (EJB) is a development architecture for server-side business applications in Java EE.
- EJBs support transactions, security, scalability, multi-threading, and remote access.
- Types of EJBs:
    - Session Beans: Used for task processing. Stateless and Stateful beans.
    - Message-Driven Beans: Used to process JMS messages asynchronously.
    - Entity Beans: Used to map database tables to objects, but deprecated.
- Annotations can be used instead of deployment descriptors to configure EJBs.
- Interfaces: Local, Remote, and No-interface views. Local interfaces provide better performance while remote interfaces provide location transparency.
- Stateless session beans are lightweight, scalable, and can serve multiple clients concurrently. Load balancing can be achieved by replicating them.
- Stateful session beans maintain conversational state across client calls. Useful for sessions and shopping carts.
- Message-driven beans contain business logic that reacts to messages. They are asynchronous and scalable.
- Transactions: Container-managed (CMT) or Bean-managed (BMT) transactions can be used with EJBs.
- Security: EJBs support authentication, authorization, and role-based access control using Java EE security.
- Example: A stateless session bean can be used to query a database and return results to the client. A message-driven bean can process files uploaded by clients.

[Diagrams and codes can be added here if helpful for understanding the concepts]

[Advantages, disadvantages, and applications of EJBs can be discussed here in points]