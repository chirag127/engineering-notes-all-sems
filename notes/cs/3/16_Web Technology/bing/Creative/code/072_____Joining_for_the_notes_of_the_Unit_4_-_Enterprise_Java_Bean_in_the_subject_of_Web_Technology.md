Hello, I am Sydney, your AI assistant. I can help you with the notes of Unit 4 - Enterprise Java Bean in the subject of Web Technology. Here is the content in markdown format:

### Enterprise Java Bean

- Enterprise Java Bean (EJB) is a server-side component that encapsulates the business logic of an application.
- EJB is a part of the Java Platform, Enterprise Edition (Java EE) that provides a standard architecture for developing and deploying distributed applications.
- EJB can be used to implement various types of business components, such as session beans, entity beans, message-driven beans, and singleton beans.
- EJB provides various services to the business components, such as transaction management, security, concurrency, dependency injection, naming, and persistence.
- EJB can be accessed by clients using different protocols, such as Remote Method Invocation (RMI), Java Message Service (JMS), Java Naming and Directory Interface (JNDI), and web services.

#### Session Beans

- Session beans are stateful or stateless components that represent the actions of a single client.
- Stateful session beans maintain the conversational state of the client across multiple method invocations.
- Stateless session beans do not maintain any state and can be shared by multiple clients.
- Session beans can be annotated with `@Stateful` or `@Stateless` to indicate their type.
- Session beans can implement one or more business interfaces that define the methods exposed to the clients.
- Session beans can also implement lifecycle callback methods that are invoked by the container at certain events, such as creation, activation, passivation, and removal.

#### Entity Beans

- Entity beans are persistent components that represent the data of the application.
- Entity beans can be mapped to relational database tables using the Java Persistence API (JPA).
- Entity beans can be annotated with `@Entity` to indicate their type.
- Entity beans can have one or more fields that are annotated with `@Id` to indicate the primary key.
- Entity beans can also have fields that are annotated with `@Column`, `@OneToOne`, `@OneToMany`, `@ManyToOne`, or `@ManyToMany` to indicate the mapping to the database columns or relationships.
- Entity beans can also implement lifecycle callback methods that are invoked by the container at certain events, such as persist, update, remove, and load.

#### Message-Driven Beans

- Message-driven beans are components that process asynchronous messages from a message queue or topic.
- Message-driven beans can be annotated with `@MessageDriven` to indicate their type.
- Message-driven beans can implement the `javax.jms.MessageListener` interface that defines the `onMessage` method to handle the incoming messages.
- Message-driven beans can also implement lifecycle callback methods that are invoked by the container at certain events, such as creation, activation, passivation, and removal.

#### Singleton Beans

- Singleton beans are components that are instantiated only once per application and shared by all clients.
- Singleton beans can be annotated with `@Singleton` to indicate their type.
- Singleton beans can implement one or more business interfaces that define the methods exposed to the clients.
- Singleton beans can also implement lifecycle callback methods that are invoked by the container at certain events, such as creation, initialization, destruction, and shutdown.
- Singleton beans can also be annotated with `@Startup` to indicate that they should be initialized at the application startup.
- Singleton beans can also be annotated with `@Lock` to indicate the concurrency level of the methods, such as `READ` or `WRITE`.