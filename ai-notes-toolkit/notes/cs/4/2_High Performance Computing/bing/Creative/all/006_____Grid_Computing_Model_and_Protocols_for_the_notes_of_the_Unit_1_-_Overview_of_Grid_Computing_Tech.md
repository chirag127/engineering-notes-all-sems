# Grid Computing Model and Protocols

Grid computing is a distributed architecture of multiple computers connected by networks to accomplish a joint task. These tasks are compute-intensive and difficult for a single machine to handle. Several machines on a network collaborate under a common protocol and work as a single virtual supercomputer to get complex tasks done.

Grid computing is enabled via an open set of standards and protocols such as open grid services architecture (OGSA) that allow communication across heterogeneous systems and environments that are geographically dispersed.

A grid computing model consists of the following layers :

- The Fabric Layer: This layer includes the protocols and interfaces that provide access to the resources that are being shared such as compute resources, data resources, network resources, etc.
- The Connectivity Layer: This layer defines core protocols required for grid-specific network transactions such as security, authentication, authorization, resource discovery, etc.
- The Resource Layer: This layer defines protocols for the publication, monitoring, and management of resources on the grid such as CPU, memory, disk, etc.
- The Collective Layer: This layer defines protocols for the coordination and interaction of multiple resources on the grid such as scheduling, load balancing, data replication, etc.
- The Application Layer: This layer defines protocols for the development and execution of grid applications such as workflow, grid portals, grid services, etc.

Some of the core grid protocols that are used in implementing various activities and services for global grid deployment are:

- Grid Security Infrastructure (GSI): This protocol provides secure authentication and communication among grid entities using public key cryptography and X.509 certificates.
- Grid Resource Allocation and Management (GRAM): This protocol provides a uniform interface for requesting, accessing, monitoring, and controlling remote resources on the grid.
- Grid Resource Information Service (GRIS): This protocol provides a mechanism for publishing and discovering information about grid resources such as their attributes, capabilities, and availability.
- Grid File Transfer Protocol (GridFTP): This protocol extends the standard FTP protocol to support high-performance and reliable data transfer over the grid.
- Grid Monitoring Architecture (GMA): This protocol defines a framework for collecting, storing, and querying performance and status information about grid resources and services.
- Grid Service Specification (GSS): This protocol defines a common interface and behavior for grid services based on the web service standards such as SOAP, WSDL, and UDDI.