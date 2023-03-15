## Unit 4 - Enterprise Java Bean

An Enterprise Java Bean (EJB) is a server-side component that encapsulates the business logic of an application. It is written in the Java programming language and runs inside an EJB container, which provides middleware services such as security, transaction management, concurrency, dependency injection, etc. to the EJBs.

There are three types of EJBs:

- **Session beans**: These are non-persistent objects that represent a single client-server interaction. They can be stateless, stateful, or singleton. Stateless session beans do not maintain any conversational state with the client, and can be pooled and reused by different clients. Stateful session beans maintain a conversational state with the client, and are bound to a single client for the duration of the session. Singleton session beans are instantiated once per application and shared by all clients.
- **Entity beans**: These are persistent objects that represent the data stored in a database. They can be container-managed or bean-managed. Container-managed entity beans delegate the persistence operations to the EJB container, which uses a mapping file to map the entity fields to the database columns. Bean-managed entity beans implement the persistence operations themselves, using JDBC or JPA APIs. Note that entity beans are deprecated in EJB 3.2 and replaced by JPA entities.
- **Message-driven beans**: These are stateless objects that act as message consumers and process messages asynchronously. They implement the javax.jms.MessageListener interface and receive messages from a JMS provider or other messaging systems.

To create an EJB, you need to follow these steps:

- Write a Java class with the appropriate annotations from the javax.ejb package, such as @Stateless, @Stateful, @Singleton, @MessageDriven, etc. You can also optionally define an interface for the EJB, which can be local or remote. Local interfaces are used for intra-application communication, while remote interfaces are used for inter-application communication.
- Package the EJB class and its interface (if any) in a JAR file with an ejb-jar.xml deployment descriptor, which specifies the EJB name, type, and other configuration parameters.
- Deploy the JAR file to an EJB container, which will register the EJB and make it available for invocation by clients.

Here is an example of a stateless session bean that implements a simple calculator service:

```java
// Calculator.java
// A local interface for the calculator bean
package com.example.ejb;

import javax.ejb.Local;

@Local
public interface Calculator {
    public int add(int a, int b);
    public int subtract(int a, int b);
    public int multiply(int a, int b);
    public int divide(int a, int b);
}
```

```java
// CalculatorBean.java
// A stateless session bean that implements the calculator interface
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

```xml
<!-- ejb-jar.xml -->
<!-- A deployment descriptor for the calculator bean -->
<?xml version="1.0" encoding="UTF-8"?>
<ejb-jar xmlns="http://java.sun.com/xml/ns/javaee" version="3.1">
    <enterprise-beans>
        <session>
            <ejb-name>CalculatorBean</ejb-name>
            <ejb-class>com.example.ejb.CalculatorBean</ejb-class>
            <session-type>Stateless</session-type>
            <local>com.example.ejb.Calculator</local>
        </session>
    </enterprise-beans>
</ejb-jar>
```

To use the calculator bean from a client, you need to obtain a reference to it using the JNDI API or dependency injection, and then invoke its methods as usual. For example:

```java
// CalculatorClient.java
// A client that uses the calculator bean
package com.example.client;

import javax.ejb.EJB;
import javax.naming.InitialContext;
import javax.naming.NamingException;

import com.example.ejb.Calculator;

public class CalculatorClient {
    // Inject the calculator bean