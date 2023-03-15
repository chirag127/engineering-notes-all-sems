#### Stateful Session bean in Enterprise Java Bean

- Stateful session beans are a type of enterprise bean in the Java EE platform.
- They are used to manage the state of a conversation between a client and the server.
- Stateful session beans maintain state across multiple method invocations and transactions.
- They are typically used in scenarios where the state of the conversation needs to be maintained, such as in a shopping cart application.
- Stateful session beans are created by the client and are bound to the client for the duration of the conversation.
- When the conversation is complete, the stateful session bean is removed by the container.
- Stateful session beans can be passivated by the container to free up resources, and activated again when needed.
- Stateful session beans can also participate in transactions and can be used to manage the state of a transaction.
- Stateful session beans can be accessed by multiple clients, but each client will have its own instance of the bean.
- Stateful session beans can be used in both local and remote scenarios.
