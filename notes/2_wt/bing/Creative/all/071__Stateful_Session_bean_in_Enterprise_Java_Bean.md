#### Stateful Session bean in Enterprise Java Bean

- A stateful session bean is a type of enterprise bean, which preserves the conversational state with the client.
- A stateful session bean keeps associated client state in its instance variables.
- EJB container creates a separate stateful session bean to process each client's request.
- A stateful session bean is intended for use by a single client during its lifetime.
- A stateful session bean can maintain a conversational state across multiple method calls.
- A stateful session bean can be annotated with `@Stateful` annotation.
- A stateful session bean can implement a local, remote, or no-interface view.
- A stateful session bean can use dependency injection to access other enterprise beans or resources.
- A stateful session bean can be passivated by the container to free up memory and reactivated when needed.
- A stateful session bean can be removed by the container when it is not used for a long time or by the client using the `@Remove` annotation.

##### Example of a stateful session bean

```java
// A stateful session bean that stores a shopping cart for a client
@Stateful
public class ShoppingCartBean implements ShoppingCart {

  // A list of items in the cart
  private List<String> items;

  // A constructor that initializes the list
  public ShoppingCartBean() {
    items = new ArrayList<String>();
  }

  // A method that adds an item to the cart
  public void addItem(String item) {
    items.add(item);
  }

  // A method that removes an item from the cart
  public void removeItem(String item) {
    items.remove(item);
  }

  // A method that returns the items in the cart
  public List<String> getItems() {
    return items;
  }

  // A method that clears the cart
  @Remove
  public void checkout() {
    items.clear();
  }
}
```

##### Advantages of stateful session beans

- They can provide a natural and intuitive way of modeling business processes that involve multiple interactions with the client.
- They can reduce the need for the client to maintain and pass the state information to the bean.
- They can improve the performance by caching the state in memory and avoiding database access.

##### Disadvantages of stateful session beans

- They consume more memory and resources than stateless session beans.
- They are not scalable for a large number of clients as each client needs a separate bean instance.
- They are not fault-tolerant as the state can be lost if the bean instance or the server fails.

##### Mnemonics and learning tricks for stateful session beans

- A stateful session bean is like a personal assistant who remembers your preferences and needs.
- A stateful session bean is like a shopping cart that keeps track of the items you want to buy.
- A stateful session bean is like a phone call that can be put on hold and resumed later.
- A stateful session bean can be PASSive (Passivated) or REActive (Reactivated) by the container.
- A stateful session bean can be REMoved by the client or the container.