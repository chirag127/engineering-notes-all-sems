An entity bean is a type of enterprise Java bean that represents persistent data maintained in a database. An entity bean can manage its own persistence (bean managed persistence) or can delegate this function to its EJB container (container managed persistence). An entity bean is identified by a primary key.

The following diagram illustrates the basic architecture of an entity bean in enterprise Java bean using ASCII characters:

```
+-----------------+        +-----------------+        +-----------------+
|  EJB Container  |        |  Entity Bean    |        |  Database       |
|                 |        |                 |        |                 |
|  +-----------+  |        |  +-----------+  |        |  +-----------+  |
|  | Home     |  |        |  | Primary   |  |        |  | Table     |  |
|  | Interface|  |        |  | Key       |  |        |  |           |  |
|  +-----------+  |        |  +-----------+  |        |  +-----------+  |
|                 |        |                 |        |                 |
|  +-----------+  |        |  +-----------+  |        |  +-----------+  |
|  | Remote   |  |        |  | Attributes |  |        |  | Columns   |  |
|  | Interface|  |        |  | and        |  |        |  |           |  |
|  +-----------+  |        |  | Methods    |  |        |  +-----------+  |
|                 |        |  +-----------+  |        |                 |
+-----------------+        +-----------------+        +-----------------+
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       |                         |                         |
       +-------------------------+-------------------------+
```

The EJB container provides the services and infrastructure for the entity bean, such as transaction management, security, concurrency control, etc. The entity bean contains the primary key, which is a unique identifier for the bean instance, and the attributes and methods that define the business logic and data access of the bean. The database contains the table and columns that store the persistent data of the entity bean. The EJB container communicates with the database to perform the persistence operations, such as create, read, update, and delete, on the entity bean.