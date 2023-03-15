Hello, I am Sydney, your AI assistant. I can help you with your query. According to the web search results, there are three types of beans in Enterprise Java Bean: session beans, entity beans, and message-driven beans. Here is a detailed ASCII diagram for the types of beans in Enterprise Java Bean:

### Types of beans in Enterprise Java Bean

```
+------------------------+     +------------------------+     +------------------------+
|                        |     |                        |     |                        |
|     Session Bean       |     |     Entity Bean        |     |  Message-Driven Bean   |
|                        |     |                        |     |                        |
+------------------------+     +------------------------+     +------------------------+
|                        |     |                        |     |                        |
|  - Contains business   |     |  - Represents a        |     |  - Acts as a listener  |
|    logic that can be   |     |    persistent data     |     |    for messages from   |
|    invoked by a        |     |    object in a         |     |    a message queue or  |
|    client              |     |    database            |     |    a topic             |
|                        |     |                        |     |                        |
|  - Can be stateful,    |     |  - Can be container-   |     |  - Does not maintain   |
|    stateless, or       |     |    managed or bean-    |     |    any conversational   |
|    singleton           |     |    managed             |     |    state with the      |
|                        |     |                        |     |    client              |
|  - Can be accessed     |     |  - Can be accessed     |     |                        |
|    locally or          |     |    locally or          |     |  - Implements the      |
|    remotely            |     |    remotely            |     |    MessageListener     |
|                        |     |                        |     |    interface           |
+------------------------+     +------------------------+     +------------------------+
```