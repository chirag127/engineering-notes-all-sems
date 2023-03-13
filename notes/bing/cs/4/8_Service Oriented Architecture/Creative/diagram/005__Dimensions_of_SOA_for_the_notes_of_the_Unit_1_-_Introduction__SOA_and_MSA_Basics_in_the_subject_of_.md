According to , Service-Oriented Architecture (SOA) is an architectural approach in which applications make use of services available in the network. These services are loosely coupled, reusable, and interoperable. SOA aims to improve the agility, scalability, and efficiency of business processes.

One way to represent the dimensions of SOA is to use a layered model, as shown in the following diagram:

```
+-------------------+
| Business Services |
+-------------------+
|   Orchestration   |
+-------------------+
|   Composition     |
+-------------------+
|  Infrastructure   |
+-------------------+
```

The business services layer contains the core business logic and functionality of the system. It exposes the services that can be consumed by other applications or users.

The orchestration layer coordinates the execution of multiple services to achieve a business goal. It uses a workflow engine or a business process management system to define and manage the business processes.

The composition layer combines the services from the business services layer or external sources to create new services or applications. It uses a service bus or a service registry to facilitate the discovery and integration of services.

The infrastructure layer provides the basic support for the communication, security, and management of the services. It includes the network, the protocols, the middleware, and the monitoring tools.