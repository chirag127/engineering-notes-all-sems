# Resource sharing for the notes of the Unit 1 - Characterization of Distributed Systems in the subject of DISTRIBUTED SYSTEM

- Resource sharing is one of the main goals and benefits of distributed systems.
- Resource sharing means that the users and applications can access and use the resources (such as data, files, devices, services, etc.) that are available in a distributed system, regardless of their physical location, ownership, or access policy.
- Resource sharing can improve the performance, reliability, scalability, and availability of distributed systems, as well as reduce the cost and complexity of managing them.
- Resource sharing can be achieved by different methods, such as:
  - File sharing: the users and applications can access and manipulate files that are stored on remote servers or peers, using protocols such as NFS, SMB, FTP, HTTP, etc.
  - Data sharing: the users and applications can access and query databases or data warehouses that are distributed across multiple nodes, using protocols such as SQL, ODBC, JDBC, etc.
  - Device sharing: the users and applications can access and use devices (such as printers, scanners, cameras, etc.) that are connected to remote nodes, using protocols such as IPP, SANE, etc.
  - Service sharing: the users and applications can access and invoke services (such as web services, cloud services, microservices, etc.) that are provided by remote nodes, using protocols such as SOAP, REST, RPC, etc.
- Resource sharing can be classified into two types, depending on the degree of transparency and coordination among the nodes that share the resources:
  - Unstructured resource sharing: the nodes that share the resources do not have any global knowledge or agreement about the availability, location, or state of the resources, and rely on mechanisms such as discovery, advertisement, or negotiation to find and access the resources. Examples of unstructured resource sharing are peer-to-peer systems, service-oriented systems, etc.
  - Structured resource sharing: the nodes that share the resources have some global knowledge or agreement about the availability, location, or state of the resources, and rely on mechanisms such as replication, caching, or consistency to access and update the resources. Examples of structured resource sharing are distributed file systems, distributed databases, etc.