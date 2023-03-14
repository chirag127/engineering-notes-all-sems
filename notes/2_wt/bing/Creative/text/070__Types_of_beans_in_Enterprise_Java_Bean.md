### Types of beans in Enterprise Java Bean

Enterprise Java Bean (EJB) is a server-side component that encapsulates the business logic of an application. It is a specification for developing distributed business applications on the Java platform. There are three types of beans in EJB: session beans, message-driven beans, and entity beans   .

- **Session beans** are beans that perform business tasks for a client, either locally or remotely. They do not have any persistent state and are usually short-lived. There are three types of session beans: stateless, stateful, and singleton  .
  - **Stateless session beans** are beans that do not maintain any conversational state with the client. They can be shared by multiple clients and are pooled by the container for better scalability. They are suitable for generic tasks that do not depend on the client's identity or previous interactions  .
  - **Stateful session beans** are beans that maintain a conversational state with the client across multiple requests. They are bound to a specific client and are not shared by others. They are suitable for tasks that require the bean to remember the client's preferences or actions  .
  - **Singleton session beans** are beans that are instantiated only once per application and are shared by all clients. They are used for application-wide tasks such as caching, logging, or configuration .
- **Message-driven beans** are beans that act as message consumers and process messages asynchronously from a message queue or topic. They are similar to stateless session beans in that they do not have any state and are pooled by the container. They are suitable for tasks that require a decoupled and reliable communication between components .
- **Entity beans** are beans that represent persistent data in a database. They are deprecated since EJB 3.0 and replaced by Java Persistence API (JPA) entities. They are not recommended for use in new applications  .

: https://stackify.com/enterprise-java-beans/
: https://www.javatpoint.com/types-of-ejb
: https://www.ibm.com/docs/en/was-nd/8.5.5?topic=applications-enterprise-beans
: https://www.geeksforgeeks.org/enterprise-java-beans-ejb/