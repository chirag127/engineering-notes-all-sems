# Stateless Session Bean

Stateless session beans are a type of enterprise bean in the Enterprise Java Bean (EJB) specification. They are used to encapsulate business logic and provide services to clients.

Here are some key points to remember about stateless session beans:

1. Stateless session beans do not maintain conversational state with clients. This means that each method invocation on a stateless session bean is independent of previous invocations.
2. Stateless session beans can be pooled by the container to improve performance. This means that multiple instances of a stateless session bean can be created and reused to serve multiple clients.
3. Stateless session beans can be accessed by multiple clients concurrently. This means that multiple clients can invoke methods on the same instance of a stateless session bean at the same time.
4. Stateless session beans are typically used for tasks that can be completed in a single method invocation, such as performing a calculation or retrieving data from a database.
5. Stateless session beans can be accessed through either local or remote interfaces. Local interfaces are used when the client and the bean are in the same application, while remote interfaces are used when the client and the bean are in different applications or on different machines.
