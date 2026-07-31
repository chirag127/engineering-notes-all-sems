#### Entity bean in Enterprise Java Bean

- An entity bean is a type of Enterprise JavaBean (EJB), which is a server-side Java EE component that encapsulates the business logic of an application.
- An entity bean represents persistent data maintained in a database. It can map to a table, a row, or a column in the database, depending on the granularity of the entity bean.
- An entity bean can manage its own persistence (Bean managed persistence, BMP) or can delegate this function to its EJB Container (Container managed persistence, CMP).
- An entity bean is identified by a primary key, which is a unique identifier for the entity bean instance. The primary key can be a single field or a composite of multiple fields.
- An entity bean can have local or remote interfaces, which define the methods that can be invoked by the clients of the entity bean. A local interface is used when the client and the entity bean are in the same JVM, while a remote interface is used when they are in different JVMs.
- An entity bean can also have a home interface, which defines the methods for creating, finding, and removing entity bean instances. A home interface can be local or remote as well.
- An entity bean can be either a session bean or a message-driven bean. A session bean is a stateful component that maintains a conversational state with a client. A message-driven bean is a stateless component that acts as a listener for messages from a message queue or a topic.
- An entity bean can implement business methods, which contain the business logic of the entity bean. Business methods can be invoked by the clients of the entity bean or by other EJBs.
- An entity bean can also implement callback methods, which are invoked by the EJB Container at certain lifecycle events, such as creation, activation, passivation, and removal of the entity bean instance.
- An entity bean can use the EJBContext interface to access the runtime context of the entity bean, such as the security information, the transaction status, and the user principal.
- An entity bean can use the JNDI (Java Naming and Directory Interface) to look up other EJBs or resources, such as data sources, connection factories, and mail sessions.
- An entity bean can use the JPA (Java Persistence API) to perform object-relational mapping and persistence operations on the entity bean. JPA provides an EntityManager interface, which can be used to create, read, update, and delete entity bean instances. JPA also provides annotations and XML descriptors to define the mapping between the entity bean and the database.
- An entity bean can use the EJB QL (Enterprise JavaBeans Query Language) to query the database using a SQL-like syntax. EJB QL can be used to define finder methods in the home interface of the entity bean, or to execute dynamic queries using the EntityManager interface.

Some possible mnemonics and learning tricks for the entity bean are:

- EJB = Entity Java Bean
- BMP = Bean Manages Persistence
- CMP = Container Manages Persistence
- PK = Primary Key
- LI = Local Interface
- RI = Remote Interface
- HI = Home Interface
- SB = Session Bean
- MDB = Message-Driven Bean
- BM = Business Method
- CM = Callback Method
- EC = EJBContext
- JNDI = Java Naming and Directory Interface
- JPA = Java Persistence API
- EM = EntityManager
- EJB QL = Enterprise JavaBeans Query Language

A possible ascii diagram for the entity bean is:

```
+-----------------+       +-----------------+
|    Database     |       |    EJB Client   |
+-----------------+       +-----------------+
|                 |       |                 |
|  +-----------+  |       |  +-----------+  |
|  |   Table   |  |       |  |   Proxy   |  |
|  +-----------+  |       |  +-----------+  |
|  |   Row     |  |       |  |   Stub    |  |
|  +-----------+  |       |  +-----------+  |
|  |   Column  |  |       |  |   Home    |  |
|  +-----------+  |       |  +-----------+  |
|                 |       |                 |
+-----------------+       +-----------------+
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |                       |
          |

```
