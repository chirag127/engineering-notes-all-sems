## Unit 2 - Open Grid Services Architecture

- Open Grid Services Architecture (OGSA) is a set of standards that extends Web services and service-oriented architecture to the grid computing environment .
- OGSA defines how information is shared and distributed among the components of large, heterogeneous grid systems; it applies to hardware, platforms and software.
- OGSA aims to provide a common, open, and extensible framework for distributed system integration, virtualization, and management.
- OGSA uses most of Web service technologies, notably WSDL and SOAP, but it also introduces some new concepts and specifications, such as:
  - Grid service: a Web service that conforms to a set of conventions and interfaces that provide a uniform way to create, manage, and discover grid resources.
  - Grid resource: a logical entity that can be accessed and manipulated through a grid service; it can represent a physical resource (such as a computer, a network, or a sensor), a logical resource (such as a database, a file, or a job), or a service resource (such as a registry, a broker, or a monitor).
  - Service data: a set of XML elements that describe the state and properties of a grid resource; it can be accessed and modified through a grid service.
  - Factory: a grid service that can create new grid services and resources.
  - Handle: a globally unique and persistent identifier for a grid service or resource.
  - Reference: a set of information that allows a client to locate and interact with a grid service or resource; it includes a handle and a service endpoint.
  - Notification: a mechanism for a grid service to send asynchronous messages to other grid services or clients about events or changes in its state or service data.
- OGSA also defines some common grid services and resources that provide basic functionalities for grid applications, such as:
  - Information and monitoring: services and resources that collect, store, and disseminate information about the grid system, such as its topology, configuration, performance, and availability.
  - Execution management: services and resources that manage the execution of tasks and jobs on the grid, such as scheduling, dispatching, and checkpointing.
  - Data management: services and resources that manage the access, transfer, replication, and storage of data on the grid, such as catalogs, repositories, and file systems.
  - Security: services and resources that provide authentication, authorization, encryption, and auditing for the grid, such as certificates, policies, and proxies.
  - Self-management: services and resources that enable the grid system to adapt to changing conditions and requirements, such as load balancing, fault tolerance, and configuration management.

- A possible mnemonic to remember the main concepts and specifications of OGSA is:

  - **G**rid service: a Web service that conforms to OGSA
  - **R**esource: a logical entity that can be accessed and manipulated through a grid service
  - **S**ervice data: a set of XML elements that describe the state and properties of a resource
  - **F**actory: a grid service that can create new grid services and resources
  - **H**andle: a globally unique and persistent identifier for a grid service or resource
  - **R**eference: a set of information that allows a client to locate and interact with a grid service or resource
  - **N**otification: a mechanism for a grid service to send asynchronous messages to other grid services or clients

  - **GRS-FHRN**: a word that sounds like "griffin", a mythical creature that is half eagle and half lion.