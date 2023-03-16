### Cluster Middleware and SSI

- Cluster middleware is a software layer that provides a unified view of the cluster resources and services to the users and applications. It consists of two sub-layers: SSI infrastructure and SAI infrastructure .
- SSI stands for Single System Image, which is the illusion of a single powerful resource that is created by the cluster middleware. SSI enables the cluster to appear as a single machine to the users, applications, and the network .
- SSI infrastructure is the sub-layer of the cluster middleware that supports the SSI features, such as process migration, load balancing, distributed shared memory, global process management, global file system, global I/O, global IPC, and global naming .
- SAI stands for System Availability Infrastructure, which is the sub-layer of the cluster middleware that provides cluster services for fault tolerance and high availability, such as checkpointing, automatic failover, recovery from failure, and fault detection .
- SAI infrastructure is also responsible for managing the cluster membership, cluster configuration, cluster monitoring, and cluster administration .
- Some examples of cluster middleware and SSI systems are OpenSSI, MOSIX, Kerrighed, and OpenMosix.