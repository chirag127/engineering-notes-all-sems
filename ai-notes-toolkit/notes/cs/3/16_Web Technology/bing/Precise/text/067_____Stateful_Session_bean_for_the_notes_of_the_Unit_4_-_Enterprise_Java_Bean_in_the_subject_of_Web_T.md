### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that maintains conversational state with a client.
- It is created by a client and its instance variables represent the state of a unique client-bean session.
- The state is retained across multiple method invocations and transactions.
- When the client finishes executing, the bean is removed.
- Stateful session beans are used in scenarios where a session with a client needs to be maintained, such as in a shopping cart application.
- The bean's state represents the state of the interaction between the bean and a particular client.
- The state is specific to a client-bean pair and is not shared across different clients.
- Stateful session beans can be passivated by the container to preserve resources. When a bean is passivated, its state is saved and the bean instance is released. When the client invokes the bean again, a new instance is created and the state is restored.
- Stateful session beans can participate in transactions and can be accessed concurrently by multiple clients.
