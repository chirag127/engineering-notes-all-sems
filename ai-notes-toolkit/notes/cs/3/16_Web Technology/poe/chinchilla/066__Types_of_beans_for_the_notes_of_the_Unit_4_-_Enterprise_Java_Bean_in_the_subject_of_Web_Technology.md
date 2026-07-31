### Types of Beans

Enterprise Java Beans (EJB) is a specification for building scalable, distributed, and transactional business applications. EJB technology allows developers to create reusable components that can be deployed on any EJB container.

There are three types of EJBs:

1. Session Beans
   - A session bean is a non-persistent object that represents a client's interaction with an application.
   - There are two subtypes of session beans: stateless and stateful.
   - Stateless session beans don't maintain conversational state between method calls, while stateful session beans maintain state across multiple method calls.
   - Session beans are used to encapsulate business logic and provide a simplified interface to clients.

2. Entity Beans
   - An entity bean represents a persistent data object.
   - Entity beans can be either container-managed or bean-managed.
   - In container-managed persistence, the container manages the persistence of the entity bean, while in bean-managed persistence, the developer has to manage the persistence.

3. Message-driven Beans
   - A message-driven bean is a type of EJB that enables Java EE applications to consume messages asynchronously from message queues.
   - Message-driven beans are used for processing messages in a decoupled manner, allowing the application to scale more easily.

In conclusion, EJB technology provides developers with a powerful toolset for building scalable and transactional business applications. Understanding the different types of EJBs and their use cases is essential for building robust and efficient applications.