### Cluster Middleware and SSI

- Cluster middleware is a software layer that resides between the operating system and the user-level environment of a cluster system.
- Cluster middleware provides various services and functionalities to make the cluster appear as a single parallel machine to the user, to applications, and to the network.
- Cluster middleware consists of two sub-layers of software infrastructure: availability infrastructure and single system image (SSI) infrastructure.
- Availability infrastructure provides high availability (HA) services, such as fault detection, fault recovery, and load balancing, to ensure the reliability and performance of the cluster system.
- SSI infrastructure provides a single entry point, a single file hierarchy, a single point of control, and a single view of the cluster resources, such as processes, memory, and devices, to the user and applications.
- SSI can be implemented at different levels, such as hardware, operating system, middleware, or application level, depending on the degree of transparency and scalability required.
- SSI can also support different types of communication and synchronization mechanisms, such as message passing, remote procedure call, or shared memory, to facilitate the development and execution of parallel and distributed applications on the cluster system.
- Some examples of cluster middleware and SSI systems are OpenSSI, MOSIX, Kerrighed, and OpenPBS.