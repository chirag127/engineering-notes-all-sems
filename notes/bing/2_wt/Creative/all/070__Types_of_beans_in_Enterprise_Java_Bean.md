### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) are Java components that can be combined with other resources to create Java applications. They provide business logic and data access functionality to the applications. There are three types of EJB: session beans, entity beans, and message-driven beans   .

- **Session beans** contain business logic that can be invoked by local, remote, or web service clients. They do not persist data, but may access data from other sources. There are three types of session beans :
  - **Stateless session beans** do not keep a conversational state with the client. They are pooled and shared by multiple clients. They are suitable for stateless operations, such as calculations or validations.
  - **Stateful session beans** keep a conversational state with the client. They are not shared by other clients. They are suitable for stateful operations, such as shopping carts or wizards.
  - **Singleton session beans** are instantiated once per application and exist for the lifecycle of the application. They are shared by all clients. They are suitable for application-wide settings or caching.
- **Entity beans** represent persistent data stored in a database. They provide an object-oriented view of the data and encapsulate the access logic. There are two types of entity beans :
  - **Container-managed persistence (CMP) entity beans** delegate the persistence logic to the container. The container generates the database access code based on the bean's fields and relationships. They are easier to develop and maintain, but less flexible and performant.
  - **Bean-managed persistence (BMP) entity beans** implement the persistence logic in the bean code. The bean developer is responsible for writing the database access code. They are more flexible and performant, but harder to develop and maintain.
- **Message-driven beans** are invoked by messages from a Java Message Service (JMS) provider. They act as asynchronous event listeners and can process multiple messages concurrently. They do not persist data, but may access data from other sources. They are suitable for integrating applications with messaging systems .

A possible mnemonic to remember the types of EJB is **SEEM** (Session, Entity, Entity, Message). Another possible mnemonic is **BESS** (Bean, Entity, Session, Session).

Some possible learning tricks for the types of EJB are:

- To remember the difference between stateless and stateful session beans, think of a stateless bean as a calculator that can perform any operation without remembering the previous inputs or outputs, and a stateful bean as a shopping cart that can store the items and the total amount for each customer.
- To remember the difference between CMP and BMP entity beans, think of a CMP bean as a car that is managed by the dealer, who takes care of the maintenance and repairs, and a BMP bean as a car that is managed by the owner, who has to do the maintenance and repairs by themselves.
- To remember the difference between session beans and message-driven beans, think of a session bean as a phone call that can be initiated by the client or the bean, and a message-driven bean as a voicemail that can only be initiated by the client.