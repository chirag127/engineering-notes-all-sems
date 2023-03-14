#### Stateless Session Bean in Enterprise Java Bean

- A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations.
- A stateless session bean does not have any associated client state, but it may preserve its instance state .
- A stateless session bean is not tied to one client and there is no guarantee for one client to get the same instance with each method invocation.
- A stateless session bean may have instance variables, but these fields are not specific to one client, so they should not be relied on between remote calls.
- A stateless session bean is typically pooled by the container and may be created or destroyed with each method invocation.
- A stateless session bean is annotated with `@Stateless` and may implement a local or remote interface .
- A stateless session bean can be injected into other components using the `@EJB` annotation .
- A stateless session bean can access other enterprise beans, web services, databases, security services, timers, and other resources .
- A stateless session bean can be used for tasks that do not require conversational state or transactions, such as calculations, logging, validation, etc .

: https://www.baeldung.com/ejb-session-beans
: https://stackoverflow.com/questions/2351220/stateless-and-stateful-enterprise-java-beans
: https://www.javatpoint.com/stateless-session-bean
: https://www.tutorialspoint.com/ejb/ejb_stateless_beans.htm