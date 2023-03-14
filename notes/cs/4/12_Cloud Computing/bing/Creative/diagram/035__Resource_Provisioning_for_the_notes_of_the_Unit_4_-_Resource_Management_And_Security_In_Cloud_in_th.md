Resource provisioning in cloud computing is the process of allocating cloud resources and services to customers according to their needs and preferences. Resource provisioning can be done using different models, such as advanced provisioning, dynamic provisioning, and user self-provisioning. Resource provisioning can also involve different types of resources, such as compute, storage, memory, network, and applications/services/microservices/lambdas.

The following diagram illustrates the basic architecture of resource provisioning in cloud computing using ASCII art:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|   Cloud User    |       |   Cloud Broker  |       |   Cloud Provider|
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                        |                        |
       |  Request resources    |                        |
       |---------------------->|                        |
       |                        |                        |
       |                        |  Negotiate resources   |
       |                        |----------------------->|
       |                        |                        |
       |                        |  Provision resources   |
       |                        |<-----------------------|
       |                        |                        |
       |  Access resources     |                        |
       |<----------------------|                        |
       |                        |                        |
       |  Release resources    |                        |
       |---------------------->|                        |
       |                        |                        |
       |                        |  Release resources     |
       |                        |----------------------->|
       |                        |                        |
```

: What is Cloud Provisioning? - SearchITChannel
: Resource Provisioning in a Cloud-Edge Computing Environment