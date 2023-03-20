## Unit 4 - Enterprise Java Bean

Enterprise Java Bean (EJB) is a server-side component architecture used for building scalable, distributed, and transactional applications in Java. EJB provides a way to encapsulate business logic in reusable components that can be deployed on a Java EE application server.

Here are some key concepts to understand in EJB:

### Types of EJBs

1. Session Beans: These are used to encapsulate business logic that can be called by a client. 
   - There are two types of session beans: Stateless and Stateful.
   - Stateless beans are used for simple tasks that do not require a persistent state. 
   - Stateful beans are used for tasks that require a persistent state, like a shopping cart in an e-commerce application.
2. Entity Beans: These represent persistent data stored in a database. 
   - They can be used to perform CRUD (create, read, update, delete) operations on the underlying database tables.
3. Message-Driven Beans: These are used for asynchronous messaging between components in a distributed system. 
   - They can be used to handle messages from a JMS (Java Message Service) queue or topic.

### EJB Container

The EJB container is responsible for managing the lifecycle of EJB instances, including creating, activating, passivating, and destroying them. The container also provides services like transaction management, security, and concurrency control.

### Annotations

Annotations are used to provide metadata to the EJB container, which is used to configure and manage the EJB instances. Some commonly used annotations in EJB are:

- @Stateless: Used to annotate a Stateless Session Bean.
- @Stateful: Used to annotate a Stateful Session Bean.
- @Entity: Used to annotate an Entity Bean.
- @MessageDriven: Used to annotate a Message-Driven Bean.

### Transactions

EJB provides support for distributed transactions, which allows multiple resources to participate in a single transaction. This ensures that all the changes made to the resources are either committed or rolled back together, ensuring data integrity.

### Security

EJB provides a way to secure the components using the Java EE security model. This includes authentication, authorization, and confidentiality.

### Concurrency

EJB provides support for concurrency control, which ensures that multiple clients can access the EJB components in a safe and controlled manner. 

Overall, EJB provides a powerful and flexible way to build scalable and distributed applications in Java. Understanding the key concepts and features of EJB is essential for building robust and reliable enterprise applications.