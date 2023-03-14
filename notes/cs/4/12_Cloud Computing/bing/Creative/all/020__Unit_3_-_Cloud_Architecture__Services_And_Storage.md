## Unit 3 - Cloud Architecture, Services And Storage

- Cloud architecture is the design of the components, systems, and resources that make up a cloud computing platform.
- Cloud services are the capabilities and functions that are delivered by the cloud provider to the cloud users, such as computing, storage, networking, security, analytics, etc.
- Cloud storage is the service that allows cloud users to store, access, and manage data on the cloud provider's infrastructure, such as files, databases, backups, etc.

### Cloud Architecture Components

- Cloud architecture consists of the following main components:

  - Cloud infrastructure: The physical and virtual resources that provide the computing, storage, and networking capabilities for the cloud platform, such as servers, switches, routers, hypervisors, etc.
  - Cloud platform: The software layer that enables the delivery and management of cloud services, such as operating systems, middleware, databases, applications, etc.
  - Cloud management: The tools and processes that allow the cloud provider and the cloud users to monitor, control, and optimize the cloud resources and services, such as billing, provisioning, orchestration, security, etc.
  - Cloud access: The interfaces and protocols that allow the cloud users to access and use the cloud services, such as web browsers, APIs, SDKs, CLI, etc.

- Cloud architecture can be represented by a diagram that shows the relationships and interactions among the components, such as the following example:

```
+-----------------+     +-----------------+
|                 |     |                 |
|   Cloud User    |     |   Cloud User    |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
|                 |     |                 |
|   Cloud Access  |     |   Cloud Access  |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
|                 |     |                 |
|  Cloud Service  |     |  Cloud Service  |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
|                 |     |                 |
| Cloud Platform  |     | Cloud Platform  |
|                 |     |                 |
+-----------------+     +-----------------+
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
        |                       |
+-----------------+     +-----------------+
|                 |     |                 |
|Cloud Infrastructure|  |Cloud Infrastructure|
|                 |     |                 |
+-----------------+     +-----------------+
```

### Cloud Service Models

- Cloud service models are the categories of cloud services that define the level of abstraction, control, and responsibility of the cloud provider and the cloud user, such as:

  - Infrastructure as a Service (IaaS): The cloud provider delivers the cloud infrastructure (servers, storage, network, etc.) as a service, and the cloud user can provision, configure, and manage the infrastructure resources and run their own platform and applications on top of them.
  - Platform as a Service (PaaS): The cloud provider delivers the cloud platform (operating system, middleware, database, etc.) as a service, and the cloud user can deploy and run their own applications on the platform without managing the underlying infrastructure.
  - Software as a Service (SaaS): The cloud provider delivers the cloud software (application, data, etc.) as a service, and the cloud user can access and use the software via the cloud access without installing or managing anything on their own devices.

- Cloud service models can be represented by a diagram that shows the layers of the cloud stack and the division of responsibility between the cloud provider and the cloud user, such as the following example:

``