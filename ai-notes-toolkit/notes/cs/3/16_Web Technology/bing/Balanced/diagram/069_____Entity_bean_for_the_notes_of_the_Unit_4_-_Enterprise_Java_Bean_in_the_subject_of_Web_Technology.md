### Entity bean

- An entity bean is a type of Enterprise JavaBean (EJB), a server-side component that runs on a Java EE application server.
- An entity bean represents persistent data stored in a database, such as a customer, an order, or a product.
- An entity bean can have a remote or a local interface, depending on whether it is accessed by a client in the same or a different JVM.
- An entity bean can manage its own persistence (bean-managed persistence or BMP) or delegate this function to its container (container-managed persistence or CMP).
- An entity bean has a primary key that uniquely identifies it among other instances of the same type.
- An entity bean can have relationships with other entity beans, such as one-to-one, one-to-many, or many-to-many.
- An entity bean can implement business logic that operates on its persistent data, such as validation, calculation, or transformation.
- An entity bean can participate in transactions, security, and concurrency control managed by the container.
- An entity bean can use other Java EE services, such as naming, messaging, or web services.