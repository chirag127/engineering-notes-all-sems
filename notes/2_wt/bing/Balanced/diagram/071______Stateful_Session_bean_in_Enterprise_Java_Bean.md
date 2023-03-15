A stateful session bean is a type of enterprise bean that preserves the conversational state with the client. It keeps the associated client state in its instance variables. The EJB container creates a separate stateful session bean for each client request.

A stateful session bean can be represented by the following diagram:

#### Stateful Session bean in Enterprise Java Bean
```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Client        +-------->  EJB Container  +-------->  Stateful Bean  |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  - invokes      |        |  - creates      |        |  - maintains    |
|  - removes      |        |  - manages      |        |  - performs     |
|  - passes       |        |  - invokes      |        |  - accesses     |
|    parameters   |        |  - passes       |        |    resources    |
|                 |        |    parameters   |        |                 |
+-----------------+        +-----------------+        +-----------------+
```