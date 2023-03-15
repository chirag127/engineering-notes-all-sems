#### Stateful Session bean in Enterprise Java Bean

- A stateful session bean is a type of enterprise bean, which preserves the conversational state with the client .
- A stateful session bean as per its name keeps associated client state in its instance variables.
- EJB Container creates a separate stateful session bean to process each client's request.
- A stateful session bean is intended for use by a single client during its lifetime and maintains a conversational state across multiple method calls and transactions.
- A stateful session bean can be accessed by only one client at a time, and the container can passivate and activate a stateful session bean to manage the system resources.
- A stateful session bean can implement a local or remote business interface, or both.
- A stateful session bean can also implement a no-interface view, which allows the client to access the bean through its bean class.
- A stateful session bean can use dependency injection to access other enterprise beans, resources, and services.
- A stateful session bean can use annotations or XML descriptors to specify its configuration, such as its name, transaction attributes, security roles, etc.
- A stateful session bean can use callback methods or listeners to perform lifecycle operations, such as initializing, destroying, passivating, and activating the bean.
- A stateful session bean can use the @Remove annotation to mark a method that removes the bean from the container after the method completes.
- A stateful session bean can use the @PrePassivate and @PostActivate annotations to mark methods that perform operations before and after the bean is passivated or activated by the container.
- A stateful session bean can use the @Stateful annotation to mark the bean class as a stateful session bean .

An example of a stateful session bean class is:

```java
@Stateful
public class ShoppingCartBean implements ShoppingCart {
  private List<String> items;

  @PostConstruct
  public void init() {
    items = new ArrayList<>();
  }

  @Override
  public void addItem(String item) {
    items.add(item);
  }

  @Override
  public List<String> getItems() {
    return items;
  }

  @Override
  @Remove
  public void checkout() {
    // process the order
  }

  @PrePassivate
  public void passivate() {
    // perform operations before passivation
  }

  @PostActivate
  public void activate() {
    // perform operations after activation
  }
}
```

Some advantages of stateful session beans are:

- They can maintain a conversational state with the client, which can improve the user experience and reduce the network traffic.
- They can use the extended persistence context, which allows the bean to manage the entities across multiple transactions without detaching and merging them.

Some disadvantages of stateful session beans are:

- They consume more memory and resources than stateless session beans, as they need to store the client state and be passivated and activated by the container.
- They are not scalable, as they can only serve one client at a time and cannot be shared or pooled by multiple clients.
- They are not fault-tolerant, as they can lose the client state if the server crashes or the bean is removed by the container.

Some applications of stateful session beans are:

- Shopping carts, which need to keep track of the items added by the client .
- Wizards, which need to guide the client through a series of steps and store the intermediate data.
- Games, which need to maintain the state of the players and the game logic.