### Entity Bean

An entity bean represents a business object in a persistent storage mechanism. Some examples of business objects are customers, orders, and products. The main features of entity beans are as follows:

1. **Persistence**: Entity beans are persistent, meaning their data is stored in a database and can survive a server crash or shutdown.
2. **Primary Key**: Each entity bean has a unique primary key that identifies it.
3. **Relationships**: Entity beans can have relationships with other entity beans. For example, an order entity bean might have a relationship with a customer entity bean.
4. **Container-Managed Persistence (CMP)**: In CMP, the EJB container manages the persistence of the entity bean. The bean developer provides the container with mapping information that tells the container how to map the bean's fields to the database.
5. **Bean-Managed Persistence (BMP)**: In BMP, the bean developer is responsible for writing the code that manages the persistence of the bean.

Entity beans can be used to model business objects that need to be stored in a database. They provide an object-oriented view of the data and can encapsulate business logic. Entity beans can be accessed by other beans and by client applications. They can be used to implement the data access layer in a multi-tier architecture.