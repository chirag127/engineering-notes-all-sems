## Unit 4 - Resource Management And Security In Cloud

Resource management is the process of allocating computing, storage, networking and energy resources to a set of applications in order to meet performance objectives and requirements of the infrastructure providers and the cloud users.

Security management in the cloud is a set of strategies designed to allow a business to use cloud applications and networks to their greatest potential while limiting potential threats and vulnerabilities. This is often done with several independent tactics: Identifying and assessing cloud services, enforcing security policies, monitoring and auditing cloud activities, and remediating security issues.

The following diagram illustrates the basic architecture of a cloud resource management and security system:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|   Cloud User    |    | Cloud Provider  |    | Cloud Auditor   |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |                      +-----------------+
       |                      |                      |                      |                 |
       |                      |                      |                      |  Cloud Service  |
       |                      |                      |                      |                 |
       |                      |                      |                      +-----------------+
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |
       |                      |                      |                             |                      +-----------------+
       |                      |                      |                             |                      |                 |
       |                      |                      |                             |                      |  Cloud Resource |
       |                      |                      |                             |                      |                 |
       |                      |                      |                             |                      +-----------------+
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |
       |                      |                      |                             |                             |                      +-----------------+
       |                      |                      |                             |                             |                      |                 |
       |                      |                      |                             |                             |                      |  Resource Pool  |
       |                      |                      |                             |                             |                      |                 |
       |                      |                      |                             |                             |                      +-----------------+
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |
       |                      |                      |                             |                             |                             |                      +-----------------+
       |                      |                      |                             |                             |                             |                      |                 |
       |                      |                      |                             |                             |                             |                      |  Resource Node  |
       |                      |                      |                             |