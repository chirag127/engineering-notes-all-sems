### Cluster Middleware and SSI

- Cluster middleware is a software layer that provides a unified view of the cluster resources and services to the users and applications.
- Cluster middleware consists of two sub-layers: SSI infrastructure and SAI infrastructure.
- SSI stands for Single System Image, which is the property of a system that hides the heterogeneous and distributed nature of the available resources and presents them to users and applications as a single unified computing resource .
- SSI infrastructure provides features such as process migration, load balancing, distributed shared memory, global process management, global file system, global IPC, and global device access  .
- SAI stands for System Availability Infrastructure, which is the software layer that enables cluster services such as check pointing, automatic failover, recovery from failure and fault-tolerance .
- SAI infrastructure provides features such as cluster membership, cluster monitoring, cluster event notification, cluster configuration, and cluster management .
- An example of a cluster middleware that supports SSI and SAI is OpenSSI, which is an open source project that extends the Linux kernel to be a cluster operating system.
- OpenSSI is designed to be used for both high performance and high availability clusters. It is possible to create an OpenSSI cluster with no single point of failure, for example the file system can be mirrored between two nodes, so if one node crashes the process accessing the file will fail over to the other node.