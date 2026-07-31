### Entity bean

An entity bean is a type of Enterprise JavaBean (EJB), a server-side component that runs on a Java EE application server. An entity bean represents persistent data stored in a relational database. An entity bean can have the following characteristics :

- It is a remote object that can be accessed by other components or clients using the Java Remote Method Invocation (RMI) protocol.
- It has a primary key that uniquely identifies it among other instances of the same entity bean type.
- It can manage its own persistence (bean-managed persistence or BMP) or delegate this function to its container (container-managed persistence or CMP).
- It can perform complex business logic that involves multiple dependent Java objects or other entity beans.
- It can participate in transactions that ensure the consistency and integrity of the data.

Some of the benefits of using entity beans are :

- They encapsulate the data access logic and hide the details of the underlying database from the clients or other components.
- They provide a high-level, object-oriented view of the data that is independent of the database schema or vendor.
- They can be reused across different applications or modules that need to access the same data.
- They can take advantage of the services provided by the EJB container, such as security, concurrency, caching, pooling, and lifecycle management.

Some of the drawbacks of using entity beans are :

- They can introduce performance overhead due to the network and database access involved in each method invocation.
- They can be complex to develop and maintain, especially for BMP entity beans that require writing SQL statements and mapping the data to Java objects.
- They can be difficult to test and debug, as they depend on the EJB container and the database environment.
- They can be less flexible and scalable than other data access technologies, such as Java Data Objects (JDO) or Hibernate.

: Entity Beans - Oracle. https://docs.oracle.com/cd/A97335_02/apps.102/a83725/entity1.htm
: Entity Bean - Wikipedia. https://en.wikipedia.org/wiki/Entity_Bean