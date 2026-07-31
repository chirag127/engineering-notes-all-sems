Hello, I am Sydney, your AI assistant. I can help you with various tasks and topics. You have asked me to write code for types of beans in Enterprise Java Bean. Here is my answer:

### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) are server-side components that encapsulate the business logic of an application. There are three types of beans in EJB:

- **Session beans**: These are non-persistent objects that provide services to clients. They can be stateless or stateful. Stateless session beans do not maintain any conversational state with the client, while stateful session beans do. Session beans can also be singleton, which means there is only one instance of the bean in the application.
- **Entity beans**: These are persistent objects that represent the data stored in a database. They can be container-managed or bean-managed. Container-managed entity beans delegate the responsibility of managing the persistence to the EJB container, while bean-managed entity beans handle it themselves. Entity beans are deprecated since EJB 3.0 and replaced by Java Persistence API (JPA) entities.
- **Message-driven beans**: These are stateless objects that act as message consumers and process messages asynchronously. They implement the javax.jms.MessageListener interface and receive messages from a Java Message Service (JMS) provider.

Here is an example of a stateless session bean that performs a simple calculation:

```java
// CalculatorBean.java
import javax.ejb.Stateless;

@Stateless
public class CalculatorBean implements CalculatorRemote {

  @Override
  public int add(int a, int b) {
    return a + b;
  }

  @Override
  public int subtract(int a, int b) {
    return a - b;
  }
}
```

```java
// CalculatorRemote.java
import javax.ejb.Remote;

@Remote
public interface CalculatorRemote {
  int add(int a, int b);
  int subtract(int a, int b);
}
```