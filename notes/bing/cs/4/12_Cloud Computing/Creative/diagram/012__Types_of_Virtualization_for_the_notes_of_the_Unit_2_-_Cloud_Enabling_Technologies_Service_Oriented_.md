Virtualization is a technique that allows the creation of multiple isolated and independent virtual environments on a single physical machine. Virtualization enables the efficient utilization of resources, flexibility, scalability, and security in cloud computing.

There are different types of virtualization in cloud computing, such as:

- **Server virtualization**: Server virtualization is a process that partitions a physical server into multiple virtual servers. Each virtual server can run its own operating system and applications, and share the resources of the physical server. Server virtualization reduces the cost and complexity of managing multiple physical servers, and improves the availability and performance of the applications.

- **Storage virtualization**: Storage virtualization is a process that abstracts the physical storage devices and presents them as a single logical storage unit. Storage virtualization enables the pooling, sharing, and allocation of storage resources among multiple virtual servers, and simplifies the backup, recovery, and migration of data.

- **Network virtualization**: Network virtualization is a process that combines multiple physical networks into one virtual network, or splits one physical network into multiple virtual networks. Network virtualization allows the creation of isolated and secure virtual networks for different applications, and enhances the network performance, scalability, and security.

- **Data virtualization**: Data virtualization is a process that integrates data from different sources and formats, and provides a unified and consistent view of the data to the applications. Data virtualization enables the access, analysis, and manipulation of data without requiring physical data movement or replication, and improves the data quality, availability, and governance.

- **Application virtualization**: Application virtualization is a process that decouples the applications from the underlying operating system and hardware, and delivers them as a service to the users. Application virtualization enables the remote access, deployment, and management of applications, and reduces the compatibility and security issues of the applications.

- **Desktop virtualization**: Desktop virtualization is a process that separates the user's desktop environment from the physical device, and delivers it as a service from a centralized server. Desktop virtualization enables the access, personalization, and security of the desktop from any device, and reduces the cost and complexity of maintaining the desktops.

The following diagram illustrates the basic architecture of a virtualized cloud environment:

```
+----------------------------------------+
|                                        |
|              Cloud Provider            |
|                                        |
+----------------------------------------+
|                                        |
|    +----------------+   +-----------+  |
|    |  Hypervisor    |   |  Storage  |  |
|    +----------------+   +-----------+  |
|    |                |   |           |  |
|    |  Virtual       |   |  Virtual  |  |
|    |  Servers       |   |  Storage  |  |
|    |                |   |           |  |
|    +----------------+   +-----------+  |
|    |                |   |           |  |
|    |  Physical      |   |  Physical |  |
|    |  Servers       |   |  Storage  |  |
|    |                |   |           |  |
|    +----------------+   +-----------+  |
|                                        |
+----------------------------------------+
|                                        |
|    +----------------+   +-----------+  |
|    |  Virtual       |   |  Virtual  |  |
|    |  Network       |   |  Data     |  |
|    +----------------+   +-----------+  |
|    |                |   |           |  |
|    |  Physical      |   |  Physical |  |
|    |  Network       |   |  Data     |  |
|    |                |   |           |  |
|    +----------------+   +-----------+  |
|                                        |
+----------------------------------------+
|                                        |
|    +----------------+   +-----------+  |
|    |  Application   |   |  Desktop  |  |
|    |  Virtualization|   |  Virtualization|
|    +----------------+   +-----------+  |
|    |                |   |           |  |
|    |  Applications  |   |  Desktops |  |
|    |                |   |           |  |
|    +----------------+   +-----------+  |
|                                        |
+----------------------------------------+
|                                        |
|              Cloud Users               |
|                                        |
+----------------------------------------+
```