An entity bean is a type of Enterprise JavaBean (EJB), a server-side Java EE component, that represents persistent data maintained in a database. An entity bean can manage its own persistence (bean managed persistence) or can delegate this function to its EJB container (container managed persistence). An entity bean is identified by a primary key.

#### Entity bean in Enterprise Java Bean

The following diagram shows the basic architecture of an entity bean in Enterprise Java Bean:

```
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  EJB Container  |        |  Entity Bean    |        |  Database       |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  EJB Object     |<------>|  Bean Instance  |<------>|  Data Record    |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  Home Object    |<------>|  Bean Class     |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
|                 |        |                 |        |                 |
|  EJB Context    |------->|  Bean Context   |        |                 |
|                 |        |                 |        |                 |
+-----------------+        +-----------------+        +-----------------+
```

The EJB container provides the runtime environment for the entity bean and manages its lifecycle, security, transactions, concurrency, and persistence. The EJB container also provides the EJB object, the home object, and the EJB context for the entity bean.

The EJB object is the proxy for the entity bean that implements the business interface and handles the client requests. The EJB object delegates the requests to the bean instance, which is the actual object that represents the entity bean's state and behavior.

The home object is the factory for the entity bean that implements the home interface and provides methods for creating, finding, and removing entity beans. The home object interacts with the bean class, which is the class that defines the entity bean's properties, methods, and annotations.

The EJB context is the interface that allows the entity bean to access the container services, such as security, transactions, and naming. The EJB context is passed to the bean context, which is the interface that allows the entity bean to access the bean instance, the primary key, and the bean managed persistence.

The database is the external data source that stores the persistent data for the entity bean. The database contains the data record, which is the row that corresponds to the entity bean's primary key and attributes. The database can be accessed by the entity bean either directly (bean managed persistence) or indirectly (container managed persistence).