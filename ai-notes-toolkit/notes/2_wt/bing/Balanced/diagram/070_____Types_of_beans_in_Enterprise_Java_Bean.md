According to the web search results, there are three types of beans in Enterprise Java Bean: session beans, entity beans, and message-driven beans. Session beans contain business logic that can be invoked by local, remote, or web service clients. Entity beans represent persistent data in a database. Message-driven beans handle asynchronous messages from a message queue or topic.

Here is a diagram that shows the types of beans and their relationships:

### Types of beans in Enterprise Java Bean

```
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  Session Bean    |      |  Entity Bean     |      | Message-Driven   |
|                  |      |                  |      |     Bean         |
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  - Stateful      |      |  - Bean-Managed  |      |  - Message-      |
|  - Stateless     |      |  - Container-    |      |    Listener      |
|  - Singleton     |      |    Managed       |      |                  |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  - Local         |      |  - Local         |      |  - Message-      |
|  - Remote        |      |  - Remote        |      |    Driven        |
|  - No-Interface  |      |                  |      |    Context       |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
|                  |      |                  |      |                  |
|  - Business      |      |  - Primary Key   |      |  - onMessage()   |
|    Methods       |      |  - Finder        |      |                  |
|  - Lifecycle     |      |  - Home          |      |                  |
|    Callbacks     |      |  - EJB QL        |      |                  |
|                  |      |                  |      |                  |
+------------------+      +------------------+      +------------------+
```