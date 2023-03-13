## Unit 4 - Enterprise Java Bean

- Enterprise Java Beans (EJB) are server-side components that encapsulate the business logic of an application.
- EJBs are managed by an EJB container, which provides services such as security, transaction management, concurrency control, dependency injection, and remote access.
- EJBs can be of two types: session beans and message-driven beans.
- Session beans are stateful or stateless components that handle requests from clients. Stateful session beans maintain a conversational state with the client, while stateless session beans do not. Session beans can also be singleton, which means only one instance exists in the application.
- Message-driven beans are components that asynchronously process messages from a message queue or a topic. Message-driven beans do not have any state or conversational context with the client.
- EJBs can be accessed by local or remote clients using either Java Naming and Directory Interface (JNDI) or dependency injection. Local clients are in the same Java Virtual Machine (JVM) as the EJB, while remote clients are in a different JVM or a different machine.
- EJBs can use annotations or XML descriptors to specify their configuration and metadata, such as the type of the bean, the interfaces it implements, the transaction attributes, the security roles, and the lifecycle callbacks.
- EJBs can interact with other components and resources using the Java EE APIs, such as Java Persistence API (JPA), Java Transaction API (JTA), Java Message Service (JMS), JavaMail, Java Authentication and Authorization Service (JAAS), and Java Connector Architecture (JCA).
- EJBs can also use interceptors, which are classes that intercept the invocation of a method on an EJB and perform some pre-processing or post-processing logic. Interceptors can be used for logging, auditing, security, caching, or validation purposes.