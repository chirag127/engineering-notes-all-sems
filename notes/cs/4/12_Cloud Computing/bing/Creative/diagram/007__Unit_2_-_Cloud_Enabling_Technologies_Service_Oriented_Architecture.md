## Unit 2 - Cloud Enabling Technologies Service Oriented Architecture

Service Oriented Architecture (SOA) is a design paradigm that focuses on discrete services that can be reused and interoperable via service interfaces. Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications. Services can be classified as different types like subsystems or tiers, and can be implemented in different programming languages, platforms, or vendors. Services communicate with each other using standard network protocols, such as SOAP/HTTP or REST/HTTP, and can be orchestrated by a centralized or decentralized component, such as an Enterprise Service Bus (ESB) or a service registry.

The following diagram illustrates the basic architecture of a SOA:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service Tier   |       |  Business Tier  |       |  Data Tier      |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 1      |       |  Business 1     |       |  Data 1         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 2      |       |  Business 2     |       |  Data 2         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 3      |       |  Business 3     |       |  Data 3         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 4      |       |  Business 4     |       |  Data 4         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 5      |       |  Business 5     |       |  Data 5         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 6      |       |  Business 6     |       |  Data 6         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 7      |       |  Business 7     |       |  Data 7         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 8      |       |  Business 8     |       |  Data 8         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 9      |       |  Business 9     |       |  Data 9         |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 10     |       |  Business 10    |       |  Data 10        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 11     |       |  Business 11    |       |  Data 11        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 12     |       |  Business 12    |       |  Data 12        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Service 13     |       |  Business 13    |       |  Data 13        |
|                 |       |                 |       |                 |