### Types of beans in Enterprise Java Bean

Enterprise Java Beans (EJB) are server-side components that encapsulate the business logic of an application. They are managed by an EJB container that provides services such as security, transaction management, dependency injection, concurrency control, etc.

There are three types of beans in EJB:

- **Session beans**: These are non-persistent objects that represent a single client-server interaction. They can be stateful or stateless. Stateful session beans maintain the conversational state of a client across multiple requests, while stateless session beans do not. Session beans can also be singleton, which means there is only one instance of the bean in the application and it is shared by all clients.
- **Message-driven beans**: These are stateless objects that act as message consumers and process messages asynchronously from a message queue or topic. They implement the javax.jms.MessageListener interface and are invoked by the EJB container when a message arrives.
- **Entity beans**: These are persistent objects that represent the data stored in a database. They can be container-managed or bean-managed. Container-managed entity beans delegate the persistence operations to the EJB container, while bean-managed entity beans handle the persistence operations themselves. Entity beans are deprecated since EJB 3.0 and replaced by Java Persistence API (JPA) entities.

A possible mnemonic to remember the types of beans is:

- Session beans are for sessions, either stateful or stateless, or singleton.
- Message-driven beans are for messages, always stateless and asynchronous.
- Entity beans are for entities, either container-managed or bean-managed, but deprecated.