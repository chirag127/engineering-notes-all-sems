#### Entity bean in Enterprise Java Bean

- An entity bean is a type of enterprise bean that represents persistent data stored in a database.
- An entity bean can have a local or remote interface that defines the business methods for accessing and modifying the data.
- An entity bean can be either container-managed or bean-managed, depending on who is responsible for managing the persistence logic.
- A container-managed entity bean delegates the persistence operations to the container, which uses a mapping file to map the bean properties to the database columns.
- A bean-managed entity bean implements the persistence logic in the bean class, using JDBC or JPA APIs to interact with the database.
- An entity bean can be either a CMP (container-managed persistence) entity bean or a BMP (bean-managed persistence) entity bean, depending on the type of persistence management.
- A CMP entity bean is simpler to develop and maintain, as the container handles the persistence logic and the bean only needs to provide the business methods and the mapping file.
- A BMP entity bean is more flexible and customizable, as the bean can implement any persistence strategy and use any database vendor, but it requires more coding and testing.
- An entity bean can have a primary key class that defines the unique identifier for the bean instance, which must be serializable and implement the equals and hashCode methods.
- An entity bean can have a home interface that defines the methods for creating, finding, and removing the bean instances, which can be local or remote depending on the client access.
- An entity bean can have a lifecycle that consists of four states: pooled, ready, passive, and does not exist, depending on the bean's activation and passivation by the container.