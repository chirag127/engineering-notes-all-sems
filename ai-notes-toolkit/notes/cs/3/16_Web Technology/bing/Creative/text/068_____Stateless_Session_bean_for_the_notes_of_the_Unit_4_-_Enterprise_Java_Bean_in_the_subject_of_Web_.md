### Stateless Session Bean

- A stateless session bean is a type of enterprise bean that provides business logic without maintaining any conversational state with the client  .
- A stateless session bean is strictly a single invocation bean, meaning that it does not store any information about the previous or subsequent method calls.
- A stateless session bean is commonly used for reusable and independent operations, such as calculations, validations, transactions, etc .
- A stateless session bean is a singleton bean, meaning that there is only one instance of the bean class per application context.
- A stateless session bean may have instance variables, but they are not specific to any client and may change between method invocations .
- A stateless session bean is pooled by the EJB container, meaning that the container can create, destroy, and reuse bean instances as needed to service the client requests .
- A stateless session bean can be annotated with `@Stateless` or declared in the deployment descriptor with `<session-type>Stateless</session-type>` .
- A stateless session bean can implement a local, remote, or web service interface, or a combination of them .
- A stateless session bean can access other enterprise beans, resources, and services through dependency injection or JNDI lookup .
- A stateless session bean can use container-managed or bean-managed transactions, security, concurrency, and interceptors .