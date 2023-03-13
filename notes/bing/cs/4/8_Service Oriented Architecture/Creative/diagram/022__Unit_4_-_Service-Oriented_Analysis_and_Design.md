## Unit 4 - Service-Oriented Analysis and Design

Service-oriented analysis and design (SOAD) is a methodology that refers to the modeling and design for service-oriented architecture (SOA) applications. A SOAD approach in designing SOA applications requires the following key elements:

- Identification of services and service candidates
- Specification of service contracts and interfaces
- Definition of service compositions and orchestrations
- Allocation of services to components and nodes
- Verification and validation of services and service compositions

The following diagram illustrates the basic architecture of a SOA application using the SOAD methodology:

```
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Consumer       |        |  Provider       |        |  Registry       |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Requestor      |        |  Implementation |        |  Repository     |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Contract       |        |  Contract       |        |  Contract       |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Proxy          |        |  Endpoint       |        |  Discovery      |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Bus            |        |  Bus            |        |  Bus            |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Invocation     |        |  Invocation     |        |  Invocation     |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Message        |        |  Message        |        |  Message        |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Metadata       |        |  Metadata       |        |  Metadata       |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Description    |        |  Description    |        |  Description    |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Interface      |        |  Interface      |        |  Interface      |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Model          |        |  Model          |        |  Model          |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Logic          |        |  Logic          |        |  Logic          |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Data           |        |  Data           |        |  Data           |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  State          |        |  State          |        |  State          |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Context        |        |  Context        |        |  Context        |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Quality        |        |  Quality        |        |  Quality        |
+-----------------+        +-----------------+        +-----------------+
|  Service        |        |  Service        |        |  Service        |
|  Policy         |        |  Policy         |        |  Policy         |
+-----------------+        +----------------