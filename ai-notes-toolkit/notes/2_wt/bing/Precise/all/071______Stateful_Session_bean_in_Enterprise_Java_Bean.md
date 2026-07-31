#### Stateful Session bean in Enterprise Java Bean

- Stateful session beans are used to represent the state of a unique client/bean session.
- They maintain the conversational state with the client.
- When the client removes the bean, its state is lost.
- Stateful session beans are not shared among multiple clients.
- They can be passivated by the container to preserve resources.
- They are typically used in shopping cart scenarios, where the user adds items to the cart and the state of the cart is maintained until the user checks out.
- Stateful session beans can be used to maintain the state of a workflow or a business process.
- They can be used to maintain the state of a user's interaction with an application over multiple requests.
- Stateful session beans can be used to maintain the state of a game or a multi-step process.
- They can be used to maintain the state of a user's interaction with a web application over multiple requests.

A mnemonic to remember the characteristics of stateful session beans is **"Stateful Shopping Carts Pass Multiple Steps"**. This stands for **Stateful, Shopping cart scenarios, Conversational state, Passivated, Multiple clients, Steps in a workflow**.

Here is an example of a stateful session bean that maintains the state of a shopping cart:

```java
@Stateful
public class ShoppingCartBean implements ShoppingCart {
    private List<String> items = new ArrayList<String>();

    public void addItem(String item) {
        items.add(item);
    }

    public void removeItem(String item) {
        items.remove(item);
    }

    public List<String> getItems() {
        return items;
    }
}
```

In this example, the `ShoppingCartBean` maintains the state of the items in the shopping cart. The `addItem` and `removeItem` methods are used to add and remove items from the cart, and the `getItems` method is used to retrieve the current state of the cart.