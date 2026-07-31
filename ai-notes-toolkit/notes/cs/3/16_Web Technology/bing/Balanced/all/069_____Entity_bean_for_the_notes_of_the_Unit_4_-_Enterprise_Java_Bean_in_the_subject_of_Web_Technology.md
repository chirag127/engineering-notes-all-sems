# Entity bean

- An entity bean is a type of Enterprise JavaBean (EJB), a server-side component that runs on a Java EE application server.
- An entity bean represents persistent data stored in a relational database, such as a customer, an order, or a product.
- An entity bean can have a remote or a local interface, depending on whether it is accessed by clients in the same or different JVMs.
- An entity bean can manage its own persistence (bean-managed persistence or BMP) or delegate this function to its container (container-managed persistence or CMP).
- An entity bean has a primary key, a unique identifier that distinguishes it from other entity beans of the same type.
- An entity bean can have relationships with other entity beans, such as one-to-one, one-to-many, or many-to-many.
- An entity bean can perform business logic on its data, such as validation, calculation, or transformation.
- An entity bean can participate in transactions, security, and concurrency control mechanisms provided by the container.
- An entity bean can have two types of life cycle methods: callback methods and home methods.
- Callback methods are invoked by the container to notify the entity bean of certain events, such as creation, activation, passivation, removal, or loading and storing of data.
- Home methods are defined in the home interface of the entity bean and are used by clients to create, find, or remove entity beans.