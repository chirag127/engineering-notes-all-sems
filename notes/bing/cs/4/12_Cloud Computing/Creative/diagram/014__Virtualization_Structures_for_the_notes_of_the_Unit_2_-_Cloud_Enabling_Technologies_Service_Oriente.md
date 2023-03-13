The following is a detailed ASCII diagram for Virtualization Structures for Service Oriented Architecture (SOA) in the subject of Cloud Computing.

SOA is a method to create software components that are reusable and interoperable via service interfaces. Services use common interface standards and an architectural pattern so they can be rapidly incorporated into new applications.

Service virtualization is a method to emulate the behavior of specific components in SOA, such as APIs, cloud-based applications, and microservices. Service virtualization allows DevOps teams to use virtual services instead of production services for testing the system without the key components .

A typical SOA system consists of three layers: the consumer layer, the business layer, and the integration layer. The consumer layer is the interface that the end users interact with, such as web browsers or mobile apps. The business layer is the core logic that implements the business processes and rules, such as order processing or inventory management. The integration layer is the communication channel that connects the business layer with the external systems, such as databases, legacy systems, or third-party services .

Service virtualization can be applied to any of these layers, depending on the testing needs and the availability of the real services. For example, service virtualization can be used to:

- Emulate the consumer layer to test the business layer without the need for a user interface.
- Emulate the business layer to test the consumer layer or the integration layer without the need for the actual business logic.
- Emulate the integration layer to test the business layer or the consumer layer without the need for the external systems.

The diagram below shows an example of how service virtualization can be used to emulate the integration layer for testing the business layer. The virtual services are marked with (V).

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Consumer       |      |  Business       |      |  Integration    |
|  Layer          |      |  Layer          |      |  Layer          |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Web Browser    |      |  Order          |      |  Database       |
|                 |----->|  Processing     |----->|                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Mobile App     |      |  Inventory      |      |  Legacy System  |
|                 |----->|  Management     |----->|                 |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Desktop App    |      |  Customer       |      |  Third-Party    |
|                 |----->|  Service        |----->|  Service (V)    |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
```

In this example, the third-party service is not available for testing, so a virtual service is created to mimic its behavior and response. The virtual service can be configured to return different data or scenarios, such as success, failure, delay, or error. This way, the business layer can be tested with various inputs and outputs without depending on the real third-party service.