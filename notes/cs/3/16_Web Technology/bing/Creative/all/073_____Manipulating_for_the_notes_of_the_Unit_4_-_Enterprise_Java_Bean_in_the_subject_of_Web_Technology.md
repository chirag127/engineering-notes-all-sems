# Manipulating Enterprise Java Beans

Enterprise Java Beans (EJB) are server-side components that encapsulate the business logic of an enterprise application. They are part of the Java Platform, Enterprise Edition (Java EE) and provide a standard way of developing distributed, transactional, secure and portable applications based on Java technology.

There are three types of enterprise beans:

- **Session beans** represent the actions or interactions of a client with the application. They are stateful or stateless and can be accessed by local or remote clients. They can also be used as web service endpoints.
- **Entity beans** represent the persistent data or objects of the application. They are mapped to database tables and can be accessed by local or remote clients. They can also use Java Persistence API (JPA) for object-relational mapping.
- **Message-driven beans** represent the asynchronous processing of messages from a message queue or topic. They are stateless and can be accessed by local or remote clients. They can also implement the Java Message Service (JMS) API for messaging.

To manipulate enterprise beans, the following steps are required:

- **Create** the enterprise bean class and annotate it with the appropriate bean type annotation, such as `@Stateless`, `@Stateful`, `@Entity` or `@MessageDriven`.
- **Implement** the business methods and interfaces of the enterprise bean, such as `@Remote`, `@Local`, `@WebService`, `@PostConstruct`, `@PreDestroy`, `@PersistenceContext` or `@Resource`.
- **Package** the enterprise bean class and its dependencies in an EJB module, which is a Java archive (JAR) file with an `ejb-jar.xml` deployment descriptor.
- **Deploy** the EJB module to an application server that supports the EJB specification, such as GlassFish, WildFly, WebLogic or WebSphere.
- **Access** the enterprise bean from a client application, such as a web application, a standalone Java application, a web service client or a JMS client. The client can use various mechanisms to locate and invoke the enterprise bean, such as JNDI, dependency injection, service locator or EJB home interface.