The following diagram illustrates the basic architecture of a public, private and hybrid cloud using ASCII characters.

Public cloud: A cloud environment that is created from IT infrastructure not owned by the end user and is shared by multiple tenants. Public cloud providers offer cloud services such as IaaS or PaaS that can be accessed over the internet. Examples of public cloud providers are AWS, Azure, Google Cloud, etc.

Private cloud: A cloud environment that is dedicated to a single end user or group and is usually run behind their firewall. Private cloud users have complete control and isolation over their cloud resources and services. Private cloud can be sourced from on-premise or off-premise IT infrastructure. Examples of private cloud platforms are OpenStack, VMware, etc.

Hybrid cloud: A cloud environment that combines public and private cloud resources and services to create a single IT solution. Hybrid cloud allows users to leverage the benefits of both public and private cloud, such as scalability, flexibility, cost-effectiveness, security, and compliance. Hybrid cloud can also include edge computing, which brings the cloud closer to the data sources and devices. Examples of hybrid cloud platforms are Azure Stack, AWS Outposts, Google Anthos, etc.

```
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|                |    |                |    |                |
|  Public cloud  |    |  Private cloud |    |  Hybrid cloud  |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|                |    |                |    |                |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|  |          |  |    |  |          |  |    |  |          |  |
|  |   IaaS   |  |    |  |   IaaS   |  |    |  |   IaaS   |  |
|  |          |  |    |  |          |  |    |  |          |  |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|                |    |                |    |                |
|                |    |                |    |                |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|  |          |  |    |  |          |  |    |  |          |  |
|  |   PaaS   |  |    |  |   PaaS   |  |    |  |   PaaS   |  |
|  |          |  |    |  |          |  |    |  |          |  |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|                |    |                |    |                |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|  |          |  |    |  |          |  |    |  |          |  |
|  |   SaaS   |  |    |  |   SaaS   |  |    |  |   SaaS   |  |
|  |          |  |    |  |          |  |    |  |          |  |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
|                |    |                |    |                |
|                |    |                |    |                |
|  +----------+  |    |  +----------+  |    |  +----------+  |
|  |          |  |    |  |          |  |    |  |          |  |
|  |   Edge   |  |    |  |   Edge   |  |    |  |   Edge   |  |
|  |          |  |    |  |          |  |    |  |