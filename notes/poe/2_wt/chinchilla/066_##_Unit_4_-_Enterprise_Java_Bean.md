## Unit 4 - Enterprise Java Bean

Enterprise Java Beans (EJBs) are server-side components that are used for developing distributed applications. They provide a standardized way to build scalable, transactional, and secure applications. EJBs are part of the Java EE specification and can be deployed on any application server that supports the Java EE platform.

### Types of Enterprise Java Beans

There are three types of EJBs:

1. Session Beans: Session beans are used for implementing business logic and represent a single client session. There are two types of session beans:
   - Stateless Session Beans: These beans do not maintain any client-specific state and are used for processing independent requests.
   - Stateful Session Beans: These beans maintain client-specific state and are used for processing a series of related requests.

2. Message-Driven Beans: Message-driven beans are used for processing messages asynchronously. They are triggered by messages sent to a specific destination (such as a queue or topic) and perform tasks based on the content of the message.

3. Entity Beans: Entity beans represent persistent data in a database and are used for managing data access. However, entity beans were deprecated in Java EE 6 and are no longer recommended for use.

### EJB Architecture

The EJB architecture consists of three layers:

1. Client Layer: This layer consists of the client application that uses EJBs to access business logic.

2. EJB Container Layer: This layer consists of the EJB container, which provides services such as transaction management, security, and resource pooling.

3. Enterprise Information System (EIS) Layer: This layer consists of the data sources and other external systems that are accessed by the EJBs.

### Advantages of Using EJBs

- EJBs provide a standardized way to develop distributed applications.
- They provide a high level of scalability, as they can be deployed on multiple servers to handle large amounts of traffic.
- EJBs provide transaction management, which ensures that database operations are performed atomically.
- They provide security features such as authentication and authorization.
- EJBs can be easily integrated with other Java EE technologies such as JPA and JMS.

### Disadvantages of Using EJBs

- EJBs can be complex to develop and deploy, requiring a significant amount of configuration.
- They can also be slower than other technologies due to the overhead of the EJB container.
- EJBs are tightly coupled with the Java EE platform, making them less portable.

### Learning Tricks and Mnemonics

- Remember the three types of EJBs with the acronym SME: Stateless Session Beans, Message-Driven Beans, and Entity Beans (deprecated).
- Think of the EJB architecture as a sandwich, with the client layer as the bread, the EJB container layer as the filling, and the EIS layer as the other slice of bread.