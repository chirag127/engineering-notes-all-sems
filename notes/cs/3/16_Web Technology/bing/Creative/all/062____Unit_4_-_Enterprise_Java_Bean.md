# Unit 4 - Enterprise Java Bean

- Enterprise Java Bean (EJB) is a technology for developing scalable, robust and secure enterprise applications in Java .
- EJB applications run inside an EJB container, which provides middleware services such as security, transaction management, concurrency, dependency injection, etc .
- EJB applications can use three types of beans: session beans, entity beans and message-driven beans .
  - Session beans are used to implement business logic and can be stateless or stateful .
  - Entity beans are used to persist data and can be container-managed or bean-managed.
  - Message-driven beans are used to process asynchronous messages from a message queue or topic .
- EJB applications can use annotations from the EJB specification to define the bean type, lifecycle, transaction attributes, etc .
- EJB applications can communicate with other components using remote or local interfaces, or use dependency injection to access other beans .
- EJB applications can use Java Persistence API (JPA) to access relational databases and map entities to tables.
- EJB applications can use Java Message Service (JMS) to send and receive messages from message-oriented middleware.
- EJB applications can use Java Naming and Directory Interface (JNDI) to look up resources and services in the application server.
- EJB applications can use Java Transaction API (JTA) to manage distributed transactions across multiple resources.
- EJB applications can use Java Authentication and Authorization Service (JAAS) to implement security features such as authentication, authorization and auditing.