### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) is a server-side component architecture for building modular, scalable, and secure enterprise applications. There are three types of beans in EJB:

1. **Session Beans**: These beans represent a single client inside the Application Server. They can be either stateful or stateless. Stateful session beans maintain the conversational state with the client, while stateless session beans do not.

2. **Entity Beans**: These beans represent persistent data stored in a database. They can be either container-managed or bean-managed. Container-managed entity beans allow the container to manage the persistence, while bean-managed entity beans require the developer to manage the persistence.

3. **Message-Driven Beans**: These beans are used to process messages asynchronously. They act as a listener for a particular messaging type, such as Java Message Service (JMS).

Each type of bean has its own advantages and disadvantages, and the choice of bean type depends on the specific requirements of the application. For example, session beans are suitable for implementing business logic, while entity beans are suitable for representing data in a database. Message-driven beans are suitable for processing messages asynchronously.