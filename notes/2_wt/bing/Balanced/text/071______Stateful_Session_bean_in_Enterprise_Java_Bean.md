#### Stateful Session Bean in Enterprise Java Bean

- A stateful session bean is a type of enterprise bean, which preserves the conversational state with the client .
- A stateful session bean keeps associated client state in its instance variables .
- EJB Container creates a separate stateful session bean to process each client's request .
- A stateful session bean is intended for use by a single client during its lifetime and maintains a conversational state across multiple method calls .
- A stateful session bean can be accessed by only one client at a time.
- A stateful session bean can implement business logic that depends on the state of the bean, such as a shopping cart or a wizard .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor .
- A stateful session bean can use the `@PostConstruct` and `@PreDestroy` callbacks to perform initialization and cleanup tasks .
- A stateful session bean can use the `@PrePassivate` and `@PostActivate` callbacks to manage its state when it is passivated or activated by the container .
- A stateful session bean can use the `@Remove` annotation to mark a method that will cause the bean to be removed after invocation .
- A stateful session bean can use the `@SessionSynchronization` interface to synchronize its state with the underlying transaction context .