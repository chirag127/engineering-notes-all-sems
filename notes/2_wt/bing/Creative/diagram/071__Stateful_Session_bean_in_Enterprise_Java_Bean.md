A stateful session bean is a type of enterprise bean that preserves the conversational state with the client. A stateful session bean keeps associated client state in its instance variables. The EJB container creates a separate stateful session bean to process each client's request .

The following diagram illustrates the basic architecture of a stateful session bean in Enterprise Java Bean using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|    Client       |       |    EJB Proxy    |       |    EJB Object   |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Business       |       |  Business       |       |  Business       |
|  Methods        |       |  Methods        |       |  Methods        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  State          |       |  State          |       |  State          |
|  Variables      |       |  Variables      |       |  Variables      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  EJB Reference  |       |  EJB Reference  |       |  EJB Reference  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  EJB Home       |       |  EJB Home       |       |  EJB Home       |
|  Reference      |       |  Reference      |       |  Reference      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  EJB Context    |       |  EJB Context    |       |  EJB Context    |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  EJB Container  |       |  EJB Container  |       |  EJB Container  |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The client is the application that invokes the business methods of the stateful session bean. The client can be a web component, another enterprise bean, or a Java application.

The EJB proxy is a local or remote interface that provides the client with a view of the stateful session bean. The client invokes the business methods through the EJB proxy.

The EJB object is the instance of the stateful session bean class that implements the business logic. The EJB object maintains the state of the client's conversation in its instance variables.

The EJB reference is a logical reference to the stateful session bean that is used by the EJB proxy to locate and invoke the EJB object.

The EJB home reference is a logical reference to the stateful session bean's home interface that is used by the client to create, remove, or find the EJB object.

The EJB context is an object that provides the stateful session bean with information about its container, security, transactions, and other services.

The EJB container is the runtime environment that manages the lifecycle, concurrency, security, transactions, and other services of the stateful session bean.