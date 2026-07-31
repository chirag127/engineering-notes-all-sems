### Entity bean

- An entity bean is a type of Enterprise JavaBean, a server-side Java EE component, that represents persistent data maintained in a database.
- An entity bean can manage its own persistence (Bean managed persistence) or can delegate this function to its EJB Container (Container managed persistence).
- An entity bean is identified by a primary key, which is a unique identifier for each instance of the bean .
- Entity beans are normally coarse-grained persistent objects, in that they utilize persistent data stored within several fine-grained persistent Java objects.
- Fine-grained persistent Java objects typically manage persistent data that has a one-to-one mapping between the data and a table column.
- Entity beans can perform complex business logic, potentially using several dependent Java objects.
- Entity beans can be accessed by multiple clients concurrently, and the EJB Container ensures the consistency and integrity of the data.
- Entity beans can be either session beans or message-driven beans, depending on the type of communication they use with the clients.
- Session beans are synchronous and stateful, meaning they maintain a conversational state with a specific client.
- Message-driven beans are asynchronous and stateless, meaning they do not maintain any state and can process messages from multiple clients.
- Entity beans can be either container-managed or bean-managed, depending on the way they handle their persistence.
- Container-managed entity beans rely on the EJB Container to provide the persistence services, such as creating, updating, deleting, and finding the data.
- Bean-managed entity beans implement their own persistence logic, using JDBC or other APIs to access the database.
- Entity beans can participate in transactions, which are units of work that ensure the atomicity, consistency, isolation, and durability of the data operations.
- Entity beans can also use security mechanisms, such as authentication and authorization, to protect the data from unauthorized access.