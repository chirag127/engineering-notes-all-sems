#### Stateless Session bean in Enterprise Java Bean
Here is an ASCII diagram for a Stateless Session bean in Enterprise Java Bean:

```
  +---------------------+
  |   Client            |
  +----------+----------+
             |
             |
             v
  +----------+----------+
  |   EJB Container      |
  +----------+----------+
             |
             |
             v
  +----------+----------+
  |   Stateless Bean     |
  +---------------------+
```

A Stateless Session bean is an Enterprise Java Bean that does not maintain conversational state with the client. When a client invokes the methods of a Stateless Bean, the bean's instance variables may contain a state specific to that client but only for the duration of the invocation. When the method is finished, the client-specific state should not be retained. The EJB container typically creates and maintains a pool of Stateless Beans, and assigns them to clients as needed. When a client is finished with a bean instance, the instance is returned to the pool and is available to serve other clients.
