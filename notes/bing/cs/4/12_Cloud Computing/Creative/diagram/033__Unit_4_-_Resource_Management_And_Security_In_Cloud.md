## Unit 4 - Resource Management And Security In Cloud

Resource management and security in cloud are two important aspects of cloud computing that aim to optimize the performance, availability, and protection of cloud resources and applications. Resource management is the process of allocating computing, storage, networking and energy resources to a set of applications in order to meet performance objectives and requirements of the infrastructure providers and the cloud users. Security management is the set of strategies designed to allow a business to use cloud applications and networks to their greatest potential while limiting potential threats and vulnerabilities. This is often done with several independent tactics, such as identifying and assessing cloud services, implementing security policies and controls, monitoring and auditing cloud activities, and responding to incidents and breaches.

The following diagram illustrates the basic architecture of a resource management and security system in cloud:

```
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Cloud Service  |       |  Cloud Service  |       |  Cloud Service  |
|  Provider (CSP) |       |  Provider (CSP) |       |  Provider (CSP) |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Resource       |       |  Resource       |       |  Resource       |
|  Manager        |       |  Manager        |       |  Manager        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Security       |       |  Security       |       |  Security       |
|  Manager        |       |  Manager        |       |  Manager        |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
       |                       |                       |
+-----------------+       +-----------------+       +-----------------+
|                 |       |                 |       |                 |
|  Cloud User     |       |  Cloud User     |       |  Cloud User     |
|                 |       |                 |       |                 |
+-----------------+       +-----------------+       +-----------------+
```

The diagram shows three cloud service providers (CSPs) that offer different cloud services to the cloud users. Each CSP has a resource manager that is responsible for allocating and managing the resources for the cloud services. The resource manager can use various techniques, such as virtualization, load balancing, scheduling, and elasticity, to optimize the resource utilization and performance of the cloud services. Each CSP also has a security manager that is responsible for ensuring the security of the cloud services and the cloud users. The security manager can use various techniques, such as encryption, authentication, authorization, firewall, and intrusion detection, to protect the cloud services and the cloud users from potential threats and vulnerabilities. The cloud users can access the cloud services through the security manager, which verifies their identity and enforces the security policies and controls. The cloud users can also monitor and audit the cloud activities and report any incidents or breaches to the security manager. The security manager can