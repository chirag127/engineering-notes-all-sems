### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that maintains conversational state with a client.
- The state is retained across multiple method calls and transactions.
- The state is specific to a particular client and is not shared among multiple clients.
- When a client invokes the methods of a stateful bean, the bean's instance variables may contain a state specific to that client.
- When the client finishes executing, the bean's state is retained and can be used in future interactions with the same client.
- Stateful session beans are typically used in scenarios where there is a need to maintain state across multiple method calls or transactions, such as in a shopping cart application.
- Stateful session beans can be passivated, which means their state is saved to secondary storage and the bean instance is removed from memory to conserve resources.
- When the client needs to interact with the bean again, the bean is activated, its state is restored from secondary storage, and the bean instance is placed back into memory.
- Stateful session beans have a lifecycle that includes the following stages: `Does not exist`, `Method-Ready Pool`, `Passive`, and `Ready`.
- The `@Stateful` annotation is used to define a stateful session bean.