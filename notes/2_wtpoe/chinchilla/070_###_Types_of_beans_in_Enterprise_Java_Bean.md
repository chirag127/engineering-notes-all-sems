### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJBs) are components of the Java Enterprise Edition (Java EE) platform that provide a standard way to write server-side business logic. EJBs are managed by a container, which provides services such as lifecycle management, security, and transaction management. There are three types of EJBs:

1. Session Beans
Session beans are used to manage the interaction between the client and the server. They are stateful or stateless, depending on whether they maintain a conversational state or not. 

- Stateful session beans: maintain a conversational state with the client, allowing the client to perform multiple operations in a single session.
- Stateless session beans: don't maintain a conversational state with the client, allowing the server to handle multiple client requests concurrently.

Mnemonic: "Stateful beans store the conversation with clients, while Stateless beans don't."

2. Entity Beans
Entity beans represent persistent data in a database. They can be used to model the data in a relational database and provide a way to interact with that data using object-oriented programming concepts. 

- Container-managed persistence (CMP) entity beans: are managed by the container and use a mapping file to map the bean's fields to the database columns.
- Bean-managed persistence (BMP) entity beans: are responsible for managing their own persistence to the database.

Mnemonic: "CMP beans are managed by the container, while BMP beans manage their own persistence."

3. Message-Driven Beans
Message-driven beans (MDBs) are used to process messages asynchronously. They can receive messages from a JMS queue or topic and perform some action in response to the message.

Mnemonic: "MDBs process messages asynchronously."

Each type of EJB has its own unique characteristics, and choosing the right type depends on the specific requirements of the application. By understanding the different types of EJBs and their use cases, developers can make informed decisions about which type to use in their applications.