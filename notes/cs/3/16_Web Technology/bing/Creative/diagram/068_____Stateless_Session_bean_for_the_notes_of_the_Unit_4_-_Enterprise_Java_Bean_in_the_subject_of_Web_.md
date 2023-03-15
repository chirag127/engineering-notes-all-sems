### Stateless Session Bean

- A stateless session bean is a type of enterprise bean that provides business logic without maintaining any conversational state with the client  .
- A stateless session bean is strictly a single invocation bean. It is employed for reusable business services that are not connected to any specific client, such as generic currency calculations, mortgage rate calculations, and so on.
- A stateless session bean and its client do not share state or identity between method invocations. All instances of a particular stateless session bean class are identical.
- A stateless session bean may contain client-independent, read-only state across a call, such as a database connection or a reference to another enterprise bean.
- A stateless session bean does not have any associated lifecycle callbacks, such as @PostConstruct or @PreDestroy.
- A stateless session bean is annotated with @Stateless or defined in the deployment descriptor with <session-type>Stateless</session-type> .
- A stateless session bean can implement a local, remote, or web service interface .
- A stateless session bean can be injected into other components using the @EJB annotation or the <ejb-ref> or <ejb-local-ref> elements .
- A stateless session bean can access other enterprise beans, the Java Persistence API, the Java Transaction API, the Java Message Service API, and other Java EE services .
- A stateless session bean can be pooled by the EJB container to service the request on demand. The container can create, destroy, or reuse stateless session bean instances as needed .
- A stateless session bean is a stateless bean in the Spring context, meaning that it is a singleton and is initialized only once. The only state it has is a shared state.