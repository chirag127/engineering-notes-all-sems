## Unit 4 - Enterprise Java Bean

- Enterprise Java Bean (EJB) is a technology for developing scalable, robust and secure enterprise applications in Java .
- EJB is a server-side component that encapsulates the business logic of an application.
- EJB provides middleware services such as security, transaction management, concurrency, dependency injection, naming and remote invocation to all EJB applications .
- EJB applications run inside an EJB container, which is a part of a Java EE application server such as JBoss, WebLogic, GlassFish, etc  .
- EJB applications can be accessed by clients using various protocols such as HTTP, RMI, SOAP, etc.
- EJB applications can interact with other Java EE components such as servlets, JSPs, web services, etc.
- EJB applications can use various Java EE APIs such as JDBC, JPA, JMS, JNDI, etc.

### Types of EJBs

- There are three types of EJBs: session beans, entity beans and message-driven beans  .
- Session beans are used to implement the business logic or workflow of an application. They are stateful or stateless, depending on whether they maintain a conversational state with the client or not  .
- Entity beans are used to represent persistent data in a relational database. They are deprecated in EJB 3.0 and replaced by Java Persistence API (JPA) entities  .
- Message-driven beans are used to process asynchronous messages from a message queue or topic. They are stateless and act as message consumers or listeners  .

### EJB Annotations

- EJB annotations are used to mark a Java class as an EJB and specify its type and properties.
- Some common EJB annotations are:

| Annotation | Description | Example |
|------------|-------------|---------|
| @Stateless | Marks a class as a stateless session bean | @Stateless public class CalculatorBean implements Calculator { ... } |
| @Stateful | Marks a class as a stateful session bean | @Stateful public class ShoppingCartBean implements ShoppingCart { ... } |
| @Singleton | Marks a class as a singleton session bean | @Singleton public class LoggerBean implements Logger { ... } |
| @MessageDriven | Marks a class as a message-driven bean | @MessageDriven(activationConfig = { @ActivationConfigProperty(propertyName = "destinationType", propertyValue = "javax.jms.Queue"), @ActivationConfigProperty(propertyName = "destination", propertyValue = "java:/jms/queue/OrderQueue") }) public class OrderProcessorBean implements MessageListener { ... } |
| @Remote | Marks an interface as a remote business interface for an EJB | @Remote public interface Calculator { ... } |
| @Local | Marks an interface as a local business interface for an EJB | @Local public interface ShoppingCart { ... } |
| @EJB | Injects a reference to another EJB | @EJB private Logger logger; |

### EJB Example

- The following example shows a simple EJB application that implements a calculator service using a stateless session bean and a remote interface.

- The remote interface Calculator.java defines the methods for the calculator service:

```java
// Calculator.java
package com.example.ejb;

import javax.ejb.Remote;

@Remote
public interface Calculator {
    public int add(int a, int b);
    public int subtract(int a, int b);
    public int multiply(int a, int b);
    public int divide(int a, int b);
}
```

- The stateless session bean CalculatorBean.java implements the calculator service:

```java
// CalculatorBean.java
package com.example.ejb;

import javax.ejb.Stateless;

@Stateless
public class CalculatorBean implements Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public int subtract(int a, int b) {
        return a - b;
    }

    public int multiply(int a, int b) {
        return a * b;
    }

    public int divide(int a, int b) {
        return a / b;
    }
}
```

- The client class CalculatorClient.java invokes the calculator service using JNDI lookup