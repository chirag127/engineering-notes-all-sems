Resource provisioning is the process of allocating the cloud provider's resources to a client according to their needs and demands. There are different methods of resource provisioning in cloud computing, such as:

- Static provisioning or advance provisioning: This method is suitable for applications with known and constant workloads. The client requests a fixed amount of resources from the provider in advance and pays for them regardless of their usage. This method offers predictable performance and cost, but lacks flexibility and scalability.

- Dynamic provisioning or on-demand provisioning: This method is suitable for applications with variable and unpredictable workloads. The provider adds or removes resources as needed by the client and charges them based on their actual usage. This method offers flexibility and scalability, but may incur higher costs and lower performance.

- Adaptive provisioning or self-provisioning: This method is suitable for applications that can adjust their resource requirements based on the current conditions and feedback. The client or the provider can use automation tools or policies to monitor and optimize the resource utilization and performance. This method offers self-management and optimization, but may require complex algorithms and mechanisms.

The following diagram illustrates the basic architecture of a resource provisioning system in cloud computing:

```
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|     Client       |        |     Provider     |        |     Resource     |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Request         |------->|  Provision       |------->|  Allocate        |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Use             |<-------|  Monitor         |<-------|  Utilize         |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
|                  |        |                  |        |                  |
|  Release         |------->|  De-provision    |------->|  De-allocate     |
|                  |        |                  |        |                  |
+------------------+        +------------------+        +------------------+
```