#### Entity bean in Enterprise Java Bean

- An entity bean is a type of enterprise bean that represents persistent data stored in a database.
- An entity bean can have a local or remote interface, or both, that defines the business methods for accessing and modifying the data.
- An entity bean can be either container-managed or bean-managed, depending on who is responsible for managing the persistence of the data.
- A container-managed entity bean delegates the persistence logic to the EJB container, which automatically synchronizes the bean's state with the database using a mapping file.
- A bean-managed entity bean implements the persistence logic in the bean class, using JDBC or JPA APIs to interact with the database.
- An entity bean can be either CMP (container-managed persistence) or BMP (bean-managed persistence), depending on the type of container-managed or bean-managed entity bean.
- A CMP entity bean is a container-managed entity bean that uses the EJB 2.x specification, which requires a home interface, a remote interface, a primary key class, and an abstract bean class with getter and setter methods for the persistent fields.
- A BMP entity bean is a bean-managed entity bean that uses the EJB 2.x specification, which requires a home interface, a remote interface, a primary key class, and a concrete bean class with the persistence logic in the ejbLoad, ejbStore, ejbFind, and ejbCreate methods.
- An entity bean can also be a JPA entity, which is a container-managed entity bean that uses the EJB 3.x specification, which simplifies the development by using annotations, eliminating the need for a home interface, a remote interface, a primary key class, and a mapping file.
- A JPA entity is a plain Java object that is annotated with @Entity and has a field or property annotated with @Id to indicate the primary key. The persistent fields or properties are mapped to the database columns by default or by using annotations such as @Column, @OneToOne, @OneToMany, etc.
- A JPA entity can have a local or remote interface, or both, that extends the javax.ejb.EJBObject or javax.ejb.EJBLocalObject interface, respectively, or can be accessed directly by the clients or other beans using the javax.persistence.EntityManager interface, which provides methods for persisting, finding, updating, and removing entities.
- A JPA entity can use inheritance, polymorphism, and relationships to model complex data structures, and can also use callbacks, listeners, and interceptors to handle lifecycle events and cross-cutting concerns.

Some possible mnemonics and learning tricks for entity beans are:

- Entity beans are persistent and map to database tables. Think of an entity as an entry in a table.
- Container-managed entity beans are easier to develop but less flexible. Think of the container as a manager who takes care of the details but also imposes some rules.
- Bean-managed entity beans are harder to develop but more flexible. Think of the bean as a self-managed worker who has more freedom but also more responsibility.
- CMP entity beans use EJB 2.x and have abstract classes and interfaces. Think of CMP as "Complex and More Parts".
- BMP entity beans use EJB 2.x and have concrete classes and interfaces. Think of BMP as "Basic but More Programming".
- JPA entities use EJB 3.x and have annotations and no interfaces. Think of JPA as "Java Persistence API" or "Just Plain Annotated".