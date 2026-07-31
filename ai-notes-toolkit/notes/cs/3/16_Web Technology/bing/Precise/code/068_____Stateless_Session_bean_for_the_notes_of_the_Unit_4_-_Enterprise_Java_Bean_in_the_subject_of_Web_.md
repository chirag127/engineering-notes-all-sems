### Stateless Session Bean

- A Stateless Session Bean is a type of Enterprise Java Bean (EJB) that does not maintain conversational state with the client.
- Each invocation of a Stateless Session Bean is independent of any previous invocation.
- Stateless Session Beans are typically used to perform independent operations, such as calculations or database access.
- They can be pooled by the container to improve performance, as they do not need to maintain state between invocations.
- Stateless Session Beans can be accessed by multiple clients concurrently.
- They are defined by implementing the `javax.ejb.Stateless` annotation or by specifying the bean type in the deployment descriptor.
- The lifecycle of a Stateless Session Bean includes the following stages: creation, injection of resources, invocation of business methods, and removal.
- The container is responsible for managing the lifecycle of Stateless Session Beans, including pooling and passivation.
- Stateless Session Beans can be accessed through either local or remote interfaces.
- They can also be exposed as web services by using the `@WebService` annotation.
