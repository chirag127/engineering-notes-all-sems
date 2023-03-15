### Stateful Session Bean

A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client. A stateful session bean as per its name keeps associated client state in its instance variables. EJB Container creates a separate stateful session bean to process client's each request.

Some of the characteristics of stateful session beans are:

- They are created by a client and bound to that client until the client removes them or they are timed out by the container.
- They can have multiple methods that can be invoked by the client in any order.
- They can access and update their instance variables across method invocations.
- They can implement the `javax.ejb.SessionSynchronization` interface to receive notifications of transaction boundaries and perform operations before and after transactions.
- They can use the `@PrePassivate` and `@PostActivate` annotations to perform operations before and after the bean is passivated (swapped out of memory) and activated (swapped back into memory) by the container.
- They can use the `@Remove` annotation to mark a method that will remove the bean from the container after invocation.
- They can use the `@Stateful` annotation to declare the bean as a stateful session bean.

An example of a stateful session bean is:

```java
import javax.ejb.Stateful;
import javax.ejb.Remove;

@Stateful
public class ShoppingCartBean implements ShoppingCart {

  private List<String> items;

  public ShoppingCartBean() {
    items = new ArrayList<String>();
  }

  public void addItem(String item) {
    items.add(item);
  }

  public void removeItem(String item) {
    items.remove(item);
  }

  public List<String> getItems() {
    return items;
  }

  @Remove
  public void checkout() {
    // process the order
  }
}
```