## Unit 4 - Enterprise Java Bean

- Enterprise Java Bean (EJB) is a server-side component architecture for Java Platform, Enterprise Edition (Java EE)  .
- EJB technology enables rapid and simplified development of distributed, transactional, secure and portable applications based on Java technology  .
- There are three types of enterprise beans, entity beans, session beans, and message-driven beans .
- Entity beans represent persistent data stored in a database. They can be accessed and updated by multiple clients .
- Session beans encapsulate business logic and perform tasks for a client. They can be stateful or stateless .
- Message-driven beans process messages asynchronously from a message queue or topic. They act as message consumers and listeners .
- EJB 3.0 was introduced with Java EE 5 in 2006. It greatly simplified development by introducing the use of Java annotations, by making XML deployment descriptors optional and by adopting a convention-over-configuration approach .
- EJB 3.0 also included the Java Persistence API (JPA) for persistence and object/relational mapping with Java EE and Java SE .
- EJB 3.1 (part of Java EE 6 and released in 2009) introduced a multitude of new features, such as :
  - A "no interface" local view for session beans
  - Simplified packaging and deployment of EJB components directly in a web archive (.war)
  - An embeddable API for executing EJB components within a Java SE environment
  - A new singleton component
  - Calendar based EJB Timer expressions
  - Asynchronous session bean invocations
  - A portable global JNDI name syntax for looking up EJB components
  - The definition of a lightweight subset of EJB functionality that can be provided within the Java EE Web Profile
- EJB components are deployed in an EJB container, which provides services such as security, transaction management, concurrency control, dependency injection, naming, pooling, and lifecycle management  .
- EJB components can communicate with each other and with other Java EE components using various protocols, such as RMI, JMS, SOAP, REST, and CORBA  .
- EJB components can be annotated with various EJB-specific annotations, such as [@Stateless](https://docs.oracle.com/javaee/7/api/javax/ejb/Stateless.html), [@Stateful](https://docs.oracle.com/javaee/7/api/javax/ejb/Stateful.html), [@Singleton](https://docs.oracle.com/javaee/7/api/javax/ejb/Singleton.html), [@MessageDriven](https://docs.oracle.com/javaee/7/api/javax/ejb/MessageDriven.html), [@Remote](https://docs.oracle.com/javaee/7/api/javax/ejb/Remote.html), [@Local](https://docs.oracle.com/javaee/7/api/javax/ejb/Local.html), [@EJB](https://docs.oracle.com/javaee/7/api/javax/ejb/EJB.html), [@Resource](https://docs.oracle.com/javaee/7/api/javax/annotation/Resource.html), [@PostConstruct](https://docs.oracle.com/javaee/7/api/javax/annotation/PostConstruct.html), and [@PreDestroy](https://docs.oracle.com/javaee/7/api/javax/annotation/PreDestroy.html)  .
- EJB components can also use XML deployment descriptors to configure their properties and dependencies, such as ejb-jar.xml and persistence.xml  .
- EJB components can be accessed by clients using various methods, such as JNDI lookup, dependency injection, service locator, and remote interface  .

### Example of a stateless session bean

```java
// Annotate the class with @Stateless to indicate that it is a stateless session bean
@Stateless
// Annotate the class with @Remote to indicate that it exposes a remote interface
@Remote(Calculator.class)
// Implement the remote interface
public class CalculatorBean implements Calculator {
  // Implement the business methods defined in the interface
  public int add(int a, int b) {
    return a + b;
  }

  public int subtract(int a, int b) {
    return a