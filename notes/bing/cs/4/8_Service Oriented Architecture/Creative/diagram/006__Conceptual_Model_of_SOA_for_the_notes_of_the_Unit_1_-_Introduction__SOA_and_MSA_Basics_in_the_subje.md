The following is a detailed ASCII diagram for the conceptual model of SOA, based on the information from the search results. The diagram shows the four main components of SOA: service consumer, service provider, service description, and service broker. The diagram also shows the interactions between these components, such as service discovery, service invocation, service registration, and service binding.

### Conceptual Model of SOA

```
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Service        |     | Service        |     | Service        |
| Consumer       |     | Description    |     | Provider       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
       |                      |                      |
       |                      |                      |
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Service        |     | Service        |     | Service        |
| Discovery      |     | Binding        |     | Invocation     |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Service        |     | Service        |     | Service        |
| Registration   |     | Discovery      |     | Binding        |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
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
+----------------+     +----------------+     +----------------+
|                |     |                |     |                |
| Service        |     | Service        |     | Service        |
| Provider       |     | Description    |     | Consumer       |
|                |     |                |     |                |
+----------------+     +----------------+     +----------------+
```