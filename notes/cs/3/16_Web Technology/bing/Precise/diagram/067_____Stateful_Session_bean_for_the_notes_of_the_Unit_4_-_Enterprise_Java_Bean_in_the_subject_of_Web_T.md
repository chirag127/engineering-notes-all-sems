### Stateful Session Bean

A stateful session bean is a type of enterprise bean that maintains conversational state with the client. This means that the bean retains information about the interactions with a specific client across multiple method calls and transactions.

Here are some key points to remember about stateful session beans:

1. Stateful session beans are associated with a specific client and maintain state across multiple method calls and transactions.
2. The state of a stateful session bean is retained for the duration of the client-bean interaction, which can span multiple method calls and transactions.
3. Stateful session beans can be passivated, which means that their state is saved to secondary storage and the bean instance is removed from memory. This can happen when the bean is not being used or when the container needs to free up memory.
4. When a client invokes a method on a stateful session bean, the container activates the bean by restoring its state from secondary storage and invoking the method.
5. Stateful session beans can be used to manage complex interactions between a client and the server, such as shopping carts or multi-step wizards.
6. Stateful session beans are not shared between clients. Each client has its own instance of the bean with its own state.
