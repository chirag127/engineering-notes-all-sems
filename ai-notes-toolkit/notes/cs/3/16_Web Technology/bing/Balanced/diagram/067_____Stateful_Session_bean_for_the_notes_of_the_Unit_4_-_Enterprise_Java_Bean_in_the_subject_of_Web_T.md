### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client  .
- The conversational state is the data that is stored in the instance variables of the bean and reflects the interaction history between the bean and the client .
- A stateful session bean is mapped to a single client for the life of that client, and the container creates a separate bean instance for each client request .
- A stateful session bean can be annotated with `@Stateful` annotation or declared in the deployment descriptor with `<session-type>Stateful</session-type>` element .
- A stateful session bean can implement the `javax.ejb.SessionBean` interface or the `javax.ejb.SessionSynchronization` interface, or use the `@PostConstruct`, `@PreDestroy`, `@PrePassivate`, and `@PostActivate` annotations to define the bean's lifecycle methods  .
- A stateful session bean can use the `@Remove` annotation or the `<remove-method>` element to mark a business method that removes the bean instance after completion  .
- A stateful session bean can use the `@PassivationCapable` annotation or the `<passivation-capable>` element to indicate whether the bean can be passivated by the container to conserve resources .
- A stateful session bean can use the `@StatefulTimeout` annotation or the `<stateful-timeout>` element to specify the amount of time that the bean can be idle before it is removed by the container .
- A stateful session bean can use the `@DependsOn` annotation or the `<depends-on>` element to declare dependencies on other singleton or stateful session beans .
- A stateful session bean can use the `@AccessTimeout` annotation or the `<access-timeout>` element to specify the maximum time that a concurrent access attempt should block before throwing an exception .