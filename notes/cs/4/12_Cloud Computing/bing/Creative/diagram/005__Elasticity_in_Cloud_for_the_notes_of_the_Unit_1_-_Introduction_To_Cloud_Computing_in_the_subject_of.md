Elasticity in cloud computing is the ability to adapt to workload changes by provisioning and de-provisioning resources in an autonomic manner, such that at each point in time the available resources match the current demand as closely as possible. Elasticity is a defining characteristic that differentiates cloud computing from other computing paradigms, such as grid computing. Elasticity aims at matching the amount of resource allocated to a service with the amount of resource it actually requires, avoiding over- or under-provisioning.

The following diagram illustrates the basic concept of elasticity in cloud computing using ASCII art:

```
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Workload      |      |   Workload      |      |   Workload      |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            V                       V                       V
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Cloud         |      |   Cloud         |      |   Cloud         |
    |   Provider      |      |   Provider      |      |   Provider      |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            V                       V                       V
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Resources     |      |   Resources     |      |   Resources     |
    |   (CPU, RAM,    |      |   (CPU, RAM,    |      |   (CPU, RAM,    |
    |   Storage, etc.)|      |   Storage, etc.)|      |   Storage, etc.)|
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            V                       V                       V
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Service       |      |   Service       |      |   Service       |
    |   Provider      |      |   Provider      |      |   Provider      |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            V                       V                       V
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Service       |      |   Service       |      |   Service       |
    |   (Website,     |      |   (Website,     |      |   (Website,     |
    |   Application,  |      |   Application,  |      |   Application,  |
    |   etc.)         |      |   etc.)         |      |   etc.)         |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+
            |                       |                       |
            |                       |                       |
            |                       |                       |
            V                       V                       V
    +-----------------+      +-----------------+      +-----------------+
    |                 |      |                 |      |                 |
    |   Users         |      |   Users         |      |   Users         |
    |                 |      |                 |      |                 |
    +-----------------+      +-----------------+      +-----------------+

    (a) Low workload   (b) High workload  (c) Low workload
```

In (a), the workload is low and the service provider only needs a few resources from the cloud provider to serve the users. In (b), the workload increases due to a surge in demand and the service provider needs more resources from the cloud provider to serve the users. In (c), the workload decreases again and the service provider releases the excess resources to the cloud provider. This is an example of elasticity