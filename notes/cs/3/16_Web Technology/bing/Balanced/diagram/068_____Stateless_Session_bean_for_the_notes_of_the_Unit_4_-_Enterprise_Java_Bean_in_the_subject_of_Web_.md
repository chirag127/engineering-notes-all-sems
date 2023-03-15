### Stateless Session Bean

- A stateless session bean is a type of enterprise bean that provides business logic without maintaining any conversational state with the client  .
- A stateless session bean is strictly a single invocation bean, meaning that it does not store any information about the previous or subsequent method calls.
- A stateless session bean is typically used for reusable and independent operations, such as calculations, validations, or database access .
- A stateless session bean can have instance variables, but they are not specific to any client and may change between method invocations .
- A stateless session bean is a singleton bean, meaning that there is only one instance of the bean class per application context.
- A stateless session bean is pooled by the EJB container, which means that the container can create, destroy, or reuse bean instances as needed to service the client requests .
- A stateless session bean can be annotated with `@Stateless` or declared in an XML deployment descriptor .
- A stateless session bean can implement a local, remote, or web service interface, or a combination of them .
- A stateless session bean can access other enterprise beans, use dependency injection, or use the EJB context object .
- A stateless session bean can use transactions, security, interceptors, or timers .