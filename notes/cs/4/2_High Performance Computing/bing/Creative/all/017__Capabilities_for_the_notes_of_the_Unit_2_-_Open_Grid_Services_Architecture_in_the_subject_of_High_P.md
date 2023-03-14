### Capabilities for the notes of the Unit 2 - Open Grid Services Architecture in the subject of High Performance Computing

- Open Grid Services Architecture (OGSA) is a service-oriented architecture for grid computing that aims to enable interoperability, virtualization, and management of heterogeneous distributed systems and resources. 
- OGSA is based on several web service technologies, such as WSDL and SOAP, but it is largely independent of the transport-level handling of data. 
- OGSA defines a core set of interfaces, behaviors, resource models, and bindings that are required to support grid systems and applications in both e-science and e-business. 
- OGSA specifies the requirements, the scope, and the functionalities of important capabilities and services for grid computing, and identifies the interrelationships among them. 
- OGSA capabilities and services can be grouped into the following categories:  
  - Infrastructure services: These are the basic services that provide the foundation for other capabilities and services. They include service creation, naming, discovery, lifetime management, notification, and messaging. 
  - Execution Management services: These are the services that enable the creation, management, and coordination of executable entities, such as jobs, workflows, and services, on the grid. They include job submission, scheduling, monitoring, and control. 
  - Data services: These are the services that enable the access, transfer, replication, and management of data on the grid. They include data access, data movement, data replication, data catalog, and data virtualization. 
  - Resource Management services: These are the services that enable the allocation, reservation, negotiation, and sharing of resources on the grid. They include resource discovery, resource brokering, resource reservation, resource allocation, and resource accounting. 
  - Security services: These are the services that enable the authentication, authorization, encryption, and auditing of users, services, and resources on the grid. They include security context, security tokens, security policy, and security audit. 
  - Self-management services: These are the services that enable the self-configuration, self-optimization, self-healing, and self-protection of the grid system. They include policy management, fault management, performance management, and configuration management. 
  - Information services: These are the services that enable the collection, aggregation, dissemination, and analysis of information about the grid system, such as its structure, state, and behavior. They include information model, information provider, information consumer, and information registry. 

- A possible mnemonic to remember the categories of OGSA capabilities and services is: **IDEaRSIS** (pronounced as "ideas is"), which stands for **I**nfrastructure, **D**ata, **E**xecution Management, **R**esource Management, **S**ecurity, **I**nformation, and **S**elf-management. 
- A possible learning trick to understand the interrelationships among the OGSA capabilities and services is to draw a diagram that shows how they depend on each other and how they support the grid system and applications. For example, the following diagram illustrates the OGSA capabilities and services and their dependencies: 

```
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
|  Applications   |      |  Grid System    |      |  Grid Resources |
|                 |      |                 |      |                 |
+-----------------+      +-----------------+      +-----------------+
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
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
+-----------------+      +-----------------+      +-----------------+
|                 |      |                 |      |                 |
| Execution       |      | Infrastructure  |      | Resource        |
| Management