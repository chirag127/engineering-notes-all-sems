## Unit 4 - Enterprise Java Bean

- An enterprise bean is a Java component that can be combined with other resources to create Java applications  .
- An enterprise bean encapsulates the business logic of an application, which is the code that fulfills the purpose of the application .
- Enterprise beans run on the server side and are managed by the enterprise bean container, which provides services such as security, transaction management, concurrency control, and dependency injection   .
- There are three types of enterprise beans: session beans, entity beans, and message-driven beans   .
  - Session beans are non-persistent objects that represent a single client-server interaction or a conversational state  .
  - Entity beans are persistent objects that represent the data stored in a database or another persistent storage  .
  - Message-driven beans are asynchronous objects that act as message consumers and process messages from a message queue or a topic  .
- Enterprise beans are written using annotations or deployment descriptors to specify the bean type, the interfaces it implements, the services it requires, and other configuration details  .
- Enterprise beans can be accessed by local or remote clients using the Java Naming and Directory Interface (JNDI) or dependency injection  .
- Enterprise beans can use other Java EE technologies such as Java Persistence API (JPA), Java Transaction API (JTA), Java Message Service (JMS), Java Authentication and Authorization Service (JAAS), and Java API for RESTful Web Services (JAX-RS) to implement their functionality  .
- Enterprise beans are part of the Jakarta Enterprise Beans (EJB) specification, which is the server-side component architecture for Java Platform, Enterprise Edition (Java EE) or Jakarta EE  .
- EJB 3.0 was introduced with Java EE 5 in 2006 and simplified the development of enterprise beans by using annotations, dependency injection, and convention over configuration .