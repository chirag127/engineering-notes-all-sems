#### Stateful Session bean in Enterprise Java Bean

- A stateful session bean is a type of enterprise bean, which preserves the conversational state with the client .
- A stateful session bean keeps the associated client state in its instance variables .
- EJB Container creates a separate stateful session bean to process each client's request .
- A stateful session bean is intended for use by a single client during its lifetime and maintains a conversational relationship with the client .
- A stateful session bean can be accessed by the client through a local or a remote interface .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor .
- A stateful session bean can implement the `javax.ejb.SessionSynchronization` interface to receive notifications of transaction boundaries .
- A stateful session bean can be removed by the client using the `@Remove` annotation or by the container using the `@Timeout` annotation or the `@RemoveTimeout` element .
- A stateful session bean can be passivated by the container to free up memory and reactivated when needed .
- A stateful session bean can use the `@PostActivate` and `@PrePassivate` callbacks to perform operations before and after passivation .

##### Example of a stateful session bean

```java
// Local interface
@Local
public interface ShoppingCart {
    public void addItem(String item);
    public void removeItem(String item);
    public List<String> getItems();
    public void checkout();
    public void cancel();
}

// Stateful session bean
@Stateful
public class ShoppingCartBean implements ShoppingCart {

    private List<String> items;

    @PostConstruct
    public void init() {
        items = new ArrayList<String>();
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
        // Process the payment and confirm the order
    }

    @Override
    @Remove
    public void cancel() {
        // Cancel the order and release the resources
    }
}
```

##### Mnemonics and learning tricks for stateful session bean

- A stateful session bean is like a shopping cart that remembers what the client has added or removed.
- A stateful session bean can be removed by the client or the container using the `R` letter: `@Remove`, `@RemoveTimeout`, or `@Timeout`.
- A stateful session bean can be passivated by the container using the `P` letter: `@PrePassivate` and `@PostActivate`.