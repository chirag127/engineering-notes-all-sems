According to the web search results, there are three types of beans in Enterprise Java Bean: session beans, entity beans, and message-driven beans   .

Session beans contain business logic that can be invoked by local, remote or web service clients. There are two types of session beans: stateful and stateless. Stateful session beans maintain a conversational state with the client, while stateless session beans do not. There is also a third type of session bean called singleton, which is instantiated only once and shared by all clients .

Entity beans represent persistent data stored in a database. They can be accessed by multiple clients and support transactions and concurrency. There are two types of entity beans: container-managed and bean-managed. Container-managed entity beans delegate the persistence logic to the container, while bean-managed entity beans implement their own persistence logic  .

Message-driven beans are used to process asynchronous messages from a message queue or a topic. They act as message consumers and can be triggered by the arrival of a message. They do not maintain any state and cannot be accessed directly by clients  .

The following diagram illustrates the basic architecture of a Java EE application using different types of beans:

```
+-----------------+    +-----------------+    +-----------------+
| Web Application |    | EJB Application |    | Database Server |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
| +-------------+ |    | +-------------+ |    | +-------------+ |
| | Web Client | |    | | EJB Client | |    | | Database    | |
| +-------------+ |    | +-------------+ |    | +-------------+ |
|       |         |    |       |         |    |       ^         |
|       |         |    |       |         |    |       |         |
|       v         |    |       v         |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
| | Web Server | |    | | EJB Server | |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
|       |         |    |       |         |    |       |         |
|       |         |    |       |         |    |       |         |
|       v         |    |       v         |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
| | Web Module | |    | | EJB Module | |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
|       |         |    |       |         |    |       |         |
|       |         |    |       |         |    |       |         |
|       v         |    |       v         |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
| | Servlet    | |    | | Session    | |    |       |         |
| +-------------+ |    | | Bean       | |    |       |         |
|       |         |    | +-------------+ |    |       |         |
|       |         |    |       |         |    |       |         |
|       v         |    |       v         |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
| | JSP        | |    | | Entity     | |    |       |         |
| +-------------+ |    | | Bean       | |    |       |         |
|       |         |    | +-------------+ |    |       |         |
|       |         |    |       |         |    |       |         |
|       v         |    |       v         |    |       |         |
| +-------------+ |    | +-------------+ |    |       |         |
| | JSF        | |    | | Message    | |    |       |         |
| +-------------+ |    | | Driven     | |    |       |         |
|       |         |    | | Bean       | |    |       |         |
|       |