### Stateful Session Bean

A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client. A stateful session bean as per its name keeps associated client state in its instance variables. Stateful session beans are useful for conversational sessions, in which it is necessary to maintain state, such as instance variable values or transactional state, between method invocations. These session beans are mapped to a single client for the life of that client.

Some points to note about stateful session beans are:

- Stateful session beans are annotated with `@Stateful` .
- Stateful session beans can implement one or more local or remote business interfaces, or use a no-interface view.
- Stateful session beans can have optional lifecycle callback methods annotated with `@PostConstruct`, `@PreDestroy`, `@PrePassivate`, and `@PostActivate`.
- Stateful session beans can use dependency injection to access other enterprise beans, web services, and resources.
- Stateful session beans can be involved in transactions, either container-managed or bean-managed.
- Stateful session beans can use the `@Remove` annotation to mark a method that removes the bean instance from the container after the method completes.
- Stateful session beans can use the `@StatefulTimeout` annotation to specify a timeout value for the bean's idle state.