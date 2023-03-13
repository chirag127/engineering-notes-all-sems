There are different types of architectural diagrams that can be used to represent the structure and interactions of a software system. One of them is the layered (N-tier) architecture, which organizes the system into horizontal layers that communicate with each other through well-defined interfaces. Each layer has a specific responsibility and provides services to the layer above it. A common example of a layered architecture is the three-tier architecture, which consists of a presentation layer, a business logic layer, and a data access layer.

The following diagram illustrates the basic architecture of a three-tier system:

### Level
```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Presentation    |      | Business Logic  |      | Data Access     |
| Layer           |      | Layer           |      | Layer           |
|                 |      |                 |      |                 |
| (UI, Web, etc.) | <--> | (Application,   | <--> | (Database,      |
|                 |      |  Service, etc.) |      |  File, etc.)    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```