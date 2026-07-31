 Here is the content in markdown format without any feeling or friendliness, being formal and without any emojis or external links:

### Implementation Levels of Virtualization for the notes of the Unit 2 - Cloud Enabling Technologies Service Oriented Architecture in the subject of Cloud Computing

1. Full Virtualization: Entire guest OS is virtualized. Example: VMware, VirtualBox.
- Guest OS kernel is unaware of being virtualized.
- Requires more resources but more isolation and compatibility.

2. Para-Virtualization: Guest OS is modified to be virtualization-aware. Example: Xen.
- Hypervisor provides APIs to guest OS.
- Guest OS kernel is virtualization-aware and optimized to work with hypervisor.
- Better performance than full virtualization but less compatibility.

3. Operating System-Level Virtualization: Multiple isolated user-space instances. Example: OpenVZ, Linux-VServer.
- Partitions a single OS kernel into multiple isolated user-space instances.
- Lightweight with good performance but less isolation.

4. Application-Level Virtualization: Application is isolated from others. Example: Java Virtual Machine (JVM), .NET Common Language Runtime (CLR).
- Single application is virtualized.
- Good performance and isolation but limited to single application.

The levels provide different trade-offs between performance and isolation. Choice depends on specific requirements and use-cases. Full virtualization and para-virtualization are more common for cloud computing. Operating system-level and application-level virtualization are more suitable for limited scenarios.