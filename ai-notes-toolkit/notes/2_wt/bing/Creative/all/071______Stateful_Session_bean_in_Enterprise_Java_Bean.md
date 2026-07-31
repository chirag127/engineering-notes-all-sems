#### Stateful Session bean in Enterprise Java Bean

- A stateful session bean is a type of enterprise bean, which preserves the conversational state with the client  .
- A stateful session bean as per its name keeps associated client state in its instance variables  . EJB Container creates a separate stateful session bean to process each client's request  .
- A stateful session bean is intended for use by a single client during its lifetime and maintains a conversational state across multiple method calls  .
- A stateful session bean can be accessed by only one client at a time, and the client can invoke methods on the bean only in a sequential manner.
- A stateful session bean can implement a local view, a remote view, or both  .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor  .
- A stateful session bean can have the following lifecycle methods: `@PostConstruct`, `@PreDestroy`, `@PrePassivate`, and `@PostActivate`  .
- A stateful session bean can be passivated by the container to free up memory resources, and reactivated when needed  .
- A stateful session bean can be removed by the client using the `@Remove` annotation or by the container when it reaches a timeout  .

##### Example of a stateful session bean

```java
// Local interface
@Local
public interface ShoppingCart {
    public void addItem(String item);
    public void removeItem(String item);
    public List<String> getItems();
    public void checkout();
}

// Stateful bean implementation
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
    public void removeItem(String item) {
        items.remove(item);
    }

    @Override
    public List<String> getItems() {
        return items;
    }

    @Override
    @Remove
    public void checkout() {
        // Process the payment and clear the items
    }

    @PrePassivate
    public void passivate() {
        // Perform any cleanup before passivation
    }

    @PostActivate
    public void activate() {
        // Perform any initialization after activation
    }

    @PreDestroy
    public void destroy() {
        // Perform any cleanup before destruction
    }
}
```

##### Advantages of stateful session beans

- They can maintain the conversational state with the client and provide a natural way of modeling complex business logic .
- They can reduce the network traffic and improve the performance by caching the client data in the bean instance .
- They can leverage the container services such as security, transaction management, dependency injection, etc .

##### Disadvantages of stateful session beans

- They consume more memory and processing resources than stateless session beans, as they need to store the client state and handle the passivation and activation .
- They are not scalable for a large number of clients, as they can create a bottleneck in the system .
- They are more complex to develop and test, as they need to handle the concurrency, passivation, activation, and removal issues .

##### Applications of stateful session beans

- They can be used for implementing shopping carts, reservation systems, online games, workflows, etc .
- They can be used for scenarios where the client needs to interact with the bean multiple times and the bean needs to remember the client state .

##### Mnemonics and learning tricks for stateful session beans

- A stateful session bean is like a personal assistant who remembers your preferences and needs, and helps you with your tasks[^2