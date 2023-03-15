### Entity bean

- An entity bean is a type of Enterprise JavaBean, a server-side Java EE component, that represents persistent data maintained in a database.
- An entity bean can manage its own persistence (Bean managed persistence) or can delegate this function to its EJB Container (Container managed persistence).
- An entity bean is identified by a primary key, which is a unique identifier for each instance of the bean .
- Entity beans are normally coarse-grained persistent objects, in that they utilize persistent data stored within several fine-grained persistent Java objects.
- Entity beans can perform complex business logic, potentially using several dependent Java objects.
- Entity beans can be accessed by multiple clients concurrently, and the EJB Container is responsible for managing concurrency, transactions, security, and lifecycle of the beans.
- Entity beans can be either container-managed or bean-managed, depending on how the persistence is implemented.
- Container-managed entity beans (CMBE) rely on the EJB Container to handle the database access, mapping, caching, and synchronization of the bean data.
- Bean-managed entity beans (BMPE) implement the persistence logic in the bean code, using JDBC or other APIs to access the database directly.
- Entity beans can also be classified as either CMP 1.x or CMP 2.x, depending on the version of the EJB specification they follow.
- CMP 1.x entity beans use a deployment descriptor to define the bean properties, primary key, and database mapping.
- CMP 2.x entity beans use an abstract persistence schema to define the bean properties, primary key, and database mapping, and also support relationships, inheritance, and queries.
- Entity beans are deprecated since EJB 3.0, and are replaced by Java Persistence API (JPA) entities, which are simpler, more flexible, and more portable.