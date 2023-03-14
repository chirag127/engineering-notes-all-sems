According to the web search results, there are three types of beans in Enterprise Java Bean: session beans, entity beans, and message-driven beans. Session beans encapsulate business logic that can be invoked by a client, either locally or remotely. Entity beans represent persistent data stored in a database. Message-driven beans handle asynchronous messages from a message queue or topic.

The following diagram illustrates the basic architecture of a Java EE application using different types of beans:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Web Container   |    |  EJB Container   |    |  Database Server |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Servlets/JSPs   |    |  Session Beans   |    |  Entity Beans    |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Web Services    |    |  Message-Driven  |    |                  |
|                  |    |  Beans           |    |                  |
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Web Clients     |    |  JMS Clients     |    |                  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+

```