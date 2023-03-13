A stateful session bean is a type of enterprise bean that preserves the conversational state with the client. It keeps the associated client state in its instance variables and can be accessed by only one client at a time. The EJB container creates and manages the lifecycle of stateful session beans and provides services such as dependency injection, security, concurrency, and transaction management.

The following ASCII diagram illustrates the basic architecture of a stateful session bean in Enterprise Java Bean:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|    Client       |     |    EJB Home     |     |    EJB Object   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|  |           |  |     |  |           |  |     |  |           |  |
|  |  lookup() |  |---->|  |  create() |  |---->|  |  business |  |
|  |           |  |     |  |           |  |     |  |  methods  |  |
|  +-----------+  |     |  +-----------+  |     |  +-----------+  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             |     |                    |     |
                             v     v                    v     v
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |    EJB Class    |     |    Bean Pool    |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
                        |                 |     |                 |
                        |  +-----------+  |     |  +-----------+  |
                        |  |           |  |     |  |           |  |
                        |  |  ejbCreate|  |<----|  |  passivate|  |
                        |  |           |  |     |  |           |  |
                        |  +-----------+  |     |  +-----------+  |
                        |                 |     |                 |
                        |  +-----------+  |     |  +-----------+  |
                        |  |           |  |     |  |           |  |
                        |  |  ejbRemove|  |---->|  |  activate |  |
                        |  |           |  |     |  |           |  |
                        |  +-----------+  |     |  +-----------+  |
                        |                 |     |                 |
                        +-----------------+     +-----------------+
```