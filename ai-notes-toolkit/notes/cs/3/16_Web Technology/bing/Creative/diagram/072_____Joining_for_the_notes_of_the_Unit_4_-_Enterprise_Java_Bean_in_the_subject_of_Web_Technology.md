Hello, I am Sydney, your AI assistant. I can help you with the notes of Unit 4 - Enterprise Java Bean in the subject of Web Technology. Here is the content in markdown format:

### Enterprise Java Bean

- Enterprise Java Bean (EJB) is a server-side component that encapsulates the business logic of an application.
- EJB is a part of the Java Platform, Enterprise Edition (Java EE) that provides a standard architecture for developing and deploying distributed applications.
- EJB provides services such as transaction management, security, concurrency, persistence, naming, and remote invocation.
- EJB can be classified into three types: session beans, entity beans, and message-driven beans.

#### Session Beans

- Session beans are stateful or stateless components that handle the requests from a single client.
- Stateful session beans maintain the conversational state with the client across multiple method calls.
- Stateless session beans do not maintain any state and can be pooled and reused by different clients.
- Session beans can be accessed by local or remote clients using Java interfaces or web services.

#### Entity Beans

- Entity beans are persistent components that represent the data stored in a database or other data sources.
- Entity beans can be accessed by multiple clients and can be shared among them.
- Entity beans can be container-managed or bean-managed, depending on who is responsible for the persistence logic.
- Entity beans are deprecated in Java EE 6 and replaced by Java Persistence API (JPA).

#### Message-Driven Beans

- Message-driven beans are components that process the messages asynchronously from a message queue or topic.
- Message-driven beans implement the Java Message Service (JMS) API and act as message consumers or listeners.
- Message-driven beans are stateless and can be pooled and reused by the container.
- Message-driven beans can be accessed by any client that can send messages using JMS.