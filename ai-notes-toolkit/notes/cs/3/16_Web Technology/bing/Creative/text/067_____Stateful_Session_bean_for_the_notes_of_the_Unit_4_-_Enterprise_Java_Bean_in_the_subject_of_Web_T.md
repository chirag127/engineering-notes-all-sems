### Stateful Session Bean

- A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client  .
- The conversational state is the data that is stored in the instance variables of the bean and reflects the interaction history between the bean and the client .
- A stateful session bean is mapped to a single client for the life of that client and is removed by the container when the client terminates or the session times out .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor with `<session-type>Stateful</session-type>` .
- A stateful session bean can implement the `javax.ejb.SessionBean` interface or the `javax.ejb.SessionSynchronization` interface, or use annotations or deployment descriptor elements to specify lifecycle callback methods.
- A stateful session bean can use dependency injection or JNDI lookup to access other enterprise beans, resources, or services.
- A stateful session bean can be accessed by local, remote, or web service clients.
- A stateful session bean can participate in transactions, security, and concurrency management.