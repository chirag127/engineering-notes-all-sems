# Stateful Session Bean

- A stateful session bean is a type of enterprise bean that represents business logic and maintains conversational state with a client  .
- The conversational state is the data that is stored in the instance variables of the bean and reflects the interaction history between the bean and the client .
- A stateful session bean is mapped to a single client for the life of that client, and the container creates a separate stateful session bean for each client request .
- A stateful session bean can be annotated with `@Stateful` or declared in the deployment descriptor with `<session-type>Stateful</session-type>` .
- A stateful session bean can implement the `javax.ejb.SessionBean` interface or the `javax.ejb.SessionSynchronization` interface, or use annotations or deployment descriptor elements to specify lifecycle callback methods .
- A stateful session bean can use dependency injection or JNDI lookup to access other enterprise beans, resources, or services .
- A stateful session bean can be accessed by local, remote, or web service clients, and can use the `@Local`, `@Remote`, or `@WebService` annotations or the deployment descriptor to specify the client views .
- A stateful session bean can participate in transactions, and can use the `@TransactionAttribute`, `@TransactionManagement`, or `@Resource` annotations or the deployment descriptor to specify the transaction attributes and the transaction manager .
- A stateful session bean can be passivated by the container to free up memory, and can be activated when the client invokes a business method .
- A stateful session bean can be removed by the client or by the container, and can use the `@Remove` annotation or the deployment descriptor to specify the methods that trigger the bean removal .