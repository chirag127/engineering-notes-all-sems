### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that represents business logic and maintains state (data) between multiple method calls  .
- The state of an object consists of the values of its instance variables. In a stateful session bean, the instance variables represent the state of a unique client/bean session.
- Stateful session beans are useful for conversational sessions, in which it is necessary to maintain state, such as instance variable values or transactional state.
- Stateful session beans are mapped to a single client for the life of that client. EJB Container creates a separate stateful session bean to process client's each request.
- Stateful session beans can be annotated with `@Stateful` annotation . Alternatively, they can be declared in the deployment descriptor with `<session-type>Stateful</session-type>` element.
- Stateful session beans can implement the `javax.ejb.SessionBean` interface or extend the `javax.ejb.SessionSynchronization` interface to receive lifecycle and synchronization callbacks.
- Stateful session beans can use the `@PostConstruct`, `@PreDestroy`, `@PrePassivate`, and `@PostActivate` annotations to mark methods that perform initialization, cleanup, passivation, and activation tasks.
- Stateful session beans can use the `@Remove` annotation to mark methods that remove the bean instance from the container.
- Stateful session beans can use the `@SessionSynchronization` annotation to mark methods that are invoked before and after the bean instance is involved in a transaction.
- Stateful session beans can use the `@DependsOn` annotation to specify the names of other singleton beans that must be initialized before this bean.
- Stateful session beans can use the `@AccessTimeout` annotation to specify the amount of time that a concurrent access attempt should block before timing out.
- Stateful session beans can use the `@ConcurrencyManagement` annotation to specify whether the bean uses container-managed or bean-managed concurrency.
- Stateful session beans can use the `@Lock` annotation to specify the concurrency lock level for a method or a bean.
- Stateful session beans can use the `@StatefulTimeout` annotation to specify the amount of time that the bean can be idle (not receive any client invocations) before it is eligible for removal by the container.