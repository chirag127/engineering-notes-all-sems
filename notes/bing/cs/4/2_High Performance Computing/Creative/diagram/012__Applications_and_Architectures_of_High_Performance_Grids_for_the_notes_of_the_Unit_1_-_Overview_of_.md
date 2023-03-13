The following is a detailed ascii diagram for Applications and Architectures of High Performance Grids for the notes of the Unit 1 - Overview of Grid Computing Technology in the subject of High Performance Computing.

### Applications and Architectures of High Performance Grids

Grid computing is a distributed computing paradigm that enables the sharing and coordination of heterogeneous and geographically dispersed resources across multiple administrative domains. Grid computing can support various types of applications, such as high-performance computing (HPC), data-intensive computing, service-oriented computing, and collaborative computing. Grid computing can also provide different levels of quality of service (QoS), such as performance, reliability, security, and availability.

A typical grid architecture consists of four layers: the fabric layer, the connectivity layer, the resource layer, and the application layer. The following diagram illustrates the basic architecture of a grid:

```
+---------------------+
| Application Layer   |
|                     |
| - Grid Applications |
| - Grid Services     |
| - Grid Portals      |
| - Grid Toolkits     |
+---------------------+
| Resource Layer      |
|                     |
| - Resource Brokers  |
| - Resource Managers |
| - Resource Monitors |
| - Resource Adapters |
+---------------------+
| Connectivity Layer  |
|                     |
| - Grid Protocols    |
| - Grid Middleware   |
| - Grid Security     |
| - Grid APIs         |
+---------------------+
| Fabric Layer        |
|                     |
| - Grid Resources    |
| - Grid Devices      |
| - Grid Networks     |
+---------------------+
```

The fabric layer provides the physical and logical resources that are available for grid computing, such as computers, storage, sensors, networks, etc. The fabric layer also provides the interfaces and mechanisms for accessing and controlling these resources.

The connectivity layer provides the communication and coordination services for grid computing, such as protocols, middleware, security, and APIs. The connectivity layer enables the interoperability and integration of heterogeneous and distributed resources across different grid domains.

The resource layer provides the management and allocation services for grid computing, such as brokers, managers, monitors, and adapters. The resource layer enables the discovery, reservation, scheduling, execution, and accounting of grid resources according to the application requirements and the grid policies.

The application layer provides the user and application services for grid computing, such as applications, services, portals, and toolkits. The application layer enables the development, deployment, and execution of grid applications and services with different functionalities and QoS levels. The application layer also provides the user interfaces and access points for grid computing.