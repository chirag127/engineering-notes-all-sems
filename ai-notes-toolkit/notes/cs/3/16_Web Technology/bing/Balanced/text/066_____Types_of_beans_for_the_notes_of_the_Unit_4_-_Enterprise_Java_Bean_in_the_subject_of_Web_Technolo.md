### Types of beans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- Enterprise Java Beans (EJB) are Java components that can be combined with other resources to create Java applications.
- EJB encapsulate the business logic of an application and can be invoked by local, remote or web service clients.
- There are three types of EJB: session beans, entity beans and message-driven beans  .
- Session beans are EJB that contain business logic that can be invoked programmatically by a client. They do not persist data or represent objects in a database.
- There are three types of session beans: stateless, stateful and singleton  .
  - Stateless session beans do not maintain a conversational state with the client. They are pooled and reused by the container for different clients.
  - Stateful session beans maintain a conversational state with the client. They are not pooled and are associated with a specific client for the duration of the session.
  - Singleton session beans are instantiated once per application and are shared by all clients. They can be used for caching or global configuration purposes.
- Entity beans are EJB that persist data and represent objects in a database. They can be accessed by multiple clients and support transactions and concurrency control.
- There are two types of entity beans: container-managed persistence (CMP) and bean-managed persistence (BMP) .
  - CMP entity beans delegate the persistence logic to the container, which generates the database access code automatically.
  - BMP entity beans implement the persistence logic in the bean class, which requires the developer to write the database access code manually.
- Message-driven beans are EJB that process messages asynchronously from a message queue or topic. They act as message consumers and can implement the Java Message Service (JMS) API or other messaging APIs  .
- Message-driven beans are similar to stateless session beans in that they do not maintain a state and are pooled by the container. However, they do not have a home or remote interface and are invoked by the container when a message arrives.