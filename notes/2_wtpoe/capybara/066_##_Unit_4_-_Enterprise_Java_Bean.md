## Unit 4 - Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side component architecture for Java EE applications. It provides a standard way to develop distributed, scalable, and transactional Java applications. In this unit, we will learn about the following topics:

1. Introduction to EJB
   - EJB Architecture
   - EJB Types
   - EJB Container

2. Session Beans
   - Stateless Session Beans
   - Stateful Session Beans
   - Singleton Session Beans

3. Entity Beans
   - Container-Managed Persistence (CMP)
   - Bean-Managed Persistence (BMP)

4. Message-Driven Beans
   - Asynchronous Processing
   - Message-Driven Bean Lifecycle

5. EJB QL (Query Language)

### Introduction to EJB

EJB is a server-side component architecture that allows developers to build distributed, scalable, and transactional Java applications. It provides a standard way to develop enterprise applications that run on Java EE servers. EJB has three types:

- Session Beans: It is used to implement business logic and represent a single client.
- Entity Beans: It is used to represent persistent data and is managed by a container.
- Message-Driven Beans: It is used to process messages asynchronously.

The EJB architecture consists of the following:

- EJB Container: It provides the runtime environment for EJB components.
- Enterprise Beans: It represents a business object that can be used by clients.
- EJB Clients: It is an application that accesses EJB components.

### Session Beans

Session Beans are used to implement business logic and are available in three types: Stateless Session Beans, Stateful Session Beans, and Singleton Session Beans.

- Stateless Session Beans: It is used when the session state is not required to be maintained between method calls.
- Stateful Session Beans: It is used when the session state needs to be maintained between method calls.
- Singleton Session Beans: It is used when there is a need for a single instance of a session bean in an application.

### Entity Beans

Entity Beans are used to represent persistent data and are managed by a container. It is available in two types: Container-Managed Persistence (CMP) and Bean-Managed Persistence (BMP).

- Container-Managed Persistence (CMP): It is used when the container manages the persistence of the entity bean.
- Bean-Managed Persistence (BMP): It is used when the bean manages the persistence of the entity bean.

### Message-Driven Beans

Message-Driven Beans are used to process messages asynchronously. It is used in scenarios where there is a need for asynchronous processing of messages.

### EJB QL (Query Language)

EJB QL is used to query entity beans. It is similar to SQL but has some differences in syntax and semantics. EJB QL helps in abstracting the underlying database and provides a standard way of querying entity beans.

That's it for Unit 4 - Enterprise Java Bean. Understanding the concepts of EJB is essential for building scalable and distributed Java applications. Practice coding examples and solve problems to gain proficiency in EJB.