## Unit 4 - Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side component architecture that provides a powerful infrastructure for building distributed, scalable, and secure enterprise applications. In this unit, we will learn about the fundamentals of EJB and its various types.

### Overview of EJB

- EJB is a component architecture that provides a standard way to develop and deploy enterprise applications on a Java EE platform.
- It provides a set of services such as transaction management, security, and persistence that can be used by enterprise applications.
- EJB components are server-side components that run in an EJB container, which provides a runtime environment for the components.

### Types of EJB

There are three types of EJBs:

1. Session Beans
- Session beans are used to implement business logic in an enterprise application.
- They can be stateless, stateful, or singleton.
- Stateless session beans do not maintain any conversational state between client invocations, stateful session beans maintain conversational state, and singleton session beans are designed to be used by all clients in the application.

2. Message-Driven Beans
- Message-driven beans are used to process messages asynchronously in enterprise applications.
- They are designed to interact with JMS (Java Message Service) providers to receive and process messages.

3. Entity Beans
- Entity beans are used to represent persistent data in an enterprise application.
- They are used to interact with a database and provide a way to map Java objects to database tables.

### EJB Container

- The EJB container provides a runtime environment for EJB components.
- It provides services such as transaction management, security, and persistence to the components.
- The container is responsible for managing the lifecycle of EJB components and providing access to the components from clients.

### Benefits of EJB

- EJB provides a standard way to develop and deploy enterprise applications.
- It provides a set of services such as transaction management, security, and persistence that can be used by enterprise applications.
- EJB components are scalable and can be distributed across multiple servers.
- EJB provides a way to implement business logic in an enterprise application, which can be easily maintained and updated.

In conclusion, EJB is a powerful component architecture that provides a standard way to develop and deploy enterprise applications. It provides a set of services that can be used by enterprise applications and allows for the implementation of business logic in a scalable and distributed manner. Understanding the fundamentals of EJB and its various types is essential for building robust and scalable enterprise applications.