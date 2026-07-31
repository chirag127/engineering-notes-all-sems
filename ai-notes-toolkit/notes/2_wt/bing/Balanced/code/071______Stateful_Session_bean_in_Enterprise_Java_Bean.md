#### Stateful Session bean in Enterprise Java Bean

A stateful session bean is a type of enterprise bean that maintains a conversational state with a client. It can store the state of a business process across multiple method invocations and transactions. A stateful session bean is marked with the `@Stateful` annotation. The code for the stateful bean is as follows:

```java
@Stateful
public class StatefulEJB {
  public String name;
}
```

The stateful bean can have a business interface that defines the methods that the client can invoke. The business interface can be a local or remote interface, or a no-interface view. The following code shows a simple business interface for the `AccountBean` stateful session EJB:

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

The stateful bean can implement the business interface and provide the logic for the methods. The following code shows a simple implementation of the `AccountBean` stateful session EJB:

```java
package examples;

import javax.ejb.Stateful;

@Stateful
public class AccountBean implements Account {
  private int balance = 0;

  public void deposit (int amount) {
    balance += amount;
  }

  public void withdraw (int amount) {
    balance -= amount;
  }

  public void sayHelloFromAccountBean () {
    System.out.println("Hello from AccountBean");
  }
}
```

The stateful bean can be accessed by a client that injects a reference to the bean using the `@EJB` annotation. The client can invoke the methods on the bean and the bean will retain the state of the client across the invocations. The following code shows a simple local client for the `AccountBean` stateful session EJB:

```java
public class EJBClient {
  @EJB
  public Account account;

  public void testAccountBean () {
    account.deposit(100);
    account.withdraw(50);
    account.sayHelloFromAccountBean();
  }
}
```

The stateful bean can also be accessed by a remote client that uses the JNDI API to look up the bean using its global JNDI name. The remote client can invoke the methods on the bean and the bean will retain the state of the client across the invocations. The following code shows a simple remote client for the `AccountBean` stateful session EJB:

```java
import examples.Account;
import javax.naming.InitialContext;

public class EJBClient {
  public static void main(String[] args) throws Exception {
    InitialContext ic = new InitialContext();
    Account account = (Account) ic.lookup("java:global/examples/AccountBean!examples.Account");
    account.deposit(100);
    account.withdraw(50);
    account.sayHelloFromAccountBean();
  }
}
```