### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side component architecture for the Java Platform, Enterprise Edition (Java EE). There are three types of beans in EJB:

1. **Session Beans**: These beans represent the business logic of an application and can be either stateful or stateless. Stateful session beans maintain state across multiple method invocations, while stateless session beans do not.

2. **Entity Beans**: These beans represent persistent data and are used to manage the interactions between the application and the database. Entity beans can be either container-managed or bean-managed.

3. **Message-Driven Beans**: These beans are used to process messages asynchronously. They act as a listener for a particular messaging type, such as Java Message Service (JMS), and perform some action when a message is received.

Each type of bean has its own specific use case and can be used in combination to build robust and scalable enterprise applications.