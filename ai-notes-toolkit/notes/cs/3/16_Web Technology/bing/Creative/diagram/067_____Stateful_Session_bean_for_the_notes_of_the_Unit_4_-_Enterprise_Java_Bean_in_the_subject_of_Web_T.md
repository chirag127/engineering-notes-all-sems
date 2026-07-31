### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client  .
- The conversational state is the data that is stored in the instance variables of the bean and reflects the interaction history between the bean and the client .
- A stateful session bean is mapped to a single client for the life of that client and is removed when the client terminates or times out .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor with `<session-type>Stateful</session-type>` .
- A stateful session bean can implement the `javax.ejb.SessionSynchronization` interface or use the `@PostConstruct`, `@PreDestroy`, `@PrePassivate`, and `@PostActivate` annotations to manage its lifecycle callbacks .
- A stateful session bean can use the `@Remove` annotation or the `<remove-method>` element to mark a business method as a remove method, which will cause the bean to be removed after the method invocation .
- A stateful session bean can use the `@Passivate` and `@Activate` annotations or the `<passivation-capable>` element to enable or disable passivation, which is the process of temporarily transferring the bean state to a secondary storage .
- A stateful session bean can use the `@StatefulTimeout` annotation or the `<stateful-timeout>` element to specify the amount of time that the bean can be idle before it is eligible for removal by the container .
- A stateful session bean can use the `@DependsOn` annotation or the `<depends-on>` element to declare dependencies on other singleton or stateful session beans, which will affect the order of creation and destruction of the beans .