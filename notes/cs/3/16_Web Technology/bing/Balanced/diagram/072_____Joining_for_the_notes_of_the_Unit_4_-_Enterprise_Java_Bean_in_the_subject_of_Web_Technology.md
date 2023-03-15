Hello, I am Sydney, your AI assistant. I can help you with the notes of Unit 4 - Enterprise Java Bean in the subject of Web Technology. Here is a brief overview of the topic:

### Enterprise Java Bean

- Enterprise Java Bean (EJB) is a server-side component model for developing and deploying distributed business applications in Java.
- EJBs are managed by an EJB container, which provides services such as security, transaction management, concurrency control, dependency injection, and remote access.
- EJBs can be of two types: session beans and message-driven beans.
- Session beans are stateful or stateless components that encapsulate the business logic of an application. They can be accessed by local or remote clients using Java interfaces.
- Message-driven beans are stateless components that act as message consumers and process messages asynchronously from a message queue or topic. They implement the javax.jms.MessageListener interface and are invoked by the EJB container when a message arrives.
- EJBs can use annotations or XML descriptors to specify their configuration and deployment properties, such as the bean type, the interfaces, the transaction attributes, the security roles, and the resource references.
- EJBs can interact with other components and resources using the Java Naming and Directory Interface (JNDI), the Java Persistence API (JPA), the Java Transaction API (JTA), the Java Message Service (JMS), and the Java API for RESTful Web Services (JAX-RS).
- EJBs can be packaged in a Java archive (JAR) file or a web archive (WAR) file, and deployed to an EJB container that runs on an application server, such as GlassFish, WildFly, or WebLogic.