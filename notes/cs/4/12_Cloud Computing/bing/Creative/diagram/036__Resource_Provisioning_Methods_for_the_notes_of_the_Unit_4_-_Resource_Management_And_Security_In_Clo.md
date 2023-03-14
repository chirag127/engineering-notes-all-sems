Resource provisioning methods in cloud computing are the ways of allocating and managing the cloud provider's resources and services to the customers. Resource provisioning is important for achieving scalability, speed, savings, and complex management of cloud resources. There are different types of resource provisioning methods, such as static provisioning, dynamic provisioning, automatic on-demand provisioning, and policy-based provisioning. The following diagram illustrates the basic architecture of resource provisioning methods in cloud computing using ASCII art:

```
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Static          |    |  Dynamic         |    |  Automatic       |
|  Provisioning    |    |  Provisioning    |    |  On-Demand       |
|                  |    |                  |    |  Provisioning    |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
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
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Cloud Provider  |    |  Cloud Provider  |    |  Cloud Provider  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
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
+------------------+    +------------------+    +------------------+
|                  |    |                  |    |                  |
|  Cloud Customer  |    |  Cloud Customer  |    |  Cloud Customer  |
|                  |    |                  |    |                  |
+------------------+    +------------------+    +------------------+
```

Static provisioning is when the cloud provider allocates a fixed amount of resources to the customer in advance, based on the customer's expected or constant demand. The customer is responsible for managing the resources and ensuring they are not overutilized. This method is suitable for applications with stable and predictable workloads, such as a database server.

Dynamic provisioning is when the cloud provider adjusts the amount of resources to the customer based on the customer's actual or variable demand. The provider adds resources as needed and subtracts them as they are no longer required. This method is suitable for applications with fluctuating and unpredictable workloads, such as a web server.

Automatic on-demand provisioning is when the cloud provider automatically allocates resources to the customer without any human intervention, based on the customer's request or trigger. The provider uses tools and policies to monitor the resource usage and provision resources accordingly. This method is suitable for applications that need to scale up and down quickly and frequently, such as a mobile app.

Policy-based provisioning is when the cloud provider allocates resources to the customer based on the customer's predefined rules or policies. The provider uses tools and policies to enforce the customer's requirements and constraints, such as cost, performance, security, and availability. This method is suitable for applications that need to comply with certain standards or regulations, such as a healthcare app.