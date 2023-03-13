The following is a detailed ASCII diagram for Strawman Architecture for Enterprise-wide SOA for the notes of the Unit 2 - Enterprise-Wide SOA in the subject of Service Oriented Architecture. The diagram is based on the information from the web search results    .

### Strawman Architecture for Enterprise-wide SOA

```
+-----------------+     +-----------------+     +-----------------+
|  Presentation   |     |  Business Logic |     |  Data Services  |
|    Services     |     |    Services     |     |    Services     |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| - Provide user  |     | - Implement the |     | - Provide data  |
|   interface     |     |   business      |     |   access and    |
| - Invoke        |     |   functionality |     |   manipulation  |
|   business      |     | - Invoke data   |     | - Invoke legacy |
|   services      |     |   services      |     |   systems       |
| - Handle        |     | - Handle        |     | - Handle        |
|   presentation  |     |   business      |     |   data          |
|   logic         |     |   logic         |     |   logic         |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         |                      |                      |
         v                      v                      v
+---------------------------------------------------------------+
|                          Enterprise Bus                        |
+---------------------------------------------------------------+
|                                                               |
| - Provide a common communication channel for services         |
| - Support various protocols and standards                     |
| - Enable service discovery, security, and governance          |
| - Facilitate service orchestration and composition            |
| - Provide service monitoring and management                   |
|                                                               |
+---------------------------------------------------------------+
```