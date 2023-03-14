The following diagram illustrates the basic architecture of a layered cloud, based on the information from the search results  . The diagram is drawn using ASCII characters.

### Layered Cloud Architecture Design

```
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Application    |  |  Application    |  |  Application    |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Platform       |  |  Platform       |  |  Platform       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Infrastructure |  |  Infrastructure |  |  Infrastructure |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Virtualization |  |  Virtualization |  |  Virtualization |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
|                 |  |                 |  |                 |
|  Physical       |  |  Physical       |  |  Physical       |
|                 |  |                 |  |                 |
+-----------------+  +-----------------+  +-----------------+
```

The layers are:

- **Physical layer**: This layer consists of the physical hardware and network resources that provide the computing power and storage capacity for the cloud. It can be heterogeneous and distributed across multiple locations. The physical layer can also include database systems and other storage services.
- **Virtualization layer**: This layer uses hypervisors or other technologies to create virtual machines or containers that abstract the physical resources and provide a flexible and isolated runtime environment for the applications. The virtualization layer also manages the pool of available resources and allocates them to the virtual machines or containers as needed.
- **Infrastructure layer**: This layer provides the basic services and capabilities that are required by the applications, such as compute, storage, networking, security, monitoring, etc. The infrastructure layer can be offered as a service (IaaS) to the users, who can provision and manage their own virtual machines or containers and run their applications on them.
- **Platform layer**: This layer provides the tools and frameworks that enable the development, deployment, and execution of applications on the cloud. The platform layer can be offered as a service (PaaS) to the users, who can use the provided tools and frameworks to create and run their applications without worrying about the underlying infrastructure. The platform layer can also provide scalability, reliability, and security features for the applications.
- **Application layer**: This layer consists of the actual cloud applications that provide the functionality and value to the users. The application layer can be offered as a service (SaaS) to the users, who can access the applications through web browsers or other interfaces without installing or maintaining them. The application layer can also take advantage of the automatic-scaling functionality to gain higher performance, availability, and lower operational costs.

The layers are connected to each other by user interfaces (UI), application programming interfaces (API), and middleware. The users can access the cloud services at different levels of abstraction, depending on their needs and preferences. The cloud architecture can also be classified into different types, such as public, private, hybrid, or community, based on the ownership, location, and access of the cloud resources.