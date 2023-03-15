# Stateless Session Bean

- A stateless session bean is a type of enterprise bean that provides business logic without maintaining any conversational state with the client  .
- A stateless session bean is strictly a single invocation bean, meaning that each method invocation is independent and unrelated to any previous or subsequent invocation.
- A stateless session bean can be used for reusable business services that are not connected to any specific client, such as generic currency calculations, mortgage rate calculations, and so on.
- A stateless session bean may contain instance variables that store client-independent, read-only state across a method call, but not across multiple calls .
- A stateless session bean does not have any lifecycle callback methods, such as @PostConstruct or @PreDestroy, because it does not need to perform any initialization or cleanup tasks.
- A stateless session bean is typically annotated with @Stateless or declared in the deployment descriptor with <session-type>Stateless</session-type> element .
- A stateless session bean can implement any number of business interfaces or use a no-interface view, which exposes all the public methods of the bean class as business methods .
- A stateless session bean can be accessed by local, remote, or web service clients.
- A stateless session bean can inject or access other enterprise beans, such as entity beans, message-driven beans, or other session beans .
- A stateless session bean can also access or update persistent data using the Java Persistence API or JDBC .
- A stateless session bean can be involved in transactions, either by using container-managed transactions or bean-managed transactions .
- A stateless session bean can use security annotations or declarative security to restrict access to its methods or data .
- A stateless session bean can use interceptors to add cross-cutting functionality, such as logging, auditing, or caching, to its methods .
- A stateless session bean can use dependency injection to obtain references to resources, such as data sources, JMS destinations, EJB references, or environment entries .
- A stateless session bean can use annotations or deployment descriptors to configure its properties, such as name, description, pool size, concurrency, or timeout .
- A stateless session bean is pooled by the EJB container to service the requests on demand. The container can create, destroy, or reuse stateless bean instances as needed .
- A stateless session bean is a singleton bean, meaning that there is only one instance of the bean class per application context. The same bean instance will be returned or injected during the lifetime of the application context.
- A stateless session bean is thread-safe, meaning that it can handle concurrent requests from multiple clients without any synchronization issues .