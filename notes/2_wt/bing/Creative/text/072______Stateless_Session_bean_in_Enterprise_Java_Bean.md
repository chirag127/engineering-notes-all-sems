#### Stateless Session Bean in Enterprise Java Bean

- A stateless session bean is a type of enterprise bean, which is normally used to perform independent operations .
- A stateless session bean does not have any associated client state, but it may preserve its instance state .
- A stateless session bean does not maintain any conversational state between multiple method calls by the same or different clients .
- A stateless session bean can be pooled and reused by the container to serve multiple clients, thus improving performance and scalability .
- A stateless session bean is annotated with `@Stateless` or declared in the deployment descriptor with `<session-type>Stateless</session-type>`.
- A stateless session bean can implement a business interface or a no-interface view, or both.
- A stateless session bean can access other enterprise beans, web services, and resources such as databases and JMS destinations .
- A stateless session bean can use dependency injection to obtain references to other beans or resources.
- A stateless session bean can be a web service endpoint or a message-driven bean.
- A stateless session bean can use interceptors to add cross-cutting functionality such as logging, auditing, or security.