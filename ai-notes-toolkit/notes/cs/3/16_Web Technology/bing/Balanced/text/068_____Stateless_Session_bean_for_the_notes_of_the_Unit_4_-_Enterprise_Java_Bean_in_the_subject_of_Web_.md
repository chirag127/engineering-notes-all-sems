### Stateless Session Bean

- A stateless session bean is a type of enterprise bean that provides business logic without maintaining any conversational state with the client  .
- A stateless session bean is strictly a single invocation bean, meaning that it does not store any information about the previous or subsequent method calls.
- A stateless session bean can be used for reusable business services that are not connected to any specific client, such as generic currency calculations, mortgage rate calculations, and so on.
- A stateless session bean may contain instance variables that are specific to a client for the duration of a method invocation, but these variables are not shared or preserved across different method invocations .
- A stateless session bean and its client do not share state or identity, and the client cannot rely on the bean instance to remain the same between method calls .
- A stateless session bean is a singleton bean, meaning that there is only one instance of the bean class per application context.
- A stateless session bean is pooled by the EJB container to service the requests on demand, and the container can create, destroy, or reuse the bean instances as needed .
- A stateless session bean can be annotated with `@Stateless` or declared in the deployment descriptor with `<session-type>Stateless</session-type>` .
- A stateless session bean can implement a local, remote, or web service interface, or a combination of these .
- A stateless session bean can access other enterprise beans, use the Java Persistence API, use the Java Transaction API, and use the Java Message Service API.