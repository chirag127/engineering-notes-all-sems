### Stateful Session Bean

A stateful session bean is a type of enterprise bean that maintains conversational state with the client. This means that the bean retains the state of the interaction between the bean and the client across multiple method calls.

Here are some key points to remember about stateful session beans:

1. Stateful session beans are designed to support a single client and are not shared across multiple clients.
2. The state of a stateful session bean is retained across multiple method calls, but is not retained across server restarts or crashes.
3. Stateful session beans can be passivated, which means that their state is saved to secondary storage, and activated, which means that their state is restored from secondary storage.
4. Stateful session beans have a lifecycle that includes the following stages: `Does not exist`, `Method-ready pool`, `Ready`, `Passive`, and `Does not exist`.
5. Stateful session beans can be used to implement shopping carts, wizards, and other conversational interactions with the client.
