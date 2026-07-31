### Cluster Middleware and SSI

- Cluster middleware is a software layer that resides between the operating system and the user-level environment of a cluster system .
- Cluster middleware provides services and functionalities that enable the cluster to operate as a single system, such as resource management, load balancing, communication, fault tolerance, security, etc .
- Single System Image (SSI) is a property of a cluster system that hides the heterogeneous and distributed nature of the available resources and presents them to users and applications as a single unified computing resource .
- SSI creates an illusion of resources such as hardware or software that presents a single powerful resource, such as a single memory space, a single file system, a single process space, a single network address, etc  .
- SSI is supported by a middleware layer that consists of two sub-layers, namely SSI Infrastructure and System Availability Infrastructure (SAI) .
- SSI Infrastructure provides services such as process migration, global process management, distributed shared memory, global file system, global network address, etc .
- SAI provides services such as check pointing, automatic failover, recovery from failure and fault-tolerance .
- SSI enhances the performance, scalability, availability, manageability and usability of cluster systems .
- SSI can be implemented at different levels, such as hardware level, operating system level, middleware level or application level .
- Examples of SSI systems are OpenSSI, Kerrighed, MOSIX, etc  .