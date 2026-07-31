### Types of beans for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology

- An enterprise bean is a Java component that can be combined with other resources to create Java applications.
- There are three types of enterprise beans: session beans, entity beans, and message-driven beans  .
- Session beans encapsulate business logic that can be invoked by local, remote or web service clients  .
- There are three subtypes of session beans: stateless, stateful, and singleton .
- Stateless session beans do not maintain a conversational state with the client and can be reused by multiple clients  .
- Stateful session beans maintain a conversational state with the client and are bound to a specific client during their lifetime  .
- Singleton session beans are instantiated once per application and are shared by all clients .
- Entity beans represent persistent data stored in a database and can be accessed by multiple clients  .
- There are two subtypes of entity beans: container-managed persistence (CMP) and bean-managed persistence (BMP) .
- CMP entity beans delegate the responsibility of managing the persistence to the container .
- BMP entity beans implement the persistence logic in the bean code .
- Message-driven beans process messages asynchronously from a message queue or topic   .
- Message-driven beans implement the javax.jms.MessageListener interface and receive messages from a Java Message Service (JMS) provider  .
- Message-driven beans are stateless and can be pooled by the container for better scalability .