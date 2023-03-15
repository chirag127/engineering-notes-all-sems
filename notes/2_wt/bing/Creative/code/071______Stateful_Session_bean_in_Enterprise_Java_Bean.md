#### Stateful Session bean in Enterprise Java Bean

A stateful session bean is a type of enterprise bean that maintains a conversational state with a client. It can remember the data and actions of a client across multiple requests. A stateful session bean is marked with the `@Stateful` annotation. For example:

```java
@Stateful
public class StatefulEJB {
  public String name;
}
```

A stateful session bean can have a business interface that defines the methods that the client can invoke. The business interface can be a local or a remote interface, depending on the location of the client. For example:

```java
package examples;

/** 
 * Business interface for the Account stateful session EJB. 
 */
public interface Account {
  public void deposit (int amount);
  public void withdraw (int amount);
  public void sayHelloFromAccountBean ();
}
```

A stateful session bean can implement the business interface and provide the logic for the methods. The bean class can also have lifecycle callback methods that are invoked by the container when the bean is created, activated, passivated, or removed. For example:

```java
package examples;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;
import javax.ejb.PostActivate;
import javax.ejb.PrePassivate;
import javax.ejb.Remove;
import javax.ejb.Stateful;

/**
 * Stateful session bean that implements the Account interface.
 */
@Stateful
public class AccountBean implements Account {

  private int balance;

  @PostConstruct
  public void init() {
    System.out.println("AccountBean created.");
  }

  @PostActivate
  public void activate() {
    System.out.println("AccountBean activated.");
  }

  @PrePassivate
  public void passivate() {
    System.out.println("AccountBean passivated.");
  }

  @PreDestroy
  public void destroy() {
    System.out.println("AccountBean destroyed.");
  }

  @Remove
  public void remove() {
    System.out.println("AccountBean removed.");
  }

  public void deposit(int amount) {
    balance += amount;
    System.out.println("Deposited " + amount + ". Balance: " + balance);
  }

  public void withdraw(int amount) {
    balance -= amount;
    System.out.println("Withdrawn " + amount + ". Balance: " + balance);
  }

  public void sayHelloFromAccountBean() {
    System.out.println("Hello from AccountBean!");
  }
}
```

A client can access a stateful session bean by injecting it using the `@EJB` annotation. The client can then invoke the methods of the bean and the bean will remember the state of the client. For example:

```java
public class EJBClient1 {
  @EJB
  public StatefulEJB statefulEJB;

  public void doSomething() {
    statefulEJB.name = "Alice";
    System.out.println("Name set to " + statefulEJB.name);
  }
}

public class EJBClient2 {
  @EJB
  public StatefulEJB statefulEJB;

  public void doSomething() {
    statefulEJB.name = "Bob";
    System.out.println("Name set to " + statefulEJB.name);
  }
}
```

In this example, each client will have a different instance of the stateful session bean and the bean will remember the name of each client. The output of the clients will be:

```
Name set to Alice
Name set to Bob
```