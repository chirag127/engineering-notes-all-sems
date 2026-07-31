#### Entity bean in Enterprise Java Bean

- Entity beans are a type of Enterprise Java Bean (EJB) that represents persistent data stored in a database.
- They provide an object-oriented view of the data, allowing developers to interact with the data using Java objects rather than SQL statements.
- Entity beans can be either container-managed or bean-managed.
- In container-managed persistence (CMP), the EJB container is responsible for managing the persistence of the entity bean. The container generates the necessary SQL statements to store and retrieve the data from the database.
- In bean-managed persistence (BMP), the developer is responsible for writing the code to manage the persistence of the entity bean. This includes writing the necessary SQL statements to store and retrieve the data from the database.
- Entity beans can participate in transactions, allowing multiple operations to be grouped together and either committed or rolled back as a single unit.
- They can also be accessed remotely, allowing clients to interact with the data from a different machine or even a different network.
- Entity beans can be used in a variety of applications, including web applications, enterprise applications, and mobile applications.

A mnemonic to remember the difference between CMP and BMP is: **C**ontainer-**M**anaged **P**ersistence is managed by the **C**ontainer, while **B**ean-**M**anaged **P**ersistence is managed by the **B**ean.