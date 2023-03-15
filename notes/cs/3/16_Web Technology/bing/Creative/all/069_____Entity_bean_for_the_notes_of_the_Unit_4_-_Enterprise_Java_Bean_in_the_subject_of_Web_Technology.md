# Entity bean

- An entity bean is a type of Enterprise JavaBean (EJB), a server-side Java EE component, that represents persistent data maintained in a database.
- An entity bean can manage its own persistence (bean-managed persistence) or can delegate this function to its EJB container (container-managed persistence).
- An entity bean is identified by a primary key, which is a unique identifier for each instance of the bean .
- Entity beans are normally coarse-grained persistent objects, in that they utilize persistent data stored within several fine-grained persistent Java objects.
- Entity beans can perform complex business logic and can use several dependent Java objects.
- Entity beans can be accessed by multiple clients concurrently and can participate in transactions.
- Entity beans can be either session beans or message-driven beans, depending on the type of client access and communication.
- Entity beans are deprecated since Java EE 5 and replaced by Java Persistence API (JPA) entities.