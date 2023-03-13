## Unit 4 - Enterprise Java Bean

- Enterprise Java Bean (EJB) is a Java API for modular construction of enterprise software.
- EJB is a server-side software component that encapsulates business logic of an application .
- EJB enables rapid and simplified development of distributed, transactional, secure and portable applications based on Java technology .
- EJB runs inside an EJB container, which provides services such as dependency injection, security, concurrency, transaction management, and lifecycle management.
- There are three types of EJBs, each with a different purpose and lifecycle:
  - Session beans: represent the business logic or behavior of an application. They can be stateless, stateful, or singleton.
  - Entity beans: represent the persistent data or state of an application. They can be container-managed or bean-managed.
  - Message-driven beans: represent the asynchronous communication or integration of an application. They act as message consumers and process messages from a message queue or topic.
- EJB can be accessed by local or remote clients, such as web components, other EJBs, or standalone Java applications .
- EJB can be annotated with one or more annotations from the EJB spec, such as @Stateless, @Stateful, @Singleton, @Entity, @MessageDriven, @Remote, @Local, etc.
- EJB can be packaged in a Java archive (JAR) file or a web archive (WAR) file, and deployed to an application server that supports the EJB specification .

Some mnemonics and learning tricks for EJB are:

- EJB = Enterprise Java Bean = Easy Java Business
- Session beans = Stateful, Stateless, or Singleton
- Entity beans = Container-managed or Bean-managed
- Message-driven beans = Message consumers
- EJB container = Services provider
- EJB annotations = @Stateless, @Stateful, @Singleton, @Entity, @MessageDriven, etc
- EJB package = JAR or WAR
- EJB server = Application server