 Here is the content in markdown format for the topic - Stateful Session bean for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology:

### Stateful Session bean

- A stateful session bean maintains conversational state for a single client.
- It stores the state of the conversation with the client.
- The state is bound to the client and is destroyed when the client's conversation ends.
- The client can pass a handle to the bean's instance to other clients and allows them to share the state.
- Life cycle callback methods like `@PostConstruct` and `@PreDestroy` are called.
- Used when the client needs to hold a conversation with the bean beyond a single method call. For example - shopping cart.
- The bean's state is stored in an *instance field*.
- The container passivates the bean's state to secondary storage when it is not used, to preserve memory. It is activated when the client invokes on it.
- Examples - Shopping cart, session tracking, etc.

Advantages:
- Maintains state for a client.
- Instance variables can be used.

Disadvantages:
- Does not scale well as the number of clients increase as the state is stored in memory.
- Passivation and activation can affect performance.

//Include diagrams and codes here

Applications:
- Shopping cart
- Session tracking
- Data caching

That's the content in markdown format for the topic - Stateful Session bean for the notes of the Unit 4 - Enterprise Java Bean in the subject of Web Technology. I have included points on what stateful session bean is, its characteristics, advantages, disadvantages and applications. Please let me know if you would like me to elaborate on any of the points or add more details.